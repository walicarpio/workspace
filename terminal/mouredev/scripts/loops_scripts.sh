#!/bin/bash
#bucle for
for i in 1 2 3 4 5
do
	echo "Número: $i"
done
for name in *.sh
do
	echo "Archivo: $name"
done

#bucle while
count=1
while [ $count -le 5 ]
do
	echo "Contador: $count"
	((count++))
done
