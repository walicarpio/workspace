let listaAmigos = [];

function agregarAmigo() {
  let inputAmigo = document.getElementById("amigo");
  let nombreAmigo = inputAmigo.value;

  if (!nombreAmigo) {
    // otra forma (nombreAmigo == false)
    alert("Ingresa un nombre");
    return;
  }
  amigo.push(nombreAmigo);
  inputAmigo.value = "";
  inputAmigo.focus();
  renderizarAmigos();
}

function renderizarAmigos() {
  let listaAmigos = document.getElementById("listaAmigos");
  listaAmigos.innerHTML = ""; // para que no se repita limpio la lista

  for (let i = 0; i < amigo.lengt; i++) {
    let item = document.createElement("li");
    item.textContent = amigo[i];
    listaAmigos.appendChild(item);
  }
}

function sortearAmigo() {
  if (amigo.lengt === 0) {
    alert("No ay amigos para sortear");
    return;
  }
  let amigoSorteado = Math.floor(Math.random() * amigo.length);
  let resultado = document.getElementById("resultado");
  resultado.innerHTML = `El amigo secreto es: ${amigoSorteado}`;

  let limpiarLista = document.getElementById("listaAmigos");
  limpiarLista.innerHTML = "";
}
