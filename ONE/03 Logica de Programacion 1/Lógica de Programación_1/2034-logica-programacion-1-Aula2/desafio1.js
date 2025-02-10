/* Mi propuesta para el ejercicio:

let introDia = prompt("¿Qué dia de la semana es?");

let diaSabado = "sabado";
let diaDomingo = "domingo";

if (introDia == diaSabado) {
  alert("Buen fin de semana");
}
if (introDia == diaDomingo) {
    alert("Buen fin de semana");
} else {
  alert("¡Buena semana");
}
*/

//Abajo, la respuesta correcta. Elegancia en el lenguaje, menos es mas:

let diaDeLaSemana = prompt('¿Qué día de la semana es?');
if (diaDeLaSemana === 'Sábado' || diaDeLaSemana === 'Domingo') {
    alert('¡Buen fin de semana!');
} else {
    alert('¡Buena semana!');
}