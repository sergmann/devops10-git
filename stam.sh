#!/bin/bash

NAME=$1
echo $NAME
shift
COUNT=$1
echo $COUNT
shift
add=$*
echo $add
addlen=$#
#echo $#
for i in $add
do
   VALUE1=10
   VALUE2=$i
   echo $VALUE2
   if [ `expr $VALUE1 + $VALUE2 > /dev/null 2>@1 ; echo $? ` -ne 0 ]
      then
     echo ""
     echo "$i is non-numeric argument"
   fi
done

