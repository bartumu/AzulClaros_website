from locust import HttpUser, TaskSet, task, between
from bs4 import BeautifulSoup
from random import randint

class FuncionarioTasks(TaskSet):
    
    def on_start(self):
        """Login antes de iniciar os testes e armazena o token CSRF."""
        self.login()

    def login(self):
        """Realiza login e extrai o token CSRF."""
        response = self.client.get("/login/")
        soup = BeautifulSoup(response.text, 'html.parser')
        csrftoken = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
        
        self.client.post("/login/", {
            "username": "seu_username",
            "password": "sua_senha",
            "csrfmiddlewaretoken": csrftoken
        }, headers={'Referer': "/login/"})
    
    def get_csrf_token(self, url):
        """Navega até uma URL e extrai o token CSRF."""
        response = self.client.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']

    @task(2)
    def func_dashboard(self):
        """Testa o dashboard principal do funcionário."""
        self.client.get("/dashBoard/func")

    @task(2)
    def list_reserva(self):
        """Testa a listagem de reservas."""
        self.client.get("/dashBoard/func/Reserva")

    @task(1)
    def levantamento(self):
        """Testa a página de levantamento."""
        self.client.get("/dashBoard/func/reservaLev")
    
    @task(1)
    def atendimento(self):
        """Simula o atendimento de uma reserva específica com token CSRF."""
        reserva_id = randint(1, 100)
        csrftoken = self.get_csrf_token(f"/dashBoard/func/reserva/{reserva_id}")
        
        self.client.post(f"/dashBoard/func/reserva/{reserva_id}", data={
            'data_saida': '2024-08-30',
            'pagamento': 1,
            'csrfmiddlewaretoken': csrftoken
        }, headers={'Referer': f"/dashBoard/func/reserva/{reserva_id}"})

    @task(1)
    def levantar_reserva(self):
        """Simula o levantamento de uma reserva específica com token CSRF."""
        reserva_id = randint(1, 100)
        csrftoken = self.get_csrf_token(f"/dashBoard/func/levantar/{reserva_id}")
        
        self.client.post(f"/func/levantar/{reserva_id}", data={
            'data_saida': '2024-08-30',
            'csrfmiddlewaretoken': csrftoken
        }, headers={'Referer': f"/dashBoard/func/levantar/{reserva_id}"})

    @task(1)
    def acessar_perfil(self):
        """Testa o acesso e edição do perfil do funcionário com token CSRF."""
        response = self.client.get("/dashBoard/func/perfil")
        csrftoken = self.get_csrf_token("/dashBoard/func/perfil")
        
        self.client.post("/func/perfil", data={
            'nome': 'Novo Nome',
            'email': 'email@dominio.com',
            'numero': '999999999',
            'endereco': 'viana',
            'genero': 'm',
            'csrfmiddlewaretoken': csrftoken
            # Inclua outros campos relevantes aqui
        }, headers={'Referer': "/dashBoard/func/perfil"})

class WebsiteUser(HttpUser):
    tasks = [FuncionarioTasks]
    wait_time = between(1, 5)

    def on_start(self):
        """Autentica o usuário."""
        response = self.client.get("/login/")
        soup = BeautifulSoup(response.text, 'html.parser')
        csrftoken = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
        
        login_response = self.client.post("/login/", {
            "username": "seu_username",
            "password": "sua_senha",
            "csrfmiddlewaretoken": csrftoken
        }, headers={'Referer': "/login/"})
        
        if login_response.status_code == 200:
            print("Autenticado com sucesso.")
        else:
            print("Falha na autenticação.")
