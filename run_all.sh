#!/bin/bash

echo Preprocessing FIPS
(
    cd preprocessing/src/fips || exit 65
    python3 -B main.py
)

echo Preprocessing data
(
    cd preprocessing
    python3 -B main.py
)

# echo Running AI model

# echo Making map
