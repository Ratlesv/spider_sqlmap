#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os

def call_sqlmap():
    #Read the file
    with open("get_url.txt", "r") as f:
        for line in f:
            test_url = line

    os.system('python3 sqlmap/sqlmap.py --url %s ==randon-agent --batch'%test_url)
def sqlmap_batch():
    os.system('python3 sqlmap/sqlmap.py -m get_url.txt  --results-file=1.csv ')
def sqlmap_post_batch():
    os.system('python3 sqlmap/sqlmap.py -m post_url.txt --forms  --results-file=2.csv')

def test():
    print(2222)

#sqlmap_post_batch()







