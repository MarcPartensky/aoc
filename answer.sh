#!/bin/sh

echo \# Answers
for year in */
do
    year=`basename $year`
    echo \#\# $year
    for day in $year/*/
    do
        day=`basename $day`
        echo - "[$day](https://adventofcode.com/$year/$day)": **`cat $year/$day/input | python $year/$day`**
    done
done
