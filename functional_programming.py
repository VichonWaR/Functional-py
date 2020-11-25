# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 01:10:59 2020

@author: vichon
"""

# funtional programming - fundis
import collections

scientist = collections.namedtuple('scientist',[
    'name',
    'field',
    'born',
    'nobel'] ) 

Scientist = (
    scientist(name="Ada Lovelace", field="math", born=1815, nobel=False),
    scientist(name="Albert Einstine", field="Physics", born=1879, nobel=True),
    scientist(name="Emmy Noether", field="math", born=1882, nobel=False),
    scientist(name="Tu Youyou",field="Chemistyr", born=1930, nobel=True),
    scientist(name="Ada Youath", field="Chemistry", born=1939, nobel=True),
    scientist(name="Vera Rubin", field="Astronomy", born=1928, nobel=False),
    scientist(name="Sally Ride", field="Physics", born=1951, nobel=False),
    scientist(name="Marie Curie", field="Physics", born=1867, nobel=True),
    )




for i in Scientist:
    print(f"{i.name} was a sceintist born in {i.born}, in the field of {i.field}")
    if i.nobel == 1:
        print("they won a nobel prize")
    else:
        print("they did not win a nobel prize")


        

