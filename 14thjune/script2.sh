#!/bin/bash


# initlisation of associative array with the name as Capitals

declare -A capitals

# filling up the A array

capitals[India]="New Delhi"
capitals[France]="Paris"
capital[Japan]="Tokyo"

# print the elements by key

echo "Capital of France: ${capitals[France]}"

# number of elements:

echo "Total countries: ${#capitals[@]}"
