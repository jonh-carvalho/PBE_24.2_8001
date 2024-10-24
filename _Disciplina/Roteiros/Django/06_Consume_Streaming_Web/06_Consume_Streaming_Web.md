Para criar um aplicativo **HTML/JavaScript** que consome o endpoint `contents` da API Django REST, podemos usar **fetch API** para fazer as requisições. Vou fornecer uma estrutura básica com um exemplo funcional que faz as operações de **GET** para listar o conteúdo e **POST** para criar um novo conteúdo.

### Passos:

1. **Estrutura HTML**: Vamos criar um formulário para adicionar novo conteúdo e uma tabela para listar os conteúdos.
2. **JavaScript**: Funções para realizar as requisições HTTP utilizando `fetch`.
3. **CSS**: Estilização básica para tornar a interface mais atraente.

---

### 1. **Criação do arquivo HTML/JavaScript**

#### Arquivo: `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>App de Conteúdo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
        .content-list {
            margin-top: 20px;
        }
        .content-list table {
            width: 100%;
            border-collapse: collapse;
        }
        .content-list th, .content-list td {
            border: 1px solid #ccc;
            padding: 10px;
            text-align: left;
        }
        .form-section {
            margin-bottom: 20px;
        }
        .form-section input, .form-section button {
            padding: 10px;
            margin-right: 10px;
        }
    </style>
</head>
<body>

    <h1>Conteúdos Disponíveis</h1>

    <!-- Formulário para adicionar conteúdo -->
    <div class="form-section">
        <h2>Adicionar Novo Conteúdo</h2>
        <form id="contentForm">
            <input type="text" id="title" placeholder="Título" required>
            <input type="text" id="description" placeholder="Descrição" required>
            <input type="url" id="file_url" placeholder="URL do arquivo" required>
            <input type="url" id="thumbnail_url" placeholder="URL da miniatura" required>
            <select id="content_type">
                <option value="video">Vídeo</option>
                <option value="audio">Áudio</option>
            </select>
            <label for="is_public">Público?</label>
            <input type="checkbox" id="is_public" checked>
            <button type="submit">Adicionar Conteúdo</button>
        </form>
    </div>

    <!-- Listagem de conteúdos -->
    <div class="content-list">
        <h2>Lista de Conteúdos</h2>
        <table id="contentTable">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Título</th>
                    <th>Descrição</th>
                    <th>Tipo</th>
                    <th>Público</th>
                </tr>
            </thead>
            <tbody>
                <!-- Conteúdos serão inseridos aqui -->
            </tbody>
        </table>
    </div>

    <script>
        const apiUrl = 'http://127.0.0.1:8000/api/contents/';

        // Função para obter e listar conteúdos
        async function fetchContents() {
            try {
                const response = await fetch(apiUrl);
                const data = await response.json();
                const contentTable = document.querySelector('#contentTable tbody');
                contentTable.innerHTML = '';

                data.forEach(content => {
                    const row = `
                        <tr>
                            <td>${content.id}</td>
                            <td>${content.title}</td>
                            <td>${content.description}</td>
                            <td>${content.content_type}</td>
                            <td>${content.is_public ? 'Sim' : 'Não'}</td>
                        </tr>
                    `;
                    contentTable.innerHTML += row;
                });
            } catch (error) {
                console.error('Erro ao buscar conteúdos:', error);
            }
        }

        // Função para adicionar novo conteúdo
        async function addContent(event) {
            event.preventDefault();

            const title = document.getElementById('title').value;
            const description = document.getElementById('description').value;
            const file_url = document.getElementById('file_url').value;
            const thumbnail_url = document.getElementById('thumbnail_url').value;
            const content_type = document.getElementById('content_type').value;
            const is_public = document.getElementById('is_public').checked;

            const contentData = {
                title,
                description,
                file_url,
                thumbnail_url,
                content_type,
                is_public
            };

            try {
                const response = await fetch(apiUrl, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(contentData)
                });

                if (response.ok) {
                    alert('Conteúdo adicionado com sucesso!');
                    fetchContents(); // Atualiza a lista de conteúdos
                    document.getElementById('contentForm').reset(); // Limpa o formulário
                } else {
                    alert('Erro ao adicionar conteúdo');
                }
            } catch (error) {
                console.error('Erro ao adicionar conteúdo:', error);
            }
        }

        // Inicializar a página carregando os conteúdos
        document.addEventListener('DOMContentLoaded', fetchContents);

        // Evento de envio do formulário
        document.getElementById('contentForm').addEventListener('submit', addContent);

    </script>

</body>
</html>
```

---

### Explicação do Código

1. **HTML Estrutura:**
   - Um formulário na seção `form-section` permite adicionar um novo conteúdo, com campos para **título**, **descrição**, **URL do arquivo**, **URL da miniatura**, **tipo de conteúdo** (vídeo ou áudio), e um checkbox para indicar se é **público**.
   - Uma tabela na seção `content-list` lista os conteúdos que são retornados da API.

2. **JavaScript:**
   - A função `fetchContents()` faz uma requisição **GET** para o endpoint `contents` e preenche a tabela com os dados.
   - A função `addContent()` faz uma requisição **POST** para o mesmo endpoint, criando um novo conteúdo com base nos dados fornecidos pelo usuário no formulário.
   - A função `fetchContents()` é chamada no evento `DOMContentLoaded` para listar os conteúdos assim que a página é carregada.
   - O evento de **submit** do formulário é tratado por `addContent()` para enviar o conteúdo à API.

3. **CSS:** 
   - O CSS básico estiliza o layout da página, a tabela e o formulário, mantendo a interface limpa e funcional.

---

### Como Testar o Aplicativo

1. **Rodar a API Django:**
   Certifique-se de que a API Django REST está rodando localmente, acessível em `http://127.0.0.1:8000/api/contents/`.

2. **Servir o Arquivo HTML:**
   Salve o arquivo como `index.html` e abra no navegador.

3. **Testando as Funções:**
   - Você pode adicionar conteúdos pelo formulário e, ao fazer isso, a tabela será atualizada automaticamente com o novo conteúdo.
   - Todos os conteúdos da API serão listados na tabela assim que a página for carregada.

---

Dessa forma, você terá um app front-end em HTML e JavaScript que consome a API Django REST e permite listar e adicionar conteúdos facilmente.