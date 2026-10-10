from playwright.sync_api import expect

def test_get_by_title(page):
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(1000)
    logo = page.get_by_title("Speed | Tricentis")
    logo.click()
    
    
# def test_get_by_test_id(page):
#     page.goto("https://demowebshop.tricentis.com/")
#     page.wait_for_timeout(1000)
#     logo = page.get_by_test_id("Tricentis Demo Web Shop")
#     logo.click()
#     expect(logo).to_be_visible()