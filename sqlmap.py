#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os

def call_sqlmap():
    #Read the file
    url = input('Enter url: ')
    sqlmap1 = os.system('sqlmap --url  {} --dbs  --randon-agent'.format(url))







