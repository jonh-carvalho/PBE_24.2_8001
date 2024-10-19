## Member Get Member

### Resumo

A funcionalidade Member Get Member permite que os usuários da plataforma recomendem e convidem novos membros para se cadastrarem.
Através de um sistema de convites, os usuários atuais podem compartilhar links personalizados para novos usuários, incentivando o crescimento da comunidade da plataforma.

### Objetivo

Incentivar o crescimento orgânico da plataforma, permitindo que usuários existentes convidem novos membros para se cadastrarem. Além disso, a funcionalidade busca aumentar o engajamento ao oferecer recompensas tanto para quem indica quanto para quem é convidado, promovendo uma rede colaborativa de desenvolvimento profissional.
Jornadas do Usuário

1. Convidar um Novo Membro
2. Receber um Convite e Cadastrar-se
   Requisitos Técnicos

### Banco de Dados:

• Armazenar o link de convite personalizado associado ao ID do usuário
• que envia o convite.
• Registrar o vínculo entre o usuário que enviou o convite e o novo
• usuário que se cadastrou através do link.
• Manter histórico de convites enviados e aceitos para cada usuário.

### Frontend:

• Interface para exibir o link de convite personalizado para o usuário.
• Botões de compartilhamento integrados para redes sociais e email.
• Página de cadastro que identifica o convite e exibe o nome do usuário
• que enviou o convite.

### Backend:

• APIs para gerar e gerenciar links de convite personalizados.
• Validação do link de convite durante o processo de cadastro para garantir que o novo usuário seja corretamente vinculado ao usuário que enviou o convite.
• Controle de limites de convites por usuário, se aplicável.
• Autenticação e Autorização:
• Garantir que apenas usuários autenticados possam acessar e gerar links de convite.

Verificar a validade do link de convite durante o cadastro do novo
usuário (evitar o uso de links expirados ou inválidos).

## 
Regras de Negócio

1. Geração de Links de Convite:
2. Limite de Convites:
3. Validade dos Links de Convite:
4. Vinculação de Convites:
5. Cadastro do Convidado:
6. Sem Benefícios Imediatos:

## SWOT Pessoal

## Resumo

A funcionalidade SWOT Pessoal permite que o usuário realize uma análise SWOT (Strengths, Weaknesses, Opportunities, Threats) de sua própria carreira, identificando seus pontos fortes, pontos fracos, oportunidades de crescimento e ameaças que podem impactar seu desenvolvimento profissional.

### Objetivo

Permitir que o usuário identifique e avalie seus pontos fortes, fraquezas, oportunidades e ameaças em relação à sua carreira, facilitando a criação de um plano de ação alinhado ao seu desenvolvimento profissional. Estes dados serão utilizados para auxiliar o sistema na personalização do plano de carreira, missões e outros recursos.

### Jornadas do Usuário

1\. Primeira Utilização (Criação da Matriz SWOT) 

8. O usuário acessa a funcionalidade SWOT Pessoal no menu da plataforma. 

9. A interface apresenta uma breve introdução sobre o que é a análise SWOT
e seus benefícios. 

10. O usuário responde a perguntas orientadoras ou insere informações
diretamente nas quatro categorias: Forças, Fraquezas, Oportunidades e
Ameaças. 

11. Após preencher todos os campos, o usuário revisa as respostas e confirma
a conclusão da análise. 

12. A matriz SWOT é gerada e apresentada ao usuário em um formato visual. 

13. O usuário pode acessar a análise SWOT finalizada em sua área pessoal.
14. Revisão da Matriz SWOT 

15. O usuário acessa a funcionalidade e visualiza sua matriz SWOT anterior. 

16. A plataforma oferece a opção de atualizar as informações nas quatro
categorias (Forças, Fraquezas, Oportunidades e Ameaças). 

17. O usuário revisa e confirma as novas entradas.

18. A matriz atualizada é gerada e substitui a anterior.


Requisitos Técnicos


Banco de Dados:


Armazenamento de dados da análise SWOT: cada análise SWOT deve ser
associada ao perfil do usuário, com campos para Forças, Fraquezas,
Oportunidades e Ameaças.
Histórico de análises: manter um registro das análises anteriores, caso o
usuário queira comparar versões antigas.


Frontend:


Criação de uma interface intuitiva e responsiva para o preenchimento das
categorias da análise SWOT.
Exibição visual da matriz SWOT em formato de quadrantes, destacando os
itens inseridos pelo usuário.


Backend:


APIs para o envio e armazenamento das informações preenchidas pelo
usuário (Forças, Fraquezas, Oportunidades e Ameaças).
Manter a segurança dos dados do usuário, garantindo que apenas ele
possa acessar sua análise SWOT.
Regras de Negócio 19. Periodicidade da Análise:
O usuário pode realizar uma nova análise SWOT a cada x dias
(configurável). Durante esse intervalo, o usuário pode visualizar a análise
anterior, mas não pode editá-la até que o período configurado seja
completado. 20. Exclusividade da Análise:
Cada análise SWOT é pessoal e exclusiva ao usuário. Nem outros usuários
nem administradores terão acesso às análises SWOT de terceiros,
garantindo total privacidade das informações. 21. Preenchimento Parcial:
O usuário pode salvar uma análise SWOT mesmo que ela não esteja
totalmente preenchida. A análise será considerada como "Pendente" até
que seja marcada como “Concluída”. O usuário poderá voltar a qualquer
momento para finalizar e marcar a análise como "Concluída". 22. Histórico de Análises:
O sistema deve manter um histórico das análises SWOT realizadas pelo
usuário. O usuário pode consultar as análises anteriores.


## Feedbacks do Produto

### Resumo


A funcionalidade Captura de Feedbacks sobre o Produto permitirá que os
usuários forneçam feedback diretamente na plataforma sobre sua
experiência de uso, funcionalidades, desempenho e sugestões de melhoria. A
ferramenta será integrada de forma simples e acessível, com opções de
feedback direto ou através de questionários rápidos.


Objetivo


Esses feedbacks serão armazenados para análise pela equipe da plataforma,
ajudando a identificar áreas de melhoria e possíveis novas funcionalidades a
serem desenvolvidas.
Jornadas do Usuário 23. Envio de Feedback Espontâneo 24. O usuário acessa a seção Feedback no menu da plataforma. 25. A plataforma exibe um formulário simples para o usuário relatar sua experiência, incluindo campos opcionais para:
• Comentários gerais.
• Sugestões de melhoria.
• Relato de problemas técnicos ou erros. 26. O usuário preenche os campos desejados e envia o feedback. 27. A plataforma confirma o recebimento do feedback e exibe uma mensagem 28. de agradecimento.



### Requisitos Técnicos

### • Banco de Dados:


o Armazenar os feedbacks enviados pelos usuários, incluindo:
 ID do usuário.
 Texto do feedback.
 Tipo de feedback (sugestão, comentário, relato de erro).
 Data e hora do envio.
o Garantir que os feedbacks sejam associados ao perfil do usuário para
rastreabilidade e análise futura.

### • Frontend:


o Interface de formulário simples e intuitivo para o envio de feedback.
o Campos opcionais para tipos de feedback, como:
 Comentários gerais.
 Sugestões de melhorias.
 Relatos de erros ou problemas técnicos.
o Mensagem de confirmação após o envio do feedback.

### Backend:

o APIs para receber, processar e armazenar os feedbacks enviados pelos usuários.
o Garantir que os feedbacks sejam armazenados de forma segura e possam ser acessados pela equipe de análise.
Autenticação e Autorização:
• Garantir que apenas usuários autenticados possam enviar feedbacks,
associando cada feedback ao perfil do usuário.

## Regras de Negócio

### * Acesso à Funcionalidade:

Apenas usuários autenticados podem enviar feedbacks pela plataforma.

### * Tipos de Feedback:

• O feedback pode ser classificado em categorias opcionais, como:
• Comentários gerais.
• Sugestões de melhoria.
• Relato de erros ou problemas técnicos.

### * Envio de Feedback Parcial:

• O usuário não é obrigado a preencher todos os campos do feedback. Se desejar, pode deixar alguns campos em branco e enviar apenas um comentário.

### * Confirmação de Envio:

Após o envio do feedback, o sistema deve exibir uma mensagem de confirmação, assegurando o usuário que o feedback foi recebido.

### * Número de Feedbacks:

Não há limite para a quantidade de feedbacks que um usuário pode enviar. O usuário pode fornecer feedbacks múltiplos a qualquer momento.  



## Feedbacks entre Usuários

### Resumo


A funcionalidade Envio e Recebimento de Feedbacks entre Usuários permitirá
que os usuários da plataforma enviem e recebam feedbacks uns dos
outros, promovendo uma cultura de colaboração e desenvolvimento pessoal.
Os feedbacks podem ser solicitados ou enviados espontaneamente,
abrangendo aspectos como competências, comportamentos ou atividades
realizadas. Essa funcionalidade ajudará os usuários a obter insights valiosos de
colegas, mentores ou outros membros da comunidade, facilitando o
crescimento contínuo e o autodesenvolvimento.

### Objetivo

Facilitar a troca de feedbacks entre os usuários da plataforma, permitindo que
eles ofereçam e recebam avaliações construtivas sobre suas competências e
comportamentos profissionais. A funcionalidade busca promover o
crescimento contínuo e o autodesenvolvimento, fortalecendo a interação e
colaboração entre os membros da comunidade.

### Jornadas do Usuário

1\. Solicitar Feedback de Outro Usuário

* O usuário acessa a seção Feedback entre Usuários e escolhe a opção
  "Solicitar Feedback".
* O usuário seleciona o destinatário (um colega ou mentor da plataforma) e
  define o tipo de feedback que deseja receber (ex.: feedback sobre
  competências, comportamentos, ou uma atividade específica).

* O solicitante pode incluir uma mensagem opcional explicando o contexto
  ou o que gostaria de receber como retorno.
* Após enviar o feedback, o solicitante visualiza uma mensagem informando
  que o feedback foi recebido.

2\\. Enviar Feedback Espontâneo a Outro Usuário

* O usuário acessa a seção Feedback entre Usuários e escolhe a opção
  "Enviar Feedback".
* O usuário seleciona o destinatário e define o tipo de feedback
  (competências, comportamentos, ou outra área de foco).

* O usuário preenche o feedback e envia diretamente, sem a necessidade de
  solicitação prévia.
* O destinatário recebe o feedback em sua área pessoal.

3\. Visualizar Feedback Recebido

* O usuário acessa sua área pessoal e visualiza os feedbacks recebidos.
* O usuário pode consultar o histórico de feedbacks e responder ao
  feedback, se desejar, para iniciar uma conversa ou pedir mais detalhes.

4\\. Reportar Feedback Recebido

* O usuário acessa a seção de Feedbacks Recebidos e visualiza um
  feedback que considera ofensivo ou inapropriado.
* Na interface de visualização do feedback, o usuário encontra a opção
  "Reportar".

* O usuário clica na opção "Reportar" e seleciona o motivo do report (ex.:
  conteúdo ofensivo, impróprio, ou fora das diretrizes da plataforma).
* O sistema exibe uma confirmação de que o feedback foi reportado e será
  revisado pela equipe da plataforma.

* A equipe de moderação recebe o report, revisa o conteúdo, e toma as
  medidas cabíveis (ex.: remoção do feedback, aviso ou suspensão do
  usuário que enviou o feedback).
* O usuário que reportou o feedback pode ser informado do resultado da
  revisão, dependendo das diretrizes da plataforma.

## Requisitos Técnicos

Banco de Dados:


• Armazenar todos os feedbacks enviados entre os usuários, incluindo:
o ID do remetente (usuário que enviou o feedback).
o ID do destinatário (usuário que recebeu o feedback).
o Tipo de feedback (competências, comportamentos, atividade
o específica, etc.).
o Conteúdo do feedback (texto inserido pelo remetente).
o Data e hora de envio.

• Armazenar logs de report de feedbacks, incluindo:

o ID do feedback reportado.
o Motivo do report (conteúdo ofensivo, impróprio, etc.).
o ID do usuário que reportou o feedback.
o Status do report (pendente, revisado, ação tomada).

### Frontend:

• Interface para envio de feedbacks com opções para:

o Seleção do destinatário.
o Escolha do tipo de feedback (competências, comportamentos,
o etc.).
o Campo de texto para a mensagem do feedback.

• Interface para solicitação de feedback, onde o usuário pode selecionaro destinatário e especificar o contexto da solicitação.

• Visualização dos feedbacks recebidos em uma área privada, com aopção de responder ao feedback.

• Botão "Reportar" disponível na visualização de feedbacks recebidos,permitindo que o usuário selecione o motivo do report e envie asolicitação de revisão.

### Backend:

• APIs para:

o Envio de feedbacks entre usuários, garantindo que o feedback seja
o armazenado de forma segura e privada.
o Solicitação de feedback com as opções para selecionar o
o destinatário e o contexto.
o Gerenciamento de feedbacks recebidos, incluindo o histórico de
o feedbacks.
o Processamento de reports de feedbacks, registrando o motivo do
o report.
o Sistema de moderação que permite à equipe revisar feedbacks
o reportados e tomar as medidas cabíveis (ex.: remoção do feedback
o ou aviso ao usuário).

• Garantir a segurança dos dados, assegurando que somente oremetente e o destinatário possam acessar o conteúdo do feedback.

### Autenticação e Autorização:

• Garantir que apenas usuários autenticados possam enviar, solicitar, visualizar e reportar feedbacks.
• Implementar regras de autorização para que apenas o destinatário tenha acesso ao feedback recebido e apenas o remetente ao feedback enviado.

## **Regras de Negócio**

1. Privacidade dos Feedbacks:
   • Todos os feedbacks são estritamente privados, visíveis apenas pelo remetente (quem enviou) e pelo destinatário (quem recebeu). Nenhum outro usuário, incluindo administradores, tem acesso aos feedbacks trocados entre os usuários.
2. Envio de Feedback:
   Qualquer usuário autenticado pode enviar feedback espontâneo a outro usuário, selecionando o destinatário dentro da plataforma e preenchendo o formulário de feedback.
   O feedback deve estar relacionado a competências, comportamentos, ou atividades específicas, com a opção de adicionar uma mensagem contextual.
3. Solicitação de Feedback:
   • Qualquer usuário autenticado pode solicitar feedback de outro usuário, especificando o tipo de feedback desejado (competências, comportamentos, etc.) e o contexto da solicitação.
   • O destinatário tem a liberdade de aceitar ou ignorar a solicitação de feedback sem penalidades.
4. Limites de Feedbacks:

• Não há limites definidos para o número de feedbacks que um usuáriopode enviar ou receber. Os usuários podem fornecer feedbacks múltiplos de acordo com as necessidades.

5. Respostas aos Feedbacks:

• Após receber um feedback, o destinatário pode responder diretamente ao remetente para agradecer ou solicitar mais detalhes. A resposta também será privada e apenas visível para o remetente original e o destinatário.

5. Moderação de Conteúdo:

• Todos os feedbacks devem seguir as diretrizes de uso da plataforma. Qualquer conteúdo ofensivo, impróprio ou fora das normas pode ser reportado pelo destinatário.
• O usuário que recebeu um feedback pode reportá-lo como ofensivo ou impróprio. O sistema registrará o report e o feedback será revisado pela equipe da plataforma.
• A equipe de moderação será responsável por revisar os feedbacks reportados e tomar as medidas cabíveis, como remoção do feedback ou aplicação de avisos ao usuário que enviou o conteúdo reportado.

6. Processo de Report:

• O destinatário de um feedback pode reportar o conteúdo se considerar que ele viola as diretrizes da plataforma.
• Após o report, o sistema registra o motivo.
• A equipe de moderação revisa o feedback e decide se uma ação é necessária (remoção ou advertência ao remetente).
• O usuário que reportou o feedback pode ser informado do resultado da moderação, dependendo das diretrizes da plataforma.
