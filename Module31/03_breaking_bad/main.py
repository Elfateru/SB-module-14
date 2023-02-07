import requests
import json
from pprint import pprint

try:
    my_req = requests.get('https://swapi.dev/api/starships/10')
    if my_req.status_code == 200:
        data_text = json.loads(my_req.text)
        ship_keys = ['name', 'max_atmosphering_speed', 'starship_class', 'pilots']
        pilot_keys = ['height', 'homeworld', 'mass', 'name']
        data = dict()
        pilots_list = []
        for key, val in data_text.items():
            if key in ship_keys:
                if key == 'pilots':
                    for link_pilot in data_text['pilots']:
                        pilot = requests.get(link_pilot)
                        pilot_text = json.loads(pilot.text)
                        pi = pilot_text.copy()
                        for key_p, val_p in pilot_text.items():
                            if key_p not in pilot_keys:
                                pi.pop(key_p)
                            if key_p == 'homeworld':
                                pi['homeworld_url'] = val_p
                                planet_req = requests.get(val_p)
                                planet_text = json.loads(planet_req.text)
                                pi['homeworld'] = planet_text['name']
                        pilots_list.append(pi)
                    data['pilots'] = pilots_list
                else:
                    data[key] = val
        with open('Millennium Falcon.json', 'w') as file:
            json.dump(data, file, indent=4)
            pprint(data)
    else:
        print(my_req)
except Exception as exc:
    print(exc)
