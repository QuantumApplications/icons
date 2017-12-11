#!/bin/bash

for file in `find . -name "*.svg"`; do xmlstarlet ed -N svg='http://www.w3.org/2000/svg' -d "//svg:path[1]" $file > temp; mv temp $file; done
