function abrirModal(imagem) {
  document.querySelector(".modal").classList.add("active");
  document.querySelector("#modalTitle").innerText = imagem.getAttribute("alt");
  document.querySelector("#modalText").innerText = imagem.getAttribute("data-texto");
  document.querySelector("#modalLink").innerText = imagem.getAttribute("data-link");
  const link = imagem.getAttribute("data-link");
  const modalLinkElement = document.querySelector("#modalLink");
  modalLinkElement.innerHTML = `<a href="${link}" target="_blank">Clique aqui para acessar o site do jogo</a>`
}

function fecharModal() {
  document.querySelector(".modal").classList.remove("active");
}

window.onclick = function (event) {
  let modal = document.querySelector("#modal");
  if (event.target === modal) {
    fecharModal();
  }
};