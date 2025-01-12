#!/bin/sh -e

# download blocks
files=$(curl "https://www2.census.gov/geo/tiger/TIGER2022/TABBLOCK20/" | grep --only-matching "tl_2022_[[:digit:]][[:digit:]]_tabblock20.zip" | uniq)

i=0
for f in $files
do
    i=$((i+1))
    echo "downloading: $f"
    curl "https://www2.census.gov/geo/tiger/TIGER2022/TABBLOCK20/$f" -o "./data/$f" 
    unzip "./data/$f" -d "./data"
    rm "./data/$f"
    echo "sleeping for 5 seconds"
    sleep 5
done