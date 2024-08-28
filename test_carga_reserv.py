from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):

    def on_start(self):
        """
        This method is called when a simulated user starts executing.
        We can use it to perform any necessary setup, like logging in the user.
        """
        self.client.get("/")  # Access the homepage
        self.login()

    def login(self):
        """
        Function to log in a user (you might need to adjust it according to your login form).
        """
        response = self.client.get("/login/")
        csrftoken = response.cookies['csrftoken']
        self.client.post("/login/", {
            "username": "testuser",
            "password": "password"
        }, headers={"X-CSRFToken": csrftoken})

    @task(1)
    def add_reserva(self):
        """
        Task to simulate adding a new reservation.
        """
        response = self.client.get("/reservas/add")
        csrftoken = response.cookies['csrftoken']
        
        # Exemplo de dados de formulário, ajuste de acordo com os seus campos.
        form_data = {
            "cliente_nome": "John Doe",
            "cliente_email": "john@example.com",
            "reserva_data": "2024-08-25",
            "servicos": [1, 2],  # IDs dos serviços
            "qtd": 1,
        }

        self.client.post("/reservas/add", data=form_data, headers={"X-CSRFToken": csrftoken})

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 3)
