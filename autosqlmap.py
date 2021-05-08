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
    os.system('python3 sqlmap/sqlmap.py -m get_url.txt  --results-file=GET.csv --output-dir=/home/iot/Desktop/spider_sqlmap/sqlmap_result')
def sqlmap_post_batch():
    os.system('python3 sqlmap/sqlmap.py -m post_url.txt --forms  --results-file=POST.csv --output-dir=/home/iot/Desktop/spider_sqlmap/sqlmap_result')

def test():
    print(2222)

#sqlmap_post_batch()







