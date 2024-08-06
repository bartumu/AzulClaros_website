# Modulo de Atendimento ao Cliente Para Azul Claros



Aplicação Web "MAC Azul Claros" usando Python "Django Framework"
## Sobre a aplicação web:

Aplicação Web "MAC Azul Claros" que permite:

- Fazer Reservas de Serviços
- Atender clientes
- Melhorar a Experiencia dos clientes
- Gerar relactório de Atendimento
- Gerar Dados de Analise para a Azul Claros


## Construído com:

- [Django Framwork](https://docs.djangoproject.com/en/)
- [MySqlClient Database](https://pypi.org/project/mysqlclient/)
- [HTML, CSS, JS, Bootstrap....](https://www.w3.org/)

## Instalação e execução do projecto:

1- Baixe ou clone o projecto


2- Instale o python na sua máquina

- [Baixe aqui](https://www.python.org/downloads/windows/)
- [verifique sua versão]

  ```bash
  python --version
  ```

  \*\* deve ser v.3 ou acima


3- Execute o seu servidor mysql e crie um novo esquema em seu SGBD com o nome "azulClarosDjango" 

4- Abra o projecto no VS Code

5- Abre o Arquivo .env e defina as informações do seu servidor de base de dados [nome do host e senha]


6- Em uma janela do Terminal execute o seguinte >>

- [instalar as dependências do Ambiente Virtual]

  ````bash
  pipenv shell

- [Sincronizar as dependências do Ambiente Virtual para o Local]

  ````bash
  pipenv sync


6- Execute o seguinte para carregar o banco de dados
```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

7- Crie o seu superusuário [admin] para acessar o [Admin Dashboard]

```bash
python manage.py createsuperuser
  > enter user name
  > enter user email
  > enter password
```

9- Depois de tudo concluído, execute o servidor

```bash
	python manage.py runserver
```

\*\* pegue o link (http://127.0.0.1:8000/) e coloque no seu navegador

## Notas

1- Você pode acessar o [Painel de Administração] por:

- No seu navegador (http://127.0.0.1:8000/admin)
- Digite o nome de usuário e a senha criada
- Adicione um novo usuário

2- Para acessar o [Painel dos Funcionários] >>

- No seu navegador acesse (http://127.0.0.1:8000/login)
- Entre com as credenciais criadas do usuário

3- Você Pode fazer as reservas no Menu Reserva no [Painel Inicial do Site] >>

- No seu navegador acesse (http://127.0.0.1:8000/)