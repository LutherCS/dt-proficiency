#!/bin/bash

function printHello() {
  echo "Hello"
}

clear
ls -l >> output.txt
echo $1, $2
echo The name of this file is $0
echo There are $# arguments

echo `date` >> date.txt

a=5
echo "The value of a is $a"
if [ $a == 6 ]; then
  echo "A"
fi

i=1
while [ ! $i == 10 ]
do
  echo $i
  printHello
  ((i = i + 1))
done
