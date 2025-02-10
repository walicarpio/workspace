// variables
let numeroSecreto = 6;
let numeroUsuario;
let intentos = 1;
let palabraVeces = 'vez';

// Loop o bucle. Mientras las variables sean distintas, se repite x intentos
while (numeroUsuario != numeroSecreto){
    numeroUsuario = prompt ("Ingresa un número entre 1 y 10, por favor");

    if (numeroUsuario == numeroSecreto){
        alert (`Felicitaciones, has ganado. El número secreto es ${numeroSecreto}. Lo hiciste en ${intentos} ${palabraVeces}`);
    } else {
        if (numeroUsuario > numeroSecreto){
            alert ("El numero secreto es menor");
        } else {
            alert ("El numero secreto es mayor");
        }
    }
    intentos = intentos + 1;
    palabraVeces = 'veces';
}
