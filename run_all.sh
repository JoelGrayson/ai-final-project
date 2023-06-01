#!/bin/bash

echo Preprocessing FIPS
(
    cd preprocessing/src/fips || exit 65
    python3 -B main.py
)


echo Preprocessing data
(
    cd preprocessing || exit 65
    python3 -B main.py
)


echo Running AI model
python3 -B main.py


echo Making map
