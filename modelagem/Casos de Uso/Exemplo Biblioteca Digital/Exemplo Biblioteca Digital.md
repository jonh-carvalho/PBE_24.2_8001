## Problema de Modelagem

Você foi contratado para desenvolver um sistema para gerenciar uma **biblioteca de livros digitais**. O sistema permitirá que os usuários façam login, procurem livros, reservem livros, e baixem cópias para leitura offline. A biblioteca também oferece assinatura premium, onde os usuários podem acessar livros exclusivos e ganhar vantagens especiais, como reservas antecipadas e downloads ilimitados.

---

### Caso de Uso

#### **Título**: Usuário Reserva um Livro

1. **Ator Principal**: Usuário autenticado
2. **Atores Secundários**: Sistema de pagamento (para verificação de status de assinatura)
3. **Pré-condições**:
   - O usuário deve estar autenticado.
   - O livro desejado deve estar disponível para reserva.
4. **Fluxo Principal**:
   1. O usuário navega na biblioteca e seleciona um livro disponível.
   2. O sistema verifica se o usuário é um assinante premium.
      - Se sim, permite a reserva imediata.
      - Se não, verifica se o número de reservas permitidas não foi excedido.
   3. O sistema realiza a reserva do livro e informa o prazo máximo para retirada.
   4. O sistema atualiza o status do livro como "Reservado" e o associa ao usuário.
5. **Fluxos Alternativos**:
   - Se o livro não estiver disponível para reserva, o sistema informa ao usuário que o livro está indisponível.
   - Se o usuário excedeu o limite de reservas, o sistema informa que não é possível realizar mais reservas.
6. **Pós-condições**:
   - O livro é reservado com sucesso e o status é atualizado.
   - O usuário é notificado do prazo para retirar o livro.

---

### Pontos para Modelagem

A partir deste caso de uso, você pode definir os seguintes objetos e suas interações:

1. **Usuário**:
   - Atributos: nome, email, status de assinatura, número de reservas.
   - Métodos: autenticar(), reservarLivro(), cancelarReserva().

2. **Livro**:
   - Atributos: título, autor, status (disponível, reservado, indisponível), prazo de retirada.
   - Métodos: verificarDisponibilidade(), reservar(), liberarReserva().

3. **Biblioteca**:
   - Atributos: catálogo de livros, usuários cadastrados.
   - Métodos: buscarLivro(), registrarReserva(), verificarLimiteReservas().

4. **Assinatura**:
   - Atributos: tipo (premium, básico), limite de reservas.
   - Métodos: verificarBenefícios().

---

Esse cenário pode ser expandido com novos casos de uso, como o gerenciamento de downloads ou renovação de assinaturas.