#!/binb/bash

echo Preprocessing FIPS
cd ./preprocessing/src/fips || exit 65
python3 main.py

echo Preprocessing data
cd ..
python3 main.py

# echo Running AI model

# echo Making map
