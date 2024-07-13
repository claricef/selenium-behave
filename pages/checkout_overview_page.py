from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutOverviewPage(BasePage):

    BUTTON_FINISH_COMPRA = (By.ID, "finish")

    def finalizar_compra(self):
        self.clicar_elemento(self.BUTTON_FINISH_COMPRA)