#!/bin/bash

NAME[1]="eba_portfolio"

source venv/bin/activate
for i in ${NAME[@]}
do
mkdir -p $i/fixtures
python3 manage.py dumpdata --format=json $i -o $i/fixtures/$i.json
done

