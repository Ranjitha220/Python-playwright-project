#iframe
import pytest 
from playwright.async_api import expect 


# @pytest.mark.asyncio
# async def test_iframe(async_page):
#     await async_page.goto("https://www.amazon.in/")
#     await async_page.locator("#twotabsearchtextbox").fill("books")
#     await async_page.locator("#twotabsearchtextbox").press("Enter")
#     check_box = await async_page.locator("//i[@class='a-icon a-icon-checkbox']").all()
#     for radio in check_box:
#         await radio.click() 

#sort the lists

@pytest.mark.asyncio
async def test_drop(async_page):
  await async_page.goto("https://www.amazon.in/")
  search_box= async_page.locator("#twotabsearchtextbox")
  await search_box.fill("books")
  
  await async_page.wait_for_timeout(2000)
  
  await search_box.press("ArrowDown")
  await search_box.press("ArrowDown")
  await search_box.press("ArrowDown")
  await search_box.press("Enter")
 