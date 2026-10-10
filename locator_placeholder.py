from playwright.sync_api import expect
def test_get_by_placeholder(page):
    page.goto("https://www.amazon.in/")
    page.wait_for_timeout(1000)
    page.get_by_placeholder("Search Amazon.in").fill("mobiles")
    page.keyboard.press("Enter")
    page.wait_for_timeout(1000)

def test_get_by_alt_text(page): #only for images
    page.goto("https://demowebshop.tricentis.com/")
    logo = page.get_by_alt_text("Tricentis Demo Web Shop")
    expect(logo).to_be_visible()
    
