#!/bin/bash

# creating an array

fruits=("apple","mango","cherry")

# access elements in fruits-array

echo "First Fruit: ${fruits[0]}"

# loop through an array

for fruit in "${fruits[@]}"; do
	echo "Fruit: $fruit"
done

# length of array

echo "length of array: ${#fruits[@]}"


# modify the Elements in array
# array is starting with index position 0
x
fruits[3]="Mango"
fruits[1]="Grape"

