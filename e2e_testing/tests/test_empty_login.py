from playwright.sync_api import expect
from pages.login_po import LoginPage


def test_login_invalid(page):
    login_page = LoginPage(page)

    login_page.navigate()
    login_page.login("", "")

    expect(login_page.error_locator).to_have_text(
        "Epic sadface: Username is required")
