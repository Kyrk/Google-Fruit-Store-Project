#!/usr/bin/env python3
"""Script that processes supplier images.
Uses PIL library to update all images within /supplier-data/images directory to
following specifications:
    - Size: Change image res from 3000x2000 to 600x400
    - Format: Change format from .TIFF to .JPEG
"""
from PIL import Image
import os

im_dir = '~/supplier_data/images'

for infile in os.listdir(im_dir):
    # Check file is .TIFF
    if os.path.splitext(infile)[1] not '.tiff':
        print('not .tiff')
        continue

    #outfile = Image.open(os.path.join(im_dir, infile)) # Open image
    # Create path for file without its ext for file conversion
    outfile = os.path.join(im_dir, os.path.splitext(infile)[0])
    # Open file and perform following:
    # - Change image res from 3000x2000 to 600x400
    # - Change format from .TIFF to .JPEG
    # - Convert image mode from RGBA to RGB for compatible file converion
    try:
        with Image.open(os.path.join(im_dir, infile)) as im:
            im.convert('RGB').resize((3000,2000)).save(outfile, 'JPEG')
    except OSError:
        pass
