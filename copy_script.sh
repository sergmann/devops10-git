#!/bin/bash

for file in `ls *.txt`
do
    newfile=`echo $file|sed 's/.txt/.doc/'`
    newfile= mv $file $newfile
done 
