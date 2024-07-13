from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventarioItemPage(BasePage):

    BUTTON_ADD_CART = (By.ID, "add-to-cart")
    ICONE_ITEM_CART = (By.XPATH, "//*[@id='shopping_cart_container']/a/span")
    BUTTON_CART = (By.ID, "shopping_cart_container")

    def adicionar_item_carrinho(self):
        self.clicar_elemento(self.BUTTON_ADD_CART)
    
    def buscar_icone_item_adicionado(self):
        self.verificar_se_elemento_existe(self.ICONE_ITEM_CART)
    
    def acessar_carrinho(self):
         self.clicar_elemento(self.BUTTON_CART)
