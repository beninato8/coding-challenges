#!/usr/bin/env python3

'''
Implement and algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
'''

def is_unique(string): # O(n)
    s = set()
    for c in string: # go through characters
        if c in s: # if character already seen
            return False # duplicate character
        s.add(c) # add unseen character to set
    return True

def is_unique_1(string): # O(n^2), no additional data structures
    for i, c1 in enumerate(string):
        for j, c2 in enumerate(string):
            if i != j and c1 == c2:
                return False
    return True