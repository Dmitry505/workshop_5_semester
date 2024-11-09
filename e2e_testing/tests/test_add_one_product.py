from playwright.sync_api import expect
from pages.login_po import LoginPage
from pages.products_po import ProductsPage


def test_login_invalid(page):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    products_page.navigate()
    products_page.buy()

    expect(products_page.check_buy).to_have_text("1")