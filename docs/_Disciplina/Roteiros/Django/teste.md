from django.contrib.auth.models import User

# Cria um novo usuário com uma senha simples
user = User.objects.create_user(username='meu_usuario', password='senha_simples')

# Ou atualiza a senha de um usuário existente
user = User.objects.get(username='meu_usuario')
user.set_password('nova_senha_simples')
user.save()