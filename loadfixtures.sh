#!/bin/bash

# List of apps to load fixtures for
# News app is not included as it is updated in production
# TODO separate out eve update (similar to news)

NAME[1]="eba_portfolio"

source venv/bin/activate
for i in ${NAME[@]}
do
python3 manage.py loaddata --format=json $i  $i/fixtures/$i.json
done

