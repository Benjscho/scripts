#!/bin/bash

ffmpeg -y -i "$1" -vf scale=1000:-1 "$1"
