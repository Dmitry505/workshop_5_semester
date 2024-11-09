class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.product = page.locator("[id='add-to-cart-sauce-labs-backpack']")
        self.check_buy = page.locator("[data-test='shopping-cart-badge']")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")

    def buy(self):
        self.product.click()

    def get_cart_count(self):
        return self.check_buy.inner_text()