#!/usr/bin/env python
# -*-coding:utf-8 -*-
import difflib


def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()


print (string_similar('http://ttt.vul.com?p=12', 'http://ttt.vul.com?p=33'))