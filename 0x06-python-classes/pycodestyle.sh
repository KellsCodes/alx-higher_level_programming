#!/bin/bash
for file in /
do
    pycodestyle --first "$file"
done
