# Versionamento

**Git** e **GitHub** – controle de versão para iniciantes

---

**Git** e **GitHub** são duas tecnologias que todo desenvolvedor deve aprender, independentemente de sua área. Se você é um desenvolvedor iniciante, pode pensar que esses dois termos significam a mesma coisa, mas são diferentes.

Este roteiro ajudará você a entender o que é Git e controle de versão, os comandos básicos do Git que você precisa conhecer, como você pode usar seus recursos para aumentar a eficiência do seu trabalho e como estender esses recursos usando o GitHub.

Este roteiro é voltado a iniciantes, pois os exemplos serão muito fáceis de entender. Também será um tutorial generalizado para que qualquer pessoa possa acompanhar, não importa qual seja sua linguagem de programação favorita.

Para nosso projeto, faremos uma lista de tarefas escrita em um arquivo de texto (txt). Você verá como podemos usar os recursos do Git para trabalhar e criar uma versão final da lista.

**Pré-requisitos**

Para concluir este roteiro, você precisará do seguinte:

* Uma interface de linha de comando, um terminal.
* Um editor de texto de sua escolha (usarei o **VS Code**).
* Uma conta no **GitHub**.

## O que é Git?

O Git é um sistema de controle de versão que permite rastrear as alterações feitas em seus arquivos ao longo do tempo. Com o Git, você pode reverter para vários estados de seus arquivos (como se usasse uma máquina do tempo). Você também pode fazer uma cópia do arquivo, fazer alterações nessa cópia e mesclar essas alterações na versão original.

Por exemplo, você pode estar trabalhando na página de destino de um site e descobrir que não gosta da barra de navegação. Ao mesmo tempo, você pode ficar apreensivo em começar a alterar seus componentes, porque o resultado pode ser pior.

Com o Git, você pode criar uma cópia idêntica desse arquivo e mexer na barra de navegação. Então, quando estiver satisfeito com suas alterações, poderá mesclar a cópia ao arquivo original.

Você não está limitado a usar o Git apenas para arquivos de código-fonte – você também pode usá-lo para acompanhar arquivos de texto ou até imagens. Isso significa que o Git não é apenas para desenvolvedores – qualquer um pode achá-lo útil.

### Como instalar o **Git**

Para usar o Git, você precisa instalá-lo em seu computador. Para fazer isso, você pode baixar a versão mais recente no [site da web oficial](https://git-scm.com/downloads). Você pode fazer o download para o seu sistema operacional a partir das opções fornecidas.

Você também pode instalar o Git usando a linha de comando, mas, como os comandos variam de acordo com cada sistema operacional, vamos nos concentrar na abordagem mais geral.

### Como configurar o **Git**

Vou assumir que, neste ponto, você já instalou o Git. Para verificar isso, você pode executar este comando no terminal: git --version. Ele mostra a versão atual instalada no seu PC.

A próxima coisa que você precisa fazer é definir seu nome de usuário e endereço de e-mail. O Git usará essas informações para identificar quem fez alterações específicas nos arquivos.

Para definir seu nome de usuário, digite e execute estes comandos:

    gitconfig --global user.name "SEU_NOME_DE_USUARIO"**

    gitconfig --global user.email "SEU_E-MAIL"**.

Apenas certifique-se de substituir "SEU_NOME_DE_USUARIO" e "SEU_E-MAIL" pelos valores que você escolher — ou seja, seu nome de usuário e seu e-mail reais.

### Como criar e inicializar um projeto no **Git**

Após terminarmos de instalar e configurar o Git, agora é hora de criar nosso projeto.

Criamos uma pasta, no desktop, chamada Git and GitHub tutorial. Usando a linha de comando, navegue até o local do seu novo projeto. Para execute os seguintes comandos:

```cd
cd desktop
cd git and github tutorial
```

Se você conhece a linha de comando há pouco e ainda está aprendendo a usá-la para navegar pelo seu PC, sugiro usar o Visual Studio Code da Microsoft. É um editor de código que possui um terminal embutido para executar comandos. Você pode baixá-lo [aqui](https://code.visualstudio.com/download).

Depois de instalar o VS Code, abra seu projeto no editor e abra um novo terminal para seu projeto. Isso apontará automaticamente o terminal/linha de comando para o caminho do seu projeto.

Agora, para inicializar um repositório do seu projeto, basta executar gitinit. Isso dirá ao Git para começar a observar seus arquivos a cada alteração que ocorrer. Esta é a aparência na linha de comando/terminal:** **

![Screenshot--95-]()git**init**

A primeira linha tem informações sobre meu PC e o caminho para a pasta. A segunda linha é o comando gitinit e a terceira linha é a resposta enviada de volta me dizendo que meu repositório (ou repo) foi inicializado. Ele é considerado vazio porque não informamos ao Git quais arquivos rastrear.** **

Um repositório é apenas outra maneira de definir um projeto que está sendo monitorado/rastreado pelo Git.

### Arquivos de projeto no **Git**

Criamos apenas um arquivo chamado todo.txt. Essa é a aparência do arquivo:** **

**
    MINHA LISTA DE TAREFAS**

1. Escrever um artigo.
2. Programar.
3. Estudar pelos livros.
4. Chegar nas aulas a tempo.
5. Visitar minha tia.
6. Me candidatar a trabalhos remotos.

---

    Antes de continuarmos aprendendo outros comandos do Git, vamos falar sobre o Github.

## O que é o GitHub?

O GitHub é um serviço de hospedagem on-line para repositórios do Git. Imagine trabalhar em um projeto em casa e, enquanto estiver fora – talvez na casa de um amigo, de repente – se dar conta da solução para um erro de código que o deixou inquieto por dias.

Você não pode fazer essas alterações porque seu PC não está com você. Se, contudo, você tiver seu projeto hospedado no GitHub, poderá acessar e baixar esse projeto com um comando em qualquer computador ao qual tenha acesso. Em seguida, você pode fazer suas alterações e enviar a versão mais recente de volta ao GitHub.

Em resumo, o GitHub permite que você armazene seu repositório em sua plataforma. Outro recurso incrível que vem com o GitHub é a capacidade de colaborar com outros desenvolvedores de qualquer local.

Agora que criamos e inicializamos nosso projeto localmente, vamos enviá-lo para o GitHub.

Se você é iniciante, encontrará alguns termos novos como push, commit, adde assim por diante – mas não se deixe assustar com eles. Com alguma prática, você será capaz de lembrar desses termos e do que eles fazem.

## *Como enviar um repositório para o **Github***

Dividimos esta seção em etapas para ajudá-lo a entender o processo com mais clareza.

**Passo** 1 – Crie uma conta no GitHub

    Para poder usar o GitHub, terá de criar uma conta primeiramente. Você pode fazer isso no[site da web](https://github.com/) do GitHub.

**Passo** 2 – Crie um repositório

    Você pode clicar no símbolo + no canto superior direito da página e escolher "New repository" (Novo repositório). Dê um nome ao seu repositório, role para baixo e clique no botão "Createrepository"  (Criar repositório).

**Passo** 3 – Adicionar e confirmar arquivos

    Antes de "adicionar" e "confirmar" nossos arquivos, você precisa entender os estágios de um arquivo que está sendo rastreado peloGit.

**Estado confirmado (committed)**

Um arquivo está no estado **confirmado** quando todas as alterações feitas no arquivo foram salvas no repositório local. Os arquivos no estágio confirmado são arquivos prontos para serem enviados para o repositório remoto (no GitHub).

**Estado modificado (modified)**

Um arquivo no estado **modificado **tem algumas alterações feitas nele, mas ainda não foi salvo. Isso significa que o estado do arquivo foi alterado de seu estado anterior no estado **confirmado**.

**Estado preparado (staged)**

Um arquivo no estado **preparado** significa que está pronto para ser confirmado. Nesse estado, todas as alterações necessárias foram feitas. Portanto, o próximo passo é mover o arquivo para o estado de confirmação.

Você pode entender isso melhor imaginando o Git como uma câmera. A câmera só tirará um instantâneo quando o arquivo atingir o estado de confirmação. Após este estado, a câmera começa a comparar as alterações feitas no mesmo arquivo com o último instantâneo (este é o estado modificado). Quando as alterações necessárias forem feitas, o arquivo é preparado e movido para o estado de confirmação para um novo instantâneo.

Isso pode ser muita informação para absorver no momento, mas não desanime – fica mais fácil com a prática.

### Como adicionar arquivos ao Git

Quando inicializamos nosso projeto, o arquivo não estava sendo rastreado pelo Git. Para isso, usamos o comando gitadd .** O ponto que vem depois de add representa todos os arquivos que existem no repositório. Se você quiser adicionar um arquivo específico (por exemplo, um arquivo chamado about.txt), use gitadd** about.txt**.**

Agora, nosso arquivo está no estado preparado. Você não receberá uma resposta após este comando, mas, para saber em que estado seu arquivo está, você pode executar o comando git status. ** **

### Como confirmar (commit) arquivos no Git

O próximo estado de um arquivo após o estado preparado é o estado confirmado. Para confirmar nosso arquivo, usamos o comando gitcommit -m "firstcommit"

A primeira parte do comando gitcommit diz ao Git que todos os arquivos preparados estão prontos para serem confirmados. Então, é hora de tirar um instantâneo. A segunda parte, -m "firstcommit"**, é a **mensagem de confirmação. -m é uma abreviação de mensagem enquanto o texto entre aspas é a mensagem de confirmação (que pode ser a mensagem que você quiser e no idioma que quiser).

Depois de executar este comando, você deve obter uma resposta semelhante a esta:

![Screenshot--97-]()gitcommit

Agora, nosso arquivo está no estado confirmado.

Passo 4 – Envie o repositório para o GitHub** **

Depois de criar o repositório, você deve ser redirecionado para uma página que informa como criar um repositório localmente ou enviar um já existente.

No nosso caso, o projeto já existe localmente, então usaremos comandos na seção "… ou enviar um repositório existente a partir da linha de comando". Estes são os comandos:

```
gitremoteaddorigin** https://github.com/ihechikara/git-and-github-tutorial.git**

gitbranch** -M main**

git push -u origin main** **
```

O primeiro comando, gitremoteaddorigin[https://github.com/ihechikara/git-and-github-tutorial.git](https://github.com/ihechikara/git-and-github-tutorial.git), cria uma conexão entre seu repositório local e o repositório remoto no GitHub.** **

O URL do seu projeto remoto deve ser totalmente diferente do anterior. Portanto, para acompanhar, certifique-se de seguir as etapas e trabalhar com seu próprio repositório remoto. Normalmente, você não receberá uma resposta após executar este comando, mas certifique-se de ter uma conexão com a internet.

O segundo comando, gitbranch -M main, altera o nome do seu branch principal para "main". O branch padrão pode ser criada como "master", mas "main" é o nome padrão para este repositório agora. Geralmente, não há resposta aqui.** **

O último comando, gitpush -u originmain**, envia seu repositório do seu dispositivo local para o GitHub. Você deve obter uma resposta semelhante a esta:**

![Screenshot--102-]()gitpush

Para ajudá-lo a aprofundar sua compreensão dos estágios do arquivo, farei alterações no arquivo e, em seguida, enviarei a nova versão para o GitHub.

Lembre-se de que nosso arquivo agora está no estado confirmado. Vamos fazer alterações no arquivo e anotar os estados.

Vou adicionar uma nova tarefa à lista de tarefas:

MINHA LISTA DE TAREFAS

---

1. Escrever um artigo.
2. Programar.
3. Estudar pelos livros.
4. Chegar nas aulas a tempo.
5. Visitar minha tia.

**6. Me candidatar a trabalhos remotos. **

7. Praticar programação

Depois de adicionar a nova tarefa, execute o comando git status. Isto é o que você deverá ver:** **

![Screenshot--98-]()git** status**

Depois de fazer alterações no arquivo, ele foi movido para o estado modificado, mas ainda não está preparado para confirmação. Então, você ainda não pode enviá-lo para o GitHub. O Git não tirou um instantâneo final desse estado atual, pois está apenas comparando as alterações que fizemos agora com o último instantâneo.

Agora vamos adicionar (preparar) este arquivo e, em seguida, confirmá-lo e enviá-lo. Isto é igual ao que fizemos na última seção.

Primeiro, adicionamos o arquivo usando gitadd ., que adiciona todos os arquivos na pasta (um único arquivo, no nosso caso). Em seguida, confirmamos o arquivo executando gitcommit -m "added new task"** (a mensagem significa "nova tarefa adicionada") seguido de gitpush** -u originmain**.**

Essas são as três etapas para enviar seus arquivos modificados para o GitHub. Você adiciona, confirma e, em seguida, envia. Espero que agora você entenda os estágios do arquivo e os comandos associados a eles.

### **Como usar branches no Git **

Com branches, você pode criar uma cópia de um arquivo no qual gostaria de trabalhar sem estragar a cópia original. Você pode mesclar essas alterações com a cópia original ou apenas deixar o branch permanecer independente.

Antes de começarmos a usar branches, quero mostrar uma representação visual do nosso repositório, que se parece com isso:

![g638]()branchmain

A imagem acima mostra nosso branch principal com os dois últimos commits (o primeiro commit e o commit da nova tarefa adicionada).

Neste ponto, quero adicionar mais tarefas à lista, mas ainda não tenho certeza se as quero na minha lista principal. Então, vou criar um outro branch chamado  test para ver como ficaria minha lista com mais tarefas incluídas.

Para criar um outro branch, execute este comando: git checkout -b test.** Vamos dividir isso em partes e explicar.**

checkout diz ao Git que deve mudar para um outro branch. -bdiz ao Git para criar esse outro branch. testé o nome do branch a ser criado e alterado. Aqui está a resposta que você deve obter:

![Screenshot--99-]()git** checkout -b**

Agora que criamos um outro branch, é assim que nosso repositório ficará:

![g664]()gitbranch

Criamos o outro branch a partir do estado do nosso último commit. Vamos agora adicionar mais tarefas a esse novo branch.

MINHA LISTA DE TAREFAS

---

1.Escrever um artigo.** **

2.Programar.

3.Estudar pelos livros.** **

4.Chegar nas aulas a tempo.** **

5.Visitar minha tia.** **

6.Me candidatar a trabalhos remotos.** **

7.Praticar programação

8.Completar a tarefa de estágio.** **

9.Praticar aberturas do xadrez.** **

10.Resolver quebra-cabeçasdo** xadrez**.** **

11.Verificar o cronograma dos testes**.**  ** **

---

  **	Adicionamos quatro novas tarefas. Para mesclar o novo estado com o branchmain**, você deve primeiro preparar e confirmar esse branch. Não entrarei em detalhes sobre o assunto, pois fizemos isso duas vezes na última seção.** **

Você deve tentar fazer isso sozinho para entender como funciona. Como dica, adicione o arquivo e, em seguida, confirme com uma mensagem (consulte a seção anterior para obter detalhes de como fazer isso).

Depois de confirmar seu branchtest, volte para o branchmainexecutando este comando: git checkout main.

Você notou que não adicionamos o -b ? Isso ocorre porque não estamos criando um outro branch, mas mudando para um branch existente. Você pode verificar todos os branches que existem em seu repositório executando o comando gitbranch ** **

Agora, podemos mesclar as alterações que fizemos no branchtestno branchmainexecutando git merge test.** Neste ponto, você verá todas as alterações feitas no branchtestrefletidas no branchmain. Você também deve receber uma resposta semelhante a esta:**

![Screenshot--100-]()git** merge**

Aqui está uma representação visual do nosso repositório:

![g816]()git** merge**

Se você continuar a enviar seu repositório para o GitHub, verá que o branchtest não será enviado. Ele permanecerá apenas em seu repositório local. Se você quiser enviar seu branchtest**, mude para ele usando git checkout test e execute o comando gitpush** -u origin test**.**

### **Como extrair um repositório no Git **

Fazer pullno Git significa clonar o estado atual de um repositório remoto em seu computador/repositório. Isso é útil quando você deseja trabalhar em seu repositório de um computador diferente ou quando está contribuindo para um projeto de código aberto on-line.

Para testar isso, não se preocupe em mudar para um novo computador. Basta executar cd .. para sair do diretório atual e voltar uma etapa. No meu caso, naveguei de volta para a minha área de trabalho.** **

Vá para o GitHub e, na página principal do seu repositório, você verá um botão verde que diz "Code". Ao clicar no botão, você deverá ver algumas opções em um menu suspenso. Vá em frente e copie o URL no formato HTTPS.

Depois disso, execute git clone SEU_URL_DE_HTTPS. Este comando puxa o repositório remoto para seu computador local em uma pasta chamada git-and-git-tutorial. Isto é o que você deverá ver em seu terminal:** **

![Screenshot--101-]()git** clone**

### Conclusão

Este artigo abordou os comandos básicos que ajudarão você a começar a usar o Git. Também começamos a aprender a usar o GitHub.

Se você seguiu até este ponto, parabéns. Você está pronto para seguir em frente. Agora, você pode usar o Git em seus projetos, independentemente da linguagem de programação que estiver usando.

Você deve saber que esses não são todos os comandos que existem no Git – portanto, sinta-se à vontade para fazer mais pesquisas para aprender mais comandos e seus usos. Esteé um ótimo lugar para ver uma lista detalhada de mais comandos do Git (em inglês).** **

---

## **Links**

git - guia prático** **

** **[https://rogerdudler.github.io/git-guide/index.pt_BR.html](https://rogerdudler.github.io/git-guide/index.pt_BR.html)

**--fast-version-control **

[https://git-scm.com/book/pt-br/v2](https://git-scm.com/book/pt-br/v2)

Interactive, Visual Git

[https://the-turing-way.netlify.app/reproducible-research/vcs/vcs-git-interactive](https://the-turing-way.netlify.app/reproducible-research/vcs/vcs-git-interactive)

LearnGitBranching!** **

[https://learngitbranching.js.org/?locale=pt_BR](https://learngitbranching.js.org/?locale=pt_BR)

UnderstandingGitthroughimages** **

[https://dev.to/nopenoshishi/understanding-git-through-images-4an1](https://dev.to/nopenoshishi/understanding-git-through-images-4an1)

A Visual GitReference

[https://marklodato.github.io/visual-git-guide/index-en.html](https://marklodato.github.io/visual-git-guide/index-en.html)

A Grip OnGit

[https://agripongit.vincenttunru.com/](https://agripongit.vincenttunru.com/)

VisualizingGitConceptswith** D3**

[https://onlywei.github.io/explain-git-with-d3/#rebase](https://onlywei.github.io/explain-git-with-d3/#rebase)

Como criar um repositório

[https://www.atlassian.com/br/git/tutorials/setting-up-a-repository](https://www.atlassian.com/br/git/tutorials/setting-up-a-repository)

---

---

---

---
