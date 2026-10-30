import requests
import json
import sys
from rich import print as printc

access_key = "b175cf5e214d218611cf3484e9fe7d3b"


response = requests.get(f"https://api.aviationstack.com/v1/flights?access_key={access_key}&limit=20&offset=0&callback=MY_CALLBACK")

o = response.json()
i=1
for flight in o['data']:
    # print("✈",json.dumps(flight, indent=2))
    flight_dept = flight['departure']
    flight_arv = flight['arrival']
    flight_aline = flight['airline']
    flight_fgt = flight['flight']
    printc(f'''

 ✈ Sl NO : [bold cyan]{i}[/bold cyan]  Flight Date : {flight['flight_date']}                                                                                                
                 Flight Status : {flight['flight_status']}           
                 Departure -                                
                    From  {flight_dept['airport']}                       
                    Scheduled Time : {flight_dept['scheduled']}             
                    Estimated Time : {flight_dept['estimated']}              Time Zone : {flight_dept['timezone']}                                    
                 Arrival -                                    
                    To {flight_arv['airport']}                 
                    Scheduled Time : {flight_arv['scheduled']}  
                    Estimated Time : {flight_arv['estimated']}              Time Zone : {flight_arv['timezone']}                                      
                 Airline Detail -                            
                    {flight_aline['name']}  | iata : {flight_aline['iata']} | icao : {flight_aline['icao']}                                           
                 Flight Details -    
                    Flight No. : {flight_fgt['number']}   
--------------------------------------------------------------------------------------------------------------------------------------

        ''')
    
    i = i+1

# ✈