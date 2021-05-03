#!/usr/bin/env python
# -*-coding:utf-8 -*-
import re
import os
import sys
import difflib

re_get = re.compile("GET")
re_post = re.compile("POST")



def save_get_url(get_url_file,target):
	with open(get_url_file,"a") as f:
        	f.write(target)

def save_post_url(post_url_file,target):
	with open(post_url_file,"a") as f:
        	f.write(target)

def classify():
    os.system('rm -rf get_url.txt')
    os.system('rm -rf post_url.txt')
    for line in open("target.txt"):
        if "GET" in line and "?" in line:
            target_get = re.sub('\(GET\)','',line,1)
            save_get_url("get_url.txt", target_get)

            '''if "?" in line:
                for line2 in open("target.txt"):
                    if "GET" in line:
                        if "?" in line:
                            if len(line) == len(line2):
                                compare = difflib.SequenceMatcher(None, line, line2).quick_ratio()
                                if compare < 0.9:
                                    target_get = re.sub('\(GET\)','',line,1)
                                    save_get_url("get_url.txt",target_get)
                                else:
                                    pass
                            else:
                                pass'''

        elif "POST" in line:
            target_post = re.sub('\(POST\)','',line,1)
            #target_post = re.sub('\(POST\)','',line,1)
            save_get_url("post_url.txt", target_post)

classify()


