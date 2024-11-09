from playwright.sync_api import expect
from pages.login_po import LoginPage


def test_login_invalid(page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("standard_user", "wrong_password")

    expect(login_page.error_locator).to_have_text(
        "Epic sadface: Username and password do not match any user in this service")