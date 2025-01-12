#!/bin/sh -e

# create FlatGeobuf version of Block Groups File
ogr2ogr -nlt MULTIPOLYGON tl_2022_us_bg.fgb tl_2022_us_bg.parquet
