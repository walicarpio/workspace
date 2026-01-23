#!/bin/bash
# Este es un comentario a mi primer script
echo "Hola, este es mi primer script en Bash"
date
echo "Tu directorio es: $(pwd)"
name="Eduardo"
echo "Hola $name"

# Ejemplo de operación aritmética 1
a=5
b=3
let sum=a+b
echo "La suma es $sum"

#La misma operación pero mas moderna
sum2=$((a+b))
echo "La suma2 es $sum2"
