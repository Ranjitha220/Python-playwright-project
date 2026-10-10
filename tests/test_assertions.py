##extracting attribute values and text 
import pytest
from playwright.async_api import Page, expect
from requests import options

# @pytest.mark.asyncio
# async def test_click_fill_type_clear_waits(async_page):
    
#       await async_page.goto("https://www.google.com/")
#       await expect(async_page).to_have_title("Google")
#       await async_page.locator("textarea[name='q']").type("Mobile")
#       await async_page.locator("textarea[name='q']").clear()
#       await async_page.locator("textarea[name='q']").fill("Books")
#       await async_page.locator("textarea[name='q']").press("Enter")
#       await expect(async_page).to_have_title("Books - Google Search") 
      
      #robot caption error - failed 
      # run in headed mode 
   
      
# @pytest.mark.asyncio
# async def test_get_text_attribute(async_page):
#       await async_page.goto("https://demowebshop.tricentis.com/")
#       ele = async_page.locator("#pollanswers-1") #id used 
#       print(await(ele.inner_text()))
#       ele1 = async_page.get_by_text("$25 Virtual Gift Card") #text used
#       print(await(ele1.get_attribute("href")))
      
#get text

# @pytest.mark.asyncio
# async def test_get_text_attribute1(async_page):
#       await async_page.goto("https://demowebshop.tricentis.com/")
#       ele = async_page.locator(".topic-html-content-header")
#       print(await(ele.inner_text())) #Welcome to our store
            
      #print(await(ele.text_content())) #full html text content

   
#Assertions
# @pytest.mark.asyncio
# async def test_assertions(async_page):
#         await async_page.goto("https://demowebshop.tricentis.com/")
#         ele = async_page.locator(".topic-html-content-header")
#         expect(ele).to_be_visible()
#         print(await(ele.inner_text()))
        
        
@pytest.mark.asyncio
async def test_assertions(async_page):
        await async_page.goto("https://demowebshop.tricentis.com/")
        await expect(async_page).to_have_title("Demo Web Shop")
        options = async_page.locator("//li[@class='answer']")
        await expect.soft(options).to_have_count(4) #soft assertion - ignore
        await options.nth(0).click()  
       
        

      
      