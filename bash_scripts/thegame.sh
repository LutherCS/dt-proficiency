#!/bin/bash
clear
secret=$RANDOM
min=0
max=32767
counter=0
guess=-1

echo "Try to guess a secret number between $min and $max"
echo "Hint: it's $secret"
echo "What is your guess ($min..$max)"
read guess
while [ ! $guess == $secret ]
do
  if [ $secret -lt $guess ]; then
    echo "The secret is less than $guess"
    ((max=guess-1))
  else
    echo "The secret is greater than $guess"
    ((min=guess+1))
  fi
  ((counter = counter + 1))
  echo "What is your guess ($min..$max)"
  read guess
done

echo "Congratulation!"
echo "It took you $counter attempts"
