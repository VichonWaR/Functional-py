# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 01:10:59 2020

@author: vichon
"""

# funtional programming - fundis
import collections
import pprint


scientist = collections.namedtuple('scientist',[
    'name',
    'field',
    'born',
    'nobel',
    'sex'] ) 

Scientist = (
    scientist(name="Ada Lovelace", field="math", born=1815, nobel=False,sex="M"),
    scientist(name="Albert Einstine", field="Physics", born=1879, nobel=True,sex="M"),
    scientist(name="Emmy Noether", field="math", born=1882, nobel=False,sex="M"),
    scientist(name="Tu Youyou",field="Chemistyr", born=1930, nobel=True, sex="M"),
    scientist(name="Ada Youath", field="Chemistry", born=1939, nobel=True,sex="F"),
    scientist(name="Vera Rubin", field="Astronomy", born=1928, nobel=False,sex="F"),
    scientist(name="Sally Ride", field="Physics", born=1951, nobel=False,sex="F"),
    scientist(name="Marie Curie", field="Physics", born=1867, nobel=True,sex="F"),
    scientist(name="Jaymels", field="Computer Science", born=1989, nobel=True,sex="M"),
    
    )



for i in Scientist:
    print(f"{i.name} was a sceintist born in {i.born}, in the field of {i.field}", end=" ")
    if i.sex == "M":
        print("he ", end="")
    else:
        print("she ", end="")
    if i.nobel == 1:
        print("won a nobel prize")
    else:
        print("did not win a nobel prize")


        

