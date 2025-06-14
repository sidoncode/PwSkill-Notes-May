#!/bin/bash

read -p "Enter a string" input

if [[ "$input" =~ ^[A-Za-z0-9]+$ ]]; then
	echo " Valid REGEX pattern"

else
	echo "not valid REGEX pattern"
fi

