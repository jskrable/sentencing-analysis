#!/usr/bin/env python3
# coding: utf-8
"""
main.py
06-25-20
jack skrable

https://www.ussc.gov/research/datafiles/commission-datafiles
"""

import pandas as pd

sample = 1000

with open('data/2019/opafy19nid.sas') as f:
    sas = f.read()

columns = sas.split('\n')[25:5937]

issues = []
cols = []
for line in columns:

    if len(line) < 75:
        issues.append(line)
    else:
        col1 = [x for x in line[:25].split(' ') if x != '']
        col2 = [x for x in line[25:50].split(' ') if x != '']
        col3 = [x for x in line[50:].split(' ') if x != '']
        cols.append(col1)
        cols.append(col2)
        cols.append(col3)


def getColSpecs(col):
    split = col[-1].split('-')
    if len(split) > 1:
        width = (int(split[0])-1, int(split[1]))
    else:
        width = (int(split[0])-1, int(split[0]))
    
    label = col[0]
    return {'label':label, 'width':width}


specs = [getColSpecs(x) for x in cols[:-1]]
names = [x['label'] for x in specs]
width = [x['width'] for x in specs]
df = pd.read_fwf('./data/2019/opafy19nid.dat', header=None, names=names, nrows=sample, colspecs=width)