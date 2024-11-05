# . **Regras de Negócio**

## 1. **Regras de Negócio para Usuários**

- **Cadastro e Login:**

  - Apenas usuários registrados podem acessar funcionalidades como criação de playlists, upload de conteúdo e gerenciamento de conteúdo.
  - Um sistema de verificação por e-mail deve ser implementado para garantir que apenas e-mails válidos sejam utilizados para cadastro.
- **Perfis de Usuário e Permissões:**

  - Usuários básicos podem criar e gerenciar suas playlists pessoais, mas não podem fazer upload de conteúdo.
  - Criadores de conteúdo e administradores possuem permissões adicionais para fazer upload de conteúdo e gerenciar suas criações.
  - Os administradores possuem acesso completo ao sistema, incluindo edição e exclusão de conteúdos e playlists de qualquer usuário.
- **Gerenciamento de Contas:**

  - Cada usuário deve poder visualizar e gerenciar suas playlists e conteúdos.
  - Somente o proprietário de uma playlist pode editá-la ou excluí-la, com exceção dos administradores.

## 2. **Regras de Negócio para Playlists**

- **Criação e Gerenciamento de Playlists:**

  - Um usuário pode criar um número limitado de playlists (limite configurável) para evitar excesso de dados no sistema.
  - Playlists devem ter um título único dentro do contexto do usuário para facilitar a busca e organização.
  - Conteúdos podem ser adicionados a uma playlist apenas uma vez; duplicatas não são permitidas.
  - É permitido que o usuário compartilhe suas playlists publicamente se o recurso for ativado (opção de playlist pública).
- **Conteúdos em Playlists:**

  - Somente conteúdos públicos podem ser adicionados a playlists públicas.
  - Conteúdos privados podem ser adicionados a playlists privadas, mas não podem ser compartilhados ou visualizados por outros usuários.
  - Usuários podem reordenar conteúdos dentro de suas playlists.

## 3. **Regras de Negócio para Conteúdos**

- **Upload e Gerenciamento de Conteúdos:**

  - Apenas usuários com permissão de criador de conteúdo podem fazer uploads. O conteúdo deve estar nos formatos de arquivo suportados (ex.: `.mp4`, `.mp3`).
  - Cada conteúdo deve ter uma miniatura (thumbnail) e uma descrição para melhorar a experiência do usuário e facilitar a navegação.
  - O título de cada conteúdo deve ser único por criador para evitar confusão.
- **Políticas de Publicação:**

  - Todo conteúdo passa por uma verificação automatizada para garantir que não contenha materiais impróprios ou violações de direitos autorais.
  - Criadores podem definir se seu conteúdo será **público** ou **privado**.
  - Conteúdos públicos podem ser visualizados e adicionados a playlists de qualquer usuário, enquanto conteúdos privados são acessíveis apenas ao criador e a playlists privadas.

## 4. **Regras de Negócio para Consumo de Conteúdos**

- **Streaming e Download:**
  - Conteúdos públicos podem ser reproduzidos via streaming por qualquer usuário, desde que respeite as permissões de visualização.
  - Downloads de conteúdos podem ser restritos a usuários premium, com limitação de número de downloads mensais.
  - Usuários podem marcar conteúdos como favoritos para acessá-los rapidamente, mas essa funcionalidade está limitada a um certo número de favoritos por perfil básico.

## 5. **Notificações e Feedback**

- **Sistema de Notificações:**

  - Os usuários devem ser notificados quando novos conteúdos de criadores que eles seguem são publicados.
  - Notificações também devem alertar sobre o status de uma playlist ou conteúdo, como exclusões, alterações de privacidade, entre outros.
- **Feedback e Reportes:**

  - Usuários devem poder reportar conteúdos impróprios ou que violam as regras da plataforma.
  - Comentários e avaliações de conteúdos são permitidos para incentivar o engajamento e fornecer feedback aos criadores.

## 6. **Regras de Negócio para Assinaturas e Recursos Premium**

- **Modelo de Assinatura:**

  - Usuários podem fazer upgrade para uma conta premium, que oferece vantagens como downloads ilimitados, acesso antecipado a conteúdos, e acesso exclusivo a playlists e conteúdos especiais.
  - O sistema deve garantir a renovação automática das assinaturas premium e permitir cancelamento a qualquer momento.
- **Benefícios Premium:**

  - Assinantes premium podem ter um número maior de playlists e favoritos, bem como maior capacidade de armazenamento de playlists.
  - Conteúdos premium (acessíveis apenas por assinantes) podem ser disponibilizados para atrair novos criadores e assinantes.

### 7. **Regras de Negócio para Segurança e Conformidade**

- **Políticas de Privacidade e Compliance:**

  - Todos os dados de usuários devem ser armazenados em conformidade com a GDPR ou outra legislação local aplicável.
  - Somente administradores e o próprio usuário podem acessar dados pessoais sensíveis.
- **Limites de Acesso e Proteção de Dados:**

  - Taxas de requisição (rate-limiting) devem ser aplicadas para evitar uso excessivo ou ataques à API.
  - Um sistema de autenticação robusto deve ser implementado, incluindo verificação de senha forte e autenticação multifator (2FA) para usuários premium ou criadores de conteúdo.

Essas regras de negócio ajudam a definir o comportamento do app, permitindo que ele seja usado de maneira organizada, segura e eficiente tanto por usuários finais quanto por administradores e criadores.
