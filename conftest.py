from playwright.async_api import async_playwright
import pytest_asyncio

@pytest_asyncio.fixture
async def async_page():
<<<<<<< HEAD
   async with async_playwright() as p:
       browser = await p.chromium.launch(headless=False)
       page = await browser.new_page()
       yield page # act as a generator operator
       await browser.close()




            
=======
    async with async_playwright() as p:
        browser =  await p.chromium.launch(headless = False)
        page = await browser.new_page()
        yield page
        await browser.close()
        #python -m pip install pytest_asyncio
        #python -m --fixture
>>>>>>> 2854a53 (testsupdate)
