#!/bin/bash

NAME[1]="eba_portfolio"

for i in ${NAME[@]}
do
python3 manage.py loaddata --format=json $i  $i/fixtures/$i.json
done

