#!/usr/bin/env python3
"Script that takes jpeg images from supplier-data/images directory and uploads
them to web server fruit catalog."
import os, requests

url = 'http://localhost/upload/'
im_dir = '~/supplier-data/images'
files = os.listdir(im_dir)  # Get list of files from directory

# Edit to loop through jpeg files in supplier-data/images directory
# TODO: Add conditional to check file is jpeg before uploading
for file in files:
    filepath = "{}/{}".format(im_dir, file)
    with open(filepath, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
