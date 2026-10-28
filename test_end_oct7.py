#scrolling 

import pytest
from playwright.async_api import expect

# @pytest.mark.asyncio
# async def test_scroll(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     footer = async_page.locator(".footer")
#     await footer.scroll_into_view_if_needed()
#     await async_page.wait_for_timeout(5000)
#     await expect(footer).to_be_visible()

# @pytest.mark.asyncio
# async def test_scroll(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     # await async_page.mouse.wheel(0,500)
#     # await async_page.wait_for_timeout(5000)
#     # await async_page.mouse.wheel(0, -500)
#     # await async_page.wait_for_timeout(5000)
#     await async_page.evaluate("window.scrollTo(0,1000)")
#     await async_page.evaluate("window.scrollTo(0,document.body.scrollHeight)")

# @pytest.mark.asyncio
# async def test_scroll_infinite(async_page):
#     await async_page.goto("https://www.playwrightautomation.com/infinite-scroll.html")
#     loading = async_page.get_by_text("Loading more books…").first
#     end_of_catalog = async_page.locator("#end-of-catalog")

#     scroll = async_page.locator("#scroll-sentinel")

#     while True:
#         await scroll.scroll_into_view_if_needed()
#         print("scroll again")
#         await async_page.wait_for_timeout(5000)
#         #expect(end_of_catalog).to_be_visible() # stop
#         if await end_of_catalog.is_visible():
#             print("scroll till end")
#             break
#..........................................................................................................................................
#slider - price range 
#using keybord action to move the slider - timeout error 

# import pytest

# from playwright.async_api import expect
# @pytest.mark.asyncio
# #
# async def test_slider(async_page):
#     await async_page.goto("https://jqueryui.com/slider/#range")
#     frame = async_page.frame_locator(".demo-frame")
#     slider = frame.locator("#slider-range")
#     min = slider.nth(0)
#     max = slider.nth(1)
#     await async_page.wait_for_timeout(5000)
#     await min.click()
#     await min.press("Home")
#     for i in range(20):
#         await min.press("ArrowRight")
#         await async_page.wait_for_timeout(2000)
#     await max.click()
#     await max.press("End")
#     for i in range(20):
#         await min.press("ArrowLeft")
#         await async_page.wait_for_timeout(2000)
        
#..........................................................................................................................................
#date picker 

import pytest
from playwright.async_api import expect

# @pytest.mark.asyncio
# async def test_date_picker(async_page):
#     await async_page.goto("https://jqueryui.com/datepicker/")
#     frame = async_page.frame_locator(".demo-frame")
#     date_input = frame.locator("#datepicker")
#     await date_input.fill("15/09/2026")
#     # await date_input.press("Enter")
#     await async_page.wait_for_timeout(5000)
    
@pytest.mark.asyncio
async def test_date_picker(async_page):
    await async_page.goto("https://jqueryui.com/datepicker/")
    frame = async_page.frame_locator(".demo-frame")
    date_input = frame.locator("#datepicker")
    await date_input.click()

    user_month = "December"
    user_year = "2026"
    user_day = "29"
    while True:
        cm =await frame.locator(".ui-datepicker-month").inner_text()
        cy = await frame.locator(".ui-datepicker-year").inner_text()
        if cm == user_month and cy == user_year:
            break

        next = frame.locator(".ui-datepicker-next")
        await next.click()
    # await frame.get_by_text(user_day).click()
    # await async_page.wait_for_timeout(5000)    
    day = frame.locator("//td[@data-handler='selectDay']").filter(has_text=user_day).first
    await day.click()

