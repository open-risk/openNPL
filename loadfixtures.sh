#!/bin/bash

NAME[1]="synthetic_data_1"

source venv/bin/activate
for i in ${NAME[@]}
do
python3 manage.py loaddata --format=json ./npl_portfolio/fixtures/$i.json
done
