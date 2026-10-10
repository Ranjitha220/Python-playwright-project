#Amazon – Left Navigation Headings

from playwright.sync_api import sync_playwright, expect
def test_scenario_2():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.amazon.in/")

        # Open left navigation
        menu = page.locator("xpath=//*[@id='nav-hamburger-menu']/span")
        menu.click()
        page.wait_for_timeout(2000)

        # Locate main headings
        headings = page.locator("xpath=//*[@id='hmenu-content']//div[contains(@class, 'hmenu-visible')]//section[contains(@class, 'category-section')]")
  
        print("\n--- Main Headings ---")
          
        for i in range(headings.count()):
              heading_text = headings.nth(i).get_attribute("aria-labelledby")
              print(heading_text)
  
       
        
        
        