#!/bin/bash

if [ -f temp ]; then
  rm temp;
fi
for file in `find . -name "*.svg"`; do
  filename=`basename $file`;
  name="${filename%.*}";
  echo `echo $name | tr -d "-"` $file >> temp
done
cat temp | sort > sorted
./printEnum.py
