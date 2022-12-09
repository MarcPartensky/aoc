#!/bin/sh

echo \# Answers
for year in */
do
    year=`basename $year`
    echo \#\# $year
    for day in $year/*/
    do
        day=`basename $day`
        number=`echo $day | cut --characters=4-`
        echo - "[$day](https://adventofcode.com/$year/day/$number)": **`cat $year/$day/input | python $year/$day`**
    done
done
