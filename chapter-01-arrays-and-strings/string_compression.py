#!/usr/bin/env python3

'''
Implement a method to perform basic string compression using the counts of repleated characters.
For example, the string 'aabcccccaaa' would become 'a2b1c5a3'.
If the compressed string would not become smaller than the original string,
your method should return the original string.
You can assume the string only has uppercase and lowercase letters (a-z)
'''

import re

def string_compression(string): # O(n)
    if len(string) < 3: # anything less than 3 can't be compressed smaller
        return string
    l = [m.group(0) for m in re.finditer(r'(.)\1*', string)] # split into repeated groups
    if len(l) * 2 >= len(string): # check if compression would be smaller
        return string
    return ''.join(f'{x[0]}{len(x)}' for x in l) # join and add repetion length