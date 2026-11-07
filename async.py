from playwright.async_api import async_playwright
import asyncio
async def run_async_demo():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)   
        page = await browser.new_page()
        page.goto("https://www.google.com")
        print("Async page title:", await page.title())
        await browser.close()
        
asyncio.run(run_async_demo())