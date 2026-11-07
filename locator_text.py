
from playwright.sync_api import expect
def test_get_by_text(page):
    page.goto("https://www.facebook.com")
    login_to_facebook_text = page.get_by_text("Log in to Facebook")
    expect(login_to_facebook_text).to_be_visible()
    forgot_password_button = page.get_by_text("Forgotten password")
    forgot_password_button.click()
    page.wait_for_timeout(1000)
    
