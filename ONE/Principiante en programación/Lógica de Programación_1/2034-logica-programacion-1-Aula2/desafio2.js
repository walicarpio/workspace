//2. Verifica si un número ingresado por el usuario es positivo o negativo. Muestra una alerta informativa.
// Mi propuesta:

/* let numero = prompt("Ingresa un numero");
if (numero >= 0){
    alert("Su numero es positivo");
    
}else{
    alert("Su numero es negativo")
}
*/

// La respuesta del Instructor:

let numero = prompt("Escribe un número positivo o negativo");
if (numero > 0) {
  alert("Número positivo");
} else if (numero < 0) {
  alert("Número negativo");
} else {
  alert("El número es cero");
}

//Me falto considerar la respuesta para número cero
