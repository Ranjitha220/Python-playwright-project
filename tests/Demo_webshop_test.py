#load the .env file
from utilis.config import BASE_URL, USERNAME, PASSWORD
# from dotenv import load_dotenv
# import os

# load_dotenv()

def test_navigate(page): #navigation methods
    page.goto(BASE_URL)
    print(page.url)
    print(page.title())
    page.reload()
    page.goto("https://www.facebook.com")
    print(page.url)
    page.go_back()
    page.go_forward()
    
    
    
