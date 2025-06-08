#!/bin/bash

a=10
b=20

echo "a = $a, b = $b"

# -eq: Equal
if [ $a -eq $b ]; then
  echo "a is equal to b"
else
  echo "a is NOT equal to b"
fi

# -ne: Not Equal
if [ $a -ne $b ]; then
  echo "a is NOT equal to b"
else
  echo "a is equal to b"
fi

# -gt: Greater Than
if [ $a -gt $b ]; then
  echo "a is greater than b"
else
  echo "a is NOT greater than b"
fi

# -lt: Less Than
if [ $a -lt $b ]; then
  echo "a is less than b"
else
  echo "a is NOT less than b"
fi

# -ge: Greater Than or Equal To
if [ $a -ge $b ]; then
  echo "a is greater than or equal to b"
else
  echo "a is LESS than b"
fi

# -le: Less Than or Equal To
if [ $a -le $b ]; then
  echo "a is less than or equal to b"
else
  echo "a is GREATER than b"
fi
