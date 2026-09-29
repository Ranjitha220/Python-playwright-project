import pytest
from playwright.sync_api import Page, expect

# @pytest.mark.asyncio
# async def test_click_fill_type_clear_waits(async_page):
#       await async_page.goto("https://www.google.com/")
#       await expect(async_page).to_have_title("Google")
#       ele = await async_page.locator("textarea[name='q']").type("Mobile")
#       await async_page.locator("textarea[name='q']").clear()
#       await async_page.locator("textarea[name='q']").fill("Books")
#       await async_page.locator("textarea[name='q']").Enter()
#       expect(async_page).to_have_title("Books - Google Search")      
      
      
@pytest.mark.asyncio
async def test_get_text_attribute(async_page):
      await async_page.goto("https://demowebshop.tricentis.com/")
      print(await async_page.locator("#pollanswers-1").inner_text())
      
      print(await async_page.get_by_text("$25 Virtual Gift Card").get_attribute("href"))
      
      
   
