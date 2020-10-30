#!/usr/bin/env python3

'''
Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold additional characters,
and that you are given the "true" length of the string.
'''

import re

def urlify(string): # O(n)
    return string.replace(' ', '%20')

def urlify_1(string): # O(n)
    return re.sub(' ', '%20', string)

def urlify_2(string): # O(n)
    string = list(string)
    out = [''] * (len(string) + 2 * string.count(' '))
    i = 0
    for c in string:
        if c != ' ':
            out[i] = c
        else:
            out[i] = '%'
            out[i+1] = '2'
            out[i+2] = '0'
            i += 2
        i += 1
    return ''.join(out)