from selenium.webdriver.common.by import By
from .base_page import BasePage

class CarrinhoPage(BasePage):

    BUTTON_CHECKOUT = (By.ID, "checkout")
    
    def realizar_checkout(self):
        self.clicar_elemento(self.BUTTON_CHECKOUT)
    