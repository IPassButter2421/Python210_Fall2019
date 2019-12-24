# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 07:48:45 2019

@author: TimLaptop
"""

import random

string_of_text = open("sherlock.txt")

string_of_text = string_of_text.readlines()

new_string = []

for _ in string_of_text:
    if _ == '\n':#remove just a plain carrage.
        pass
    else:
        new_string.append(_[:-1])

words = []
for _ in new_string:
    temp_list = _.split()
    for i in temp_list:    
        words.append(i) 

def build_trigrams(words):
        
    trigrams = {}
    
    for i in range(len(words)-2):
       pair = words[i:i + 2]
       #print("Pair: ",pair)
       value = words[i+2]
       #print("Values: ", value)
       key = tuple(pair)
     
       try: 
           trigrams[key]
           trigrams[key].append(value)
       except KeyError:
           trigrams[key] = [value]
           
    return trigrams

def build_text(tri_dict):   
    #was not able to build the text portion
    tri_dict
    
if __name__ == "__main__":
    trigrams = build_trigrams(words)