#!/usr/bin/python

import random
import os
import json

count = os.getenv("FILE_COUNT") or 100
words = [word.strip() for word in open('../sample.txt').readlines()]

for identifier in range(1, count + 1):
    amount = random.uniform(1.0, 1000.0)
    content = {
            # pick one of the item form given file
            'topic': random.choice(words),
            'value': "%.2f" % amount
    }
    with open('./new/receipt-%s.json' % identifier, 'w') as f:
        json.dump(content, f)
