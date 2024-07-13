from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutCompletePage(BasePage):

    MENSAGEM_CHECKOUT_COMPLETE = (By.ID, "checkout_complete_container")

    def buscar_mensagem_checkout_complete(self):
        self.verificar_se_elemento_existe(self.MENSAGEM_CHECKOUT_COMPLETE)