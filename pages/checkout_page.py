from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):

    INPUT_FIRST_NAME = (By.ID, "first-name")
    INPUT_LAST_NAME = (By.ID, "last-name")
    INPUT_POSTAL_CODE = (By.ID, "postal-code")
    BUTTON_CONTINUE = (By.ID, "continue")

    def preencher_checkout(self, nome, sobrenome, cep):
        self.escrever_campo(self.INPUT_FIRST_NAME, nome)
        self.escrever_campo(self.INPUT_LAST_NAME, sobrenome)
        self.escrever_campo(self.INPUT_POSTAL_CODE, cep)
    
    def finalizar_checkout(self):
        self.clicar_elemento(self.BUTTON_CONTINUE)