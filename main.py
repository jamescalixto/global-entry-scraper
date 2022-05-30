import argparse
from config import WEBHOOK_URL
from datetime import datetime
from discord_webhook import DiscordWebhook
import requests
import time


REQUEST_DELAY = 2
TIMESLOT_URL = "https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit={limit}&locationId={location_id}&minimum=1"
MAPPING_URL = "https://ttp.cbp.dhs.gov/schedulerapi/locations/?temporary=false&inviteOnly=false&operational=true&serviceName=Global%20Entry"


def import_mapping_from_url() -> dict:
    """Get mapping of location ids to location names from the TTP website."""
    r = requests.get(MAPPING_URL)
    return {
        location["id"]: "{} ({}, {})".format(
            location["name"], location["city"], location["state"]
        )
        for location in r.json()
    }


def parse_timeslot_datetime(timeslot: dict) -> dict:
    """Parse the timestamp of a single timeslot."""
    return datetime.strptime(timeslot["startTimestamp"], "%Y-%m-%dT%H:%M")


def get_timeslots_for_location_id(location_id: int, limit: int) -> set:
    """Get list of objects representing open slots for a certain location."""
    r = requests.get(TIMESLOT_URL.format(location_id=location_id, limit=limit))
    timeslots = [parse_timeslot_datetime(timeslot) for timeslot in r.json()]
    return sorted(list(set(timeslots)))


def get_timeslots_for_location_ids(
    location_ids: list, before: str = None, limit: int = 10
) -> list:
    """Get a mapping of location ids to open timeslots. Takes in an optional YYYY-MM-DD
    parameter to filter the results."""
    all_timeslots = {}
    for index, location_id in enumerate(location_ids):
        timeslots = [
            timeslot
            for timeslot in get_timeslots_for_location_id(location_id, limit)
            if before is None or datetime.strptime(before, "%Y-%m-%d") > timeslot
        ]
        all_timeslots[location_id] = timeslots
        if index < len(location_ids) - 1:  # delay between requests.
            time.sleep(REQUEST_DELAY)
    return all_timeslots


def generate_notification_texts(
    location_mapping: dict, all_timeslots: dict, silent: bool
) -> None:
    """Generate the text for the notification."""
    notification_texts = ["✈️ Global Entry Timeslot Bot ✈️"]
    for location_id, timeslots in all_timeslots.items():
        if len(timeslots) > 0:
            location_texts = []
            location_texts.append(
                "{} ({})".format(location_mapping[location_id], location_id)
            )
            for timeslot in timeslots:
                location_texts.append(
                    "    {}".format(
                        timeslot.strftime("%B %d, %Y (%a) @ %I:%M %p").replace(
                            " 0", " "
                        )
                    )
                )
            notification_texts.append("\n".join(location_texts))
    if len(notification_texts) == 1:
        if silent:
            return []
        else:
            notification_texts.append("No open timeslots found!")
    return notification_texts


def send_to_discord(notification_texts: str) -> None:
    """Send a notification to Discord."""
    for index, message in enumerate(notification_texts):
        webhook = DiscordWebhook(url=WEBHOOK_URL, content=message)
        webhook.execute()
        if index < len(notification_texts) - 1:  # delay between messages.
            time.sleep(REQUEST_DELAY)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--location-ids",
        nargs="+",
        type=int,
        help="List of location ids to check",
        required=True,
    )
    parser.add_argument(
        "--before",
        type=str,
        help="YYYY-MM-DD string of the date to filter results before",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit of appointments to fetch, per location",
    )
    parser.add_argument(
        "--silent",
        default=False,
        action="store_true",
        help="Suppress notifications if there are no open timeslots",
    )

    args = vars(parser.parse_args())
    kwargs = {
        k: args[k] for k in ["location_ids", "before", "limit"] if args[k] is not None
    }  # strip empty params for parameters when getting timeslots.

    location_mapping = import_mapping_from_url()
    all_timeslots = get_timeslots_for_location_ids(**kwargs)
    notification_text = generate_notification_texts(
        location_mapping, all_timeslots, args["silent"]
    )

    send_to_discord(notification_text)
