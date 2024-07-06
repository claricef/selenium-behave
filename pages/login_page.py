from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):

    INPUT_USERNAME = (By.ID, "user-name")
    INPUT_PASSWORD = (By.ID, "password")
    BUTTON_LOGIN = (By.ID, "login-button")
    ERROR = (By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")

    def preencher_login_usuario_cadastrado(self, usuario, senha):
       self.escrever_campo(self.INPUT_USERNAME, usuario)
       self.escrever_campo(self.INPUT_PASSWORD, senha)
    
    def acessar_sistema(self):
        self.clicar_elemento(self.BUTTON_LOGIN)
    
    def buscar_mensagem_login_invalido(self):
        self.verificar_se_elemento_existe(self.ERROR)
