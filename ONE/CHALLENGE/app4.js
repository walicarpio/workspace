let listaAmigos = [];
const inputAmigo = document.getElementById("amigo");
const ulListaAmigos = document.getElementById("listaAmigos");
const resultado = document.getElementById("resultado");

function agregarAmigo() {
  const nombre = inputAmigo.value.trim();

  if (nombre === "") {
    alert("Por favor, ingresa un nombre. El nombre debe contener solo letras y espacios");
    return;
  }

  listaAmigos.push(nombre);

  const li = document.createElement("li");
  li.textContent = nombre;
  ulListaAmigos.appendChild(li);
}

function sortearAmigo() {
  if (listaAmigos.length === 0) {
    alert("Debes agregar amigos a la lista antes de realizar el sorteo.");
    return;
  }

  const indiceAleatorio = Math.floor(Math.random() * listaAmigos.length);
  const amigoSecreto = listaAmigos[indiceAleatorio];
  resultado.innerHTML = `El amigo secreto es: ${amigoSecreto}`;
}