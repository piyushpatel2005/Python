#!/usr/bin/python

import glob
import os
import re
import shutil
import json
import math

try:
    os.mkdir("./processed")
except OSError:
    print("'processed' directory already exists")

# Get the list of receipts
# receipts = glob.glob('./new/receipt-[0-9]*.json')
even_receipts = [f for f in glob.iglob('./new/receipt-[0-9]*.json') if re.match('./new/receipt-[0-9]*[02468].json', f)]
subtotal = 0.0
# for path in receipts:
for path in even_receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    # name = path.split('/')[-1]
    # destination = "./processed/%s" % name
    destination = path.replace('new', 'processed')
    shutil.move(path, destination)
    print("moved '%s' to '%s'" % (path, destination))

print("Receipt subtotal: $%s" % round(subtotal, 2))
# Iterate over the receipts

    # read content and tally a subtotal
    # move file to processed directoryqqq

    # print that processed the file

# print subtotal of all processed receipts
