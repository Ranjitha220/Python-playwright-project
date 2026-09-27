from playwright.sync_api import expect
def test_get_by_alt_text(page):
    page.goto("https://demowebshop.tricentis.com/")
    logo = page.get_by_alt_text("Tricentis Demo Web Shop")
    expect(logo).to_be_visible()

def test_get_by_title(page):
    page.goto("https://demowebshop.tricentis.com/")
    logo = page.get_by_title("Tricentis Demo Web Shop")
    logo.click()
    
    
def test_get_by_test_id(page):
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(1000)
    logo = page.get_by_test_id("Tricentis Demo Web Shop")
    logo.click()
    expect(logo).to_be_visible()