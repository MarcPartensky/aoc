#!/bin/sh

for date in */*
do
    echo $date: `cat $date/input | python $date`
done
