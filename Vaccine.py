import requests

print("----------VACCINE SEARCH------------")

print("To Search By Pincode: Press 1")
print("To Search By State and District: Press 2")

k=int(input("Your Input: => "))

if (k==2):
    STATE = input("Enter the State: => ")
    DISTRICT = input("Enter the District: => ")
    REQ_DATE = input("Enter the Date:(Date format: DD-MM-YYYY) => ")
    request_link = f"https://cdn-api.co-vin.in/api/v2/admin/location/states"
    header = {'User-Agent': 'Chrome/84.0.4147.105 Safari/537.36'}
    response = requests.get(request_link, headers=header)
    raw_JSON = response.json()

    for item in raw_JSON['states']:
        if (STATE == (item['state_name'])):
            STATE_ID=item['state_id']

    request_link1 = f"https://cdn-api.co-vin.in/api/v2/admin/location/districts/{STATE_ID}"
    header = {'User-Agent': 'Chrome/84.0.4147.105 Safari/537.36'}
    response1 = requests.get(request_link1, headers=header)
    raw_JSON = response1.json()

    for item in raw_JSON['districts']:
        if (DISTRICT == (item['district_name'])):
            DISTRICT_ID=item['district_id']

    request_link2 = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={DISTRICT_ID}&date={REQ_DATE}"
    response1 = requests.get(request_link2, headers=header)
    raw_JSON = response1.json()

    Total_centers = len(raw_JSON['centers'])
    print()
    print("                        *>>>>>>   VACCINE RESULTS   <<<<<<<*                                ")
    print("-------------------------------------------------------------------------------------")
    print(f"Date: {REQ_DATE} | State: {STATE}  | DISTRICT: {DISTRICT}")

    if Total_centers != 0:
        print(f"Total centers in your area is: {Total_centers}")
    else:
        print(f"Seems like there aren't any vaccination centers in your area. Kindly re-check.")

    print("------------------------------------------------------------------------------------")
    print()

elif (k==1):
    PINCODE = "0"
    while len(PINCODE) != 6:
        PINCODE = input("Enter the Pincode: ")
        if len(PINCODE) < 6:
            print(f"{PINCODE} is shorter than the actual length")
        elif len(PINCODE) > 6:
            print(f"{PINCODE} is longer than the actual length")

    REQ_DATE = input("Enter the Date:(Date format: DD-MM-YYYY) => ")

    request_link = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={PINCODE}&date={REQ_DATE}"
    header = {'User-Agent': 'Chrome/84.0.4147.105 Safari/537.36'}
    response = requests.get(request_link, headers=header)
    raw_JSON = response.json()

    Total_centers = len(raw_JSON['centers'])
    print()
    print("                        *>>>>>>   VACCINE RESULTS   <<<<<<<*                                ")
    print("-------------------------------------------------------------------------------------")
    print(f"Date: {REQ_DATE} | Pincode: {PINCODE} ")

    if Total_centers != 0:
        print(f"Total centers in your area is: {Total_centers}")
    else:
        print(f"Seems like there aren't any vaccination centers in your area. Kindly re-check.")

    print("------------------------------------------------------------------------------------")
    print()

else:
    print('Invalid Input')
    exit()

for cent in range(Total_centers):
    print()
    print(f"[{cent + 1}] Center Name:", raw_JSON['centers'][cent]['name'])
    print(f"Fee Type:",  raw_JSON['centers'][cent]['fee_type'])
    print("------------------------------------------------------------")
    print("   Date      Vaccine Type    Minimum Age    Available     Dose 1    Dose 2  ")
    print("  ------     -------------   ------------   ----------    ------    ------  ")
    this_session = raw_JSON['centers'][cent]['sessions']

    for _sess in range(len(this_session)):
        print("{0:^12} {1:^12} {2:^14} {3:^12} {4:^12} {5:^12} ".format(this_session[_sess]['date'], this_session[_sess]['vaccine'],
                                                        this_session[_sess]['min_age_limit'],this_session[_sess]['available_capacity'],
                                                        this_session[_sess]['available_capacity_dose1'],this_session[_sess]['available_capacity_dose2']))
m=input()