from playwright.sync_api import sync_playwright

print("hello world")
len("hello")


with sync_playwright() as p: #playwright context manager 
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()
        page.goto("https://www.google.com")
        print(page.title())
        browser.close()
    
