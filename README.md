# global-entry-scraper

Scraper for [Global Entry](https://www.cbp.gov/travel/trusted-traveler-programs/global-entry) appointments so that you can find timeslots at hotly contested locations.

## Usage

1. Clone the repo locally.
2. Create a `config.py` file with a single line, defining a string `WEBHOOK_URL` with the value of the Discord webhook URL.
3. Run it from the command line. It takes the following parameters:

- `--location-ids`, a space-separated list of location ids to check for appointments.
- `--before`, a YYYY-MM-DD formatted date to filter appointment lookups (only appointments before this date will be returned).
- `--limit`, the number of appointments per location to retrieve.

Example usage:
```python3 main.py --location-ids 5140 5444 --before 2023-01-01 --limit 5```

The script, of course, can be modified to provide notifications other than Discord messages.

## Location IDs

Each location has a unique numeric ID. They can be found at [this link](https://ttp.cbp.dhs.gov/schedulerapi/locations/?temporary=false&inviteOnly=false&operational=true&serviceName=Global%20Entry). A list is below:

|ID   |Name                                                                        |
|-----|----------------------------------------------------------------------------|
|5001 |Hidalgo Enrollment Center (Mission, TX)                                     |
|5002 |San Diego -Otay Mesa Enrollment Center (San Diego, CA)                      |
|5003 |Brownsville Enrollment Center (Brownsville, TX)                             |
|5004 |Laredo Enrollment Center (Laredo, TX)                                       |
|5005 |El Paso Enrollment Center (El Paso, TX)                                     |
|5006 |Calexico Enrollment Center (Calexico, CA)                                   |
|5007 |Nogales, AZ (Nogales, AZ)                                                   |
|5021 |Champlain Enrollment Center (Champlain, NY)                                 |
|5022 |Buffalo-Ft. Erie Enrollment Center (Fort Erie, ON)                          |
|5023 |Detroit Enrollment Center Global Entry (Detroit, MI)                        |
|5024 |Port Huron Enrollment Center (Port Huron, MI)                               |
|5025 |Ottawa International Airport (Ottawa, ON)                                   |
|5026 |Vancouver Enrollment Center (Richmond, BC)                                  |
|5027 |Toronto Enrollment Center (Mississauga, ON)                                 |
|5028 |Montreal Enrollment Center (Montreal, QC)                                   |
|5029 |Winnipeg Enrollment Center (Winnipeg, MB)                                   |
|5030 |Calgary Enrollment Center (Calgary, AB)                                     |
|5031 |Halifax Enrollment Center (Goffs, NS)                                       |
|5032 |Edmonton Enrollment Center (Edmonton, AB)                                   |
|5041 |Vancouver Urban Enrollment Center (Vancouver, BC)                           |
|5060 |Warroad Enrollment Center  (Warroad, MN)                                    |
|5080 |Sault Ste Marie Enrollment Center (Sault Ste. Marie, MI)                    |
|5101 |Houlton POE/Woodstock (Belleville, NB)                                      |
|5120 |Sweetgrass NEXUS and FAST Enrollment Center (Sweetgrass, MT)                |
|5140 |JFK International Global Entry EC (Jamaica, NY)                             |
|5141 |Houston Intercontinental Global Entry EC (Houston, TX)                      |
|5142 |Washington Dulles International Global Entry EC (Sterling, VA)             |
|5161 |Niagara Falls Enrollment Center (Niagara Falls, NY)                         |
|5180 |Los Angeles International Global Entry EC (Los Angeles, CA)                 |
|5181 |Miami International Airport (Miami, FL)                                     |
|5182 |Atlanta International Global Entry EC (Atlanta, GA)                         |
|5183 |Chicago O'Hare International Global Entry EC  (Chicago, IL)                 |
|5200 |Atlanta Port Office Global Entry Enrollment Center (Atlanta, GA)            |
|5223 |Derby Line Enrollment Center (Derby Line, VT)                               |
|5300 |Dallas-Fort Worth International Airport Global Entry (DFW Airport, TX)      |
|5320 |Detroit Metro Airport (Detroit, MI)                                         |
|5340 |Honolulu Enrollment Center (Honolulu, HI)                                   |
|5360 |Las Vegas Enrollment Center (Las Vegas, NV)                                 |
|5380 |Orlando International Airport (Orlando, FL)                                 |
|5400 |San Juan Global Entry Enrollment Center (Carolina, PR)                      |
|5420 |Seatac International Airport Global Entry EC (Seattle, WA)                  |
|5441 |Boston-Logan Global Entry Enrollment Center (East Boston, MA)               |
|5443 |Fort Lauderdale Global Entry Enrollment Center (Ft Lauderdale, FL)          |
|5444 |Newark Liberty Intl Airport (Newark, NJ)                                   |
|5445 |Philadelphia International Airport (Philadelphia, PA)                       |
|5446 |San Francisco Global Entry Enrollment Center (San Francisco, CA)            |
|5447 |Sanford Global Entry Enrollment Center (Sanford, FL)                        |
|5460 |San Luis Enrollment Center (San Luis, AZ)                                   |
|5500 |Calais Enrollment Center (Calais, ME)                                       |
|5520 |Lansdowne, ON  (Lansdowne, ON)                                              |
|6480 |U.s. Custom House - Bowling Green (New York, NY)                            |
|6840 |Minneapolis - St. Paul Global Entry EC (St. Paul, MN)                       |
|6920 |Doha International Airport (Doha)                                         |
|6940 |Denver International Airport (Denver, CO)                                   |
|7160 |Phoenix Sky Harbor Global Entry Enrollment Center (Phoenix, AZ)             |
|7480 |Houston Hobby Airport Enrollment Center (Houston, TX)                       |
|7520 |San Antonio International Airport (San Antonio, TX)                         |
|7540 |Anchorage Enrollment Center (Anchorage, AK)                                |
|7600 |Salt Lake City International Airport (Salt Lake City, UT)                   |
|7680 |Cincinnati Enrollment Center (Erlanger, KY)                                 |
|7740 |Milwaukee Enrollment Center (Milwaukee, WI)                                 |
|7820 |Austin-Bergstrom International Airport (Austin, TX)                         |
|7940 |Balt/Wash Intl Thurgood Marshall Airport (Linthicum, MD)                    |
|7960 |Portland, OR Enrollment Center (Portland, OR)                               |
|8020 |Tampa Enrollment Center (Tampa, FL)                                         |
|8040 |Albuquerque Enrollment Center (Albuquerque, NM)                             |
|8100 |Douglas Enrollment Center (Douglas, AZ)                                     |
|8120 |Washington, DC Enrollment Center (Washington, DC)                           |
|8920 |Los Angeles -Long Beach Seaport  (Long Beach, CA)                           |
|9040 |Singapore (Singapore, U.S. Embassy)  (Singapore)                            |
|9101 |Grand Portage (Grand Portage, MN)                                           |
|9140 |Guam International Airport (Tamuning, GU)                                   |
|9180 |Cleveland U.S. Customs and border protection (Middleburg Heights, OH)       |
|9200 |Pittsburgh International Airport (Pittsburgh, PA)                           |
|9240 |Tucson Enrollment Center (Tucson, AZ)                                       |
|9260 |West Palm Beach Enrollment Center (Riviera Beach, FL)                       |
|9300 |Warwick, RI Enrollment Center (Warwick, RI)                                 |
|9740 |New Orleans Enrollment Center (Kenner, LA)                                  |
|10260|Nashville Enrollment Center (Nashville, TN)                                 |
|11000|Moline Quad Cities International Airport (Moline, IL)                       |
|11001|Rockford-Chicago International Airport (Rockford, IL)                       |
|11002|Peoria international airport (Peoria, IL)                                   |
|11841|Port Clinton, Ohio Enrollment Center (Port Clinton, OH)                     |
|11981|Chicago Field Office Enrollment Center (Chicago, IL)                        |
|12021|St. Louis Enrollment Center (St. Louis, MO)                                 |
|12161|Boise Enrollment Center (Boise, ID)                                         |
|12781|Kansas City Enrollment Center (Kansas City, MO)                             |
|13321|Blaine Global Entry Enrollment Center (Blaine, WA)                          |
|13621|Memphis Intl Airport Global Enrollment Center (Memphis, TN)                 |
|14181|International Falls Global Entry Enrollment Center (International Falls, MN)|
|14321|Charlotte-Douglas International Airport (Charlotte, NC)                     |
|14381|Fairbanks Enrollment Center (Fairbanks, AK)                                 |
|14481|Gulfport-Biloxi Global Entry Enrollment Center (Gulfport, MS)               |
|14681|Bradley International Airport Enrollment Center (Windsor Locks, CT)         |
|14981|Richmond, VA Enrollment Center (Richmond, VA)                               |
|15221|Pembina Global Entry Enrollment Center (Pembina, ND)                        |
|16226|Eagle Pass  (Eagle Pass, TX)                                                |
|16242|Dayton Enrollment Center (Vandalia, OH)                                     |
|16248|Treasure Coast International Airport (Fort Pierce, FL)                      |
|16251|Sweetgrass Global Entry Enrollment Center (Sweetgrass, MT)                  |
|16271|Tri-cities Enrollment Center (Blountville, TN)                              |
|16277|Huntsville Global Entry Enrollment Center (Huntsville, AL)                  |
|16278|South Bend Enrollment Center (South Bend, IN)                               |
|16280|Grand Forks, ND enrollment Center (Grand Forks, ND)                         |
|16282|Mobile Regional Airport Enrollment Center (Mobile, AL)                      |
|16290|BUFFO - Albany International Airport (Albany, NY)                           |
|16460|Del Rio Port of Entry, TX 2302 (Del Rio, TX)                               |
|16461|Des Moines GE Enrollment Center (Des Moines, IA)                            |
|16463|Springfield – Branson National Airport, MO (Springfield, MO)                |
|16467|Omaha, NE Enrollment Center (Omaha, NE)                                     |
|16475|SEAFO - Bozeman Airport (Belgrade, MT)                                      |
|16476|SEAFO - FARGO Global Entry Workshop (Fargo, ND)                             |
|16482|Grand Forks, ND Enrollment Event (Grand Forks, ND)                          |
|16485|SEAFO - Billings-Logan Airport GE Mobile Event (Billings, MT)               |
|16488|SEAFO - Missoula International Airport (Missoula, MT)                       |
