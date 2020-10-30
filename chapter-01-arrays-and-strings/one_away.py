#!/usr/bin/env python3

'''
There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character.
Given two strings, write a function to check if they are less than two edits away
'''

def one_away(s1, s2): # O(n)
    if s1 == s2 or (len(s1) < 2 and len(s2) < 2): # same string or both are length 0 or 1
        return True
    if abs(len(s1) - len(s2)) > 1: # difference in lengths is greater than 1
        return False
    for i in range(min(len(s1), len(s2))):
        if s1[i] != s2[i]:
            if len(s1) == len(s2): # replaced char
                return s1[i+1:] == s2[i+1:]
            elif len(s1) < len(s2): # added a char to s1
                return s1[i+1:] == s2[i+2:]
            else: # if len(s2) < len(s1): # removed a char from s1
                return s1[i+2:] == s2[i+1:]
    return True # character added to end