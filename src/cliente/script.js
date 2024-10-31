const apiUrl = "http://127.0.0.1:8000/api/contents/";

// Função para obter e listar conteúdos
async function fetchContents() {
  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    const contentTable = document.querySelector("#contentTable tbody");
    contentTable.innerHTML = "";

    data.forEach((content) => {
      const row = `
                        <tr>
                            <td>${content.id}</td>
                            <td>${content.title}</td>
                            <td>${content.description}</td>
                            <td>${content.content_type}</td>
                            <td>${content.is_public ? "Sim" : "Não"}</td>
                            <td>${content.creator}</td>
                        </tr>
                    `;
      contentTable.innerHTML += row;
    });
  } catch (error) {
    console.error("Erro ao buscar conteúdos:", error);
  }
}

// Função para adicionar novo conteúdo
async function addContent(event) {
  event.preventDefault();

  const titleElement = document.getElementById("title");
  const descriptionElement = document.getElementById("description");
  const fileUrlElement = document.getElementById("file_url");
  const thumbnailUrlElement = document.getElementById("thumbnail_url");
  const contentTypeElement = document.getElementById("content_type");
  const isPublicElement = document.getElementById("is_public");
  const creatorElement = document.getElementById("creator");

  if (!titleElement || !descriptionElement || !fileUrlElement || !thumbnailUrlElement || !contentTypeElement || !isPublicElement || !creatorElement) {
    alert("Erro: Um ou mais elementos do formulário não foram encontrados.");
    return;
  }

  const title = titleElement.value;
  const description = descriptionElement.value;
  const file_url = fileUrlElement.value;
  const thumbnail_url = thumbnailUrlElement.value;
  const content_type = contentTypeElement.value;
  const is_public = isPublicElement.checked;
  const creator = creatorElement.value;

  const contentData = {
    title,
    description,
    file_url,
    thumbnail_url,
    content_type,
    is_public,
    creator
  };

  try {
    const response = await fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(contentData),
    });

    if (response.ok) {
      alert("Conteúdo adicionado com sucesso!");
      fetchContents(); // Atualiza a lista de conteúdos
      document.getElementById("contentForm").reset(); // Limpa o formulário
    } else {
      const errorData = await response.json();
      alert(`Erro ao adicionar conteúdo 1: ${errorData.message || response.statusText}`);
    }
  } catch (error) {
    console.error("Erro ao adicionar conteúdo 2:", error);
  }
}

// Inicializar a página carregando os conteúdos
document.addEventListener("DOMContentLoaded", fetchContents);

// Evento de envio do formulário
document.getElementById("contentForm").addEventListener("submit", addContent);