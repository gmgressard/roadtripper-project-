"""seeding database NP_data of hikes"""

import os
import json
import crud, model, server 

import csv

os.system('dropdb hikes')
os.system('createdb hikes')

model.connect_to_db(server.app)
model.db.create_all()


with open('NP_data.csv', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        hike_name = row['name']
        national_park = row['area_name']
        city = row['city_name']
        state = row['state_name']
        length = row['length']
        difficulty_rating = row['difficulty_rating']
        avg_rating = row['avg_rating']
        coordinates = row['_geoloc']
