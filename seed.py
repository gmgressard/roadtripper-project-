"""seeding database NP_data of hikes"""

import os
import json

import server
import model
import crud
import csv


os.system('dropdb hikes')
os.system('createdb hikes')

model.connect_to_db(server.app)
model.db.create_all()

hikes_in_db = []

with open('NP_data.csv', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    # reader = csv.reader(csvfile)

    hikes_in_db = []

    for row in reader: #row is a dic 
        hike_name = row['name'] #string
        national_park = row['area_name']
        city = row['city_name']
        state = row['state_name']
        length = row['length']
        difficulty_rating = row['difficulty_rating']
        avg_rating = row['avg_rating']
        coordinates = row['_geoloc']

        hike_info = crud.create_hike(hike_name=hike_name,coordinates=coordinates,state=state,city=city,national_park=national_park,length=length,difficulty_rating=difficulty_rating,avg_rating=avg_rating)
        hikes_in_db.append(hike_info)
    
    print("*" * 40)
    print(len(hikes_in_db))
    print("*" * 40)
