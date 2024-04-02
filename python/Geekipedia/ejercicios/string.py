mensaje="Hola"
mensaje+=" "
mensaje+="Eduardo"
print(mensaje)

mensaje="Hola"
espacio=" "
nombre="Eduardo"
print("Concatenación: ", mensaje+espacio+nombre)

numero_uno=4
numero_dos=6
resultado=numero_uno+numero_dos
resultado=str(resultado)
print("El resultado de la suma es: "+resultado)

print("Búsqueda:")
mensaje="Hola Ernesto"
buscar_subcadena=mensaje.find("Ernesto")
print(buscar_subcadena)

print("Extraer:")
mensaje="Hola Ernesto"
extraer_subcadena=mensaje[1:8]
print(extraer_subcadena)

## Comparación de caracteres que NO coinciden da como resultado respuesta FALSE
mensaje_uno="Hola"
mensaje_dos="Eduardo"
print ("La comparación entre "+mensaje_uno, "y "+mensaje_dos, "es:", mensaje_uno==mensaje_dos)

## Comparación de caracteres que coinciden da como resultado respuesta TRUE
mensaje_uno="Hola"
mensaje_dos="Hola"
print ("La comparación entre "+mensaje_uno, "y "+mensaje_dos, "es:", mensaje_uno==mensaje_dos)
