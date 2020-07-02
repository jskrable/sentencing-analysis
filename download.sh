#!/usr/bin/env sh
# coding: utf-8

mkdir temp
mkdir data
mkdir data/2019
curl https://www.ussc.gov/sites/default/files/zip/opafy19nid.zip > temp/2019.zip
unzip 2019.zip -d data/2019/
rm -rf temp/