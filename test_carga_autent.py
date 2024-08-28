from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):

    def on_start(self):
        # Captura o token CSRF para o envio de formulário
        response = self.client.get("/login/")
        self.csrftoken = response.cookies['csrftoken']

    @task
    def login(self):
        self.client.post("/login/", {
            "email": "testuser@example.com", 
            "password": "password123",
            "csrfmiddlewaretoken": self.csrftoken
        }, headers={"Referer": "/login/"})

    @task
    def recuperar_senha(self):
        self.client.post("/recuperar/", {
            "email": "testuser@example.com",
            "csrfmiddlewaretoken": self.csrftoken
        }, headers={"Referer": "/recuperar/"})

    @task
    def atualizar_senha(self):
        self.client.post("/recuperar/senha/?email=testuser@example.com", {
            "password": "novaSenha123",
            "password_confirm": "novaSenha123",
            "csrfmiddlewaretoken": self.csrftoken
        }, headers={"Referer": "/recuperar/senha/?email=testuser@example.com"})

    @task
    def logout(self):
        self.client.get("/logout/")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)

