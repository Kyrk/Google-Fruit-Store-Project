#!/usr/bin/env python3
'''Script that takes jpeg images from supplier-data/images directory and uploads
them to web server fruit catalog.'''
import os, requests

url = 'http://localhost/upload/'
im_dir = 'supplier-data/images'
files = os.listdir(im_dir)  # Get list of files from directory

for file in files:
    # Check that file is .jpeg before uploading
    if os.path.splitext(file)[1] != '.jpeg':
        continue

    # Get filepath
    #filepath = "{}/{}".format(im_dir, file)
    filepath = os.path.join(im_dir, file)

    # Upload file to web server
    with open(filepath, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
