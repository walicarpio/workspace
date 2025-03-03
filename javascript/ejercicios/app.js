let numeroSecreto = Math.floor(Math.random() * 10) + 1;
let numeroUsuario = 0;
let intentos = 1;
// let palabraVeces = "vez";
let maximosIntentos = 3;

while (numeroSecreto != numeroUsuario) {
    numeroUsuario = parseInt(prompt("Me indicas un número entre 1 y 10, por favor: "));

    console.log(numeroUsuario);
    if (numeroUsuario == numeroSecreto) {
        alert(`Acertaste, el numero secreto es: ${numeroSecreto}. Lo hiciste en ${intentos} ${intentos == 1 ? "vez" : "veces"}`);
    } else {
        if (numeroUsuario > numeroSecreto) {
        alert("El numero es menor");
        } else {
        alert("El numero es mayor");
        }
    }
    intentos++;
    // palabraVeces = "veces";
    if (intentos > maximosIntentos) {
        alert(`Llegaste al número máximo de ${maximosIntentos} intentos`);
        break;
    }
    }
