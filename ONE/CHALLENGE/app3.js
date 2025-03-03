let amigos = [];

function agregarAmigo() {
  const inputAmigo = document.getElementById('amigo');
  const nombreAmigo = inputAmigo.value.trim();

  if (nombre === "") {
    alert("Inserta un nombre");
    return;
  }
  if (amigos.includes(nombreAmigo)) {
    alert(`El nombre ${nombreAmigo} ya está en la lista`);
    return;
  }
  amigos.push(nombreAmigo);

  inputAmigo.value.trim = "";

  actualizarLista();
}

function actualizarLista() {
  const listaAmigos = document.getElementById(listaAmigos);

  listaAmigos.innerHTML = "";

  for (let i = 0; i < amigos.length; i++) {
    const li = document.createElement("li");
    li.textContent = amigos[i];
    listaAmigos.appendChild(li);
  }
}

function sortearAmigo() {
  if (amigos.length === 0) {
    alert("No tenemos amigos que sortear");
    return;
  }
  const indiceAleatorio = Math.floor(Math.random() * amigos.length);

  const amigoSorteado = amigos[indiceAleatorio];
  const resultado = document.getElementById("resultado");
  resultado.innerHTML = `Amigo Sorteado; <strong>${amigoSorteado}</strong>`;
}
