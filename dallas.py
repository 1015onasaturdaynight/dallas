# python3 -m pip install pandas
# python3 -m pip install sodapy

import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from sodapy import Socrata

client = Socrata("www.dallasopendata.com", None)

# valid columns:
# ===============
# service_request_number
# address
# city_council_district
# department
# service_request_type
# ert_estimated_response_time
# overall_service_request_due_date
# status
# created_date
# update_date
# closed_date
# outcome
# priority
# method_received_description
# unique_key
# lat_location

dt = (datetime.today() + relativedelta(days = -30)).strftime("%Y-%m-%d")

results = client.get("d7e7-envw", "?$query=select "
                                  "service_request_number, "
                                  "address, "
                                  "service_request_type, "
                                  "method_received_description, "
                                  "status, "
                                  "created_date, "
                                  "closed_date, "
                                  "outcome "
                                  "where created_date > '{}' "
                                  "order by created_date desc limit 100000".format(dt))

df = pd.DataFrame(results)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

print(df)
