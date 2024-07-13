from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventarioPage(BasePage):

    LINK_ITEM = (By.ID, "item_4_title_link")

    def acessar_item(self):
        self.clicar_elemento(self.LINK_ITEM)
