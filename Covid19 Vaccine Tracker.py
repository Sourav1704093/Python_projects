import requests
from datetime import date, datetime,timedelta
import time
import json

from requests.models import Response

print("Starting search for Covid vaccine slots!!")

age = 50
pinCodes = ["462003"]
print_flag = "Y"
num_days = 3

actual = datetime.today()

list_format = [actual +timedelta(days = i) for i in range(num_days)]

actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]

while True:
    counter = 0
    
    for pinCode in pinCodes:
        for given_date in actual_dates:
            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pinCode,given_date)

            header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
            
            result = requests.get(URL,headers=header)

            if result.ok:
                response_json = result.json()
                
                flag = False
                if response_json["centers"]:
                    if(print_flag.lower() == 'y'):
                        for center in response_json["centers"]:
                            for session in center["sessions"]:
                                if(session["min_age_limit"]<= age and session["available_capacity"]>0):
                                    print('Pincode:  '+ pinCode)
                                    print("available on : {}".format(given_date))
                                    print("\t",center["name"])
                                    print("\t",center["block_name"])
                                    print("\t Price: ",center["fee_type"])
                                    print("\t Availability : ",session["available_capacity"])
                                    
                                    if(session["vaccine"]!= ''):
                                        print("\t Vaccine type: ",session["vaccine"])
                                    print("\n")
                                    
                                    counter = counter+1
                                else:
                                    pass 
                else:
                    pass
            else:
                print("NO response")
    if counter == 0:
        print("No vaccination slot available!")
    else:
        print("Seach completed")
    
    dt = datetime.now() + timedelta(minutes=3)
    while datetime.now() < dt:
        time.sleep(1)
                
