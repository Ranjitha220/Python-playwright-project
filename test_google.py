from playwright.sync_api import sync_playwright,expect

# print("hello world")
# len("hello")

# def test_google(url):
#     with sync_playwright() as p: #playwright context manager 
#         browser = p.chromium.launch(headless=False) 
#         page = browser.new_page()
#         page.goto(url)
#         print(page.title())
#     browser.close()
    
# test_google("https://www.google.com")
# test_google("https://www.bing.com") # without pytest
  
      
def test_google(page): #with pytest
    page.goto("https://www.google.com")
    print(page.title())
    expect(page).to_have_title("Google")
    
