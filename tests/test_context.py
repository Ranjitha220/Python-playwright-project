
#open 2 browsers in 1 test[context]

from playwright.sync_api import sync_playwright,expect
def test_application():
    with sync_playwright() as p:
      browser = p.chromium.launch(headless=False)
      
      end_user_context = browser.new_context()
      end_user_page = end_user_context.new_page()
      end_user_page.goto("https://agents.akbartravelsonline.com/b2bplus/flight")
      expect(end_user_page).to_have_title("Cheap Flights ; Domestic ; International Flight Offers in India")
      
      admin_context = browser.new_context()
      admin_page = admin_context.new_page()
      admin_page.goto("https://agents.akbartravelsonline.com/b2bplus/flight")
      expect(admin_page).to_have_title("Cheap Flights ; Domestic ; International Flight Offers in India")
         