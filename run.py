#!/usr/bin/env python3
"Script to process text files (001.txt, 003.txt, ...) from
supplier-data/descriptions directory. Turns data into JSON dictionary by adding
all required fields, including image associated with fruit (image_name), and
uploading it to http://[linux-instance-external-IP]/fruits using Python
requests library."
import os
import requests
import re

# Iterate over all fruits and use post method from Python requests library
#to upload all data to URL
path = 'supplier-data/descriptions/'
files = os.listdir(path)

for file in files:
    # Initialize empty dictionary
    descriptions = {
            'name': '',
            'weight': '',
            'description': '',
            'image_name': '',
            }

    # Check for .txt format before continuing
    if os.path.splitext(file)[1] != '.txt':
        continue

    # Open file and add lines of file to dictionary keys
    with open(path + file) as fp:
        for i, line in enumerate(fp):
            if i == 0:
                descriptions['name'] = line.rstrip('\n')
            elif i == 1:
                # Get int value from line
                weight = int(re.search(r'\d+', line)[0])
                descriptions['weight'] = weight
            else:
                descriptions['description'] += line.rstrip('\n')

    # Add image name to dictionary
    descriptions['image_name'] = os.path.splitext(file)[0] + '.jpeg'

    # Upload dictionary to URL
    response = requests.post('http://<IP>/fruits', json=descriptions)
    print(response.status_code) # Check status_code for error message
