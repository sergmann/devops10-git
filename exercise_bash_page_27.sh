#!/bin/bash
clear
ARG1=$1
ARG2=$2
echo $ARG1
echo $ARG2
if [ "${#ARG1}" -gt 3 ] || [ "${#ARG2}" -gt 3 ]
     then
     echo "they are good"
  else
     echo "ARG1 and ARG2 less then 3"
     exit 1
fi
if [ "$ARG1" != "$ARG2" ]
      then
      echo "ARG1 not equal ARG2"
  else
      echo "ARG1 equal ARG2"
fi
