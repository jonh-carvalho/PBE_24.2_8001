---
id: documento_de_arquitetura
title: Documento de Arquitetura
---
 
# Documento de Arquitetura de Software (DAS)
# "Nome do Projeto"
 
# Introdução
## Proposta
<p align = "justify">
Este documento apresenta uma visão geral da arquitetura do sistema, utilizando diferentes visões arquiteturais para destacar diferentes aspectos do sistema. É utilizado para capturar as decisões arquiteturais significativas que fizeram parte do sistema.
</p>
 
## Escopo
<p align = "justify">
A aplicação "XXXX" tem o objetivo fornecer...
</p>
 
## Definições, Acrônimos e Abreviações
 
- MVC - 
- MVT - 
- SIGLA PARA O APP - Nome do Aplicativo
 
## Visão Geral
<p align = "justify">
O Documento de Arquitetura de Software (DAS) trata-se de uma visão geral de toda a arquitetura do sistema, observando diferentes aspectos do mesmo. Neste documento serão abordadas as seguintes visões da aplicação TCM:
</p>
 
- Caso de Uso;
- Lógica;
- Implantação;
- Implementação;
- Dados;
 
# Representação Arquitetural
## Cliente-Servidor
<p align = "justify">
Cliente-Servidor é um modelo de arquitetura...
</p>
 
Cliente (Frontend):
 
- View: Consiste.....
 
Servidor (Backend):
 
- Controller: faz a conexão entre as camadas...
 
- Service: Responsável pela lógica...
 
- Model: Responsável pela persistência...
 
 
# Objetivos de Arquitetura e Restrições
## Objetivos
<p align = "justify">
Segurança:
   -
Persistência:
   - 
Privacidade:
   - Middlewares: Foi usado middlewares...
Desempenho:
   Requisições...
Reusabilidade:
   Componentes no Frontend...
</p>
 
## Restrições
<p align = "justify">
Tamanho da tela:...
 
Portabilidade:...
 
|IE|Edge|Firefox|Chrome|Safari|Googlebot|
|--|----|-------|------|------|---------|
|11 |>= 14|>= 52|>= 49|>= 10|Sim|
 
Serviços: Os serviços oferecidos....
 
Acesso a internet: A aplicação está limitada apenas a conexão com internet
</p>
 
## Ferramentas Utilizadas
 
- XXX: Ambiente de execução...
- XXXX: Linguagem de programação...
Typescript: XXXX
- XXXX: XXXX
- XXX: XXXX
- XXXX: XXXX
- XXXX: XXXX
- XXXX: XXXX
- XXXXX: XXXX.

 
# Visão de Caso de Uso
 
<p align = "justify">
O primeiro caso de uso descreve a ação de um usuário que cria um torneio, sendo assim, ele é o manager do torneio. No segundo caso de uso descreve a ação de um usuário que é entra na aplicação com a intenção de entrar em torneios como jogador. Nos dois casos o usuário pode ser o mesmo, porém com funções diferentes.
</p>
 
![Caso de uso 1](../assets/Casos_de_uso/caso_de_uso_1.png)
 
![Caso de uso 2](../assets/Casos_de_uso/caso_de_uso_2.png)
 
# Visão Lógica
 

# Visão de Implantação
![Diagrama de Implantação](../assets/Diagrama_implantacao/diagrama_de_implantacao.png)
 
# Visão de Implementação
## Visão Geral
![Diagrama de Componentes](../assets/Diagrama_componentes/diagrama_de_componentesV2.0.png)
 
# Visão de Dados
 
## Modelo Entidade Relacionamento (MER)
 
 
#### Entidades e Relacionamentos:
 
## Diagrama Entidade Relacionamento (DER)
 
# Tamanho e Desempenho
 
# Qualidade
 
</p>
 
# Referências Bibliográficas
> 
> 
> 
 
# Histórico de Versão
| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 08/11/2020 | 1.0 | Criada estrutura básica do documento | xxx xxx, xxx xx, xxx xx, xxx xxx e xxx xxxx |
| 15/11/2020 | 1.1 | Representação arquitetural e objetivos e restrições arquiteturais.  | Autores |
| 19/11/2020| 1.2 | Adição dos diagramas, visões, tamanho e desempenho e qualidade | Autores |
|20/11/2020|1.3| Adição da descrição de MER e DER | Autores |
|20/11/2020|1.4| Adição do tópico de qualidade | Autores |
|20/11/2020|1.5| Revisão | Autores |
