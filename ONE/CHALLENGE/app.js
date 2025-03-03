// El principal objetivo de este desafío es fortalecer tus habilidades en lógica de programación.
// Aquí deberás desarrollar la lógica para resolver el problema.
let listaAmigos = [];
const inputAmigo = document.getElementById("amigo");
const ulListaAmigos = document.getElementById("listaAmigos");
const resultado = document.getElementById("resultado");

function agregarAmigo() {
  if (inputAmigo.value === "") {
    alert("Por favor, ingresa un nombre. El nombre debe contener solo letras y espacios");
    return;
  }

  listaAmigos.push(inputAmigo.value);
  ulListaAmigos.innerHTML += `<li>${inputAmigo.value}</li>`;
  inputAmigo.value = "";
}

function sortearAmigo() {
  const sorteo = Math.floor(Math.random() * listaAmigos.length);
  const amigoSecreto = listaAmigos[sorteo];
  resultado.innerHTML = `El amigo secreto es: ${amigoSecreto}`;
  return;
}
