import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://demowebshop.tricentis.com/")
    await page.get_by_role("link", name="Books").nth(1).click()
    await page.locator("#small-searchterms").click()
    await page.locator("#small-searchterms").fill("computers")
    await page.locator("#small-searchterms").press("Enter")
    await page.locator("#small-searchterms").click()
    await page.get_by_role("link", name="Computers").nth(1).click()
    await page.locator("#small-searchterms").click()
    await page.locator("#small-searchterms").fill("mobiles")
    await page.locator("#small-searchterms").press("Enter")
    await page.get_by_role("link", name="Jewelry").nth(1).click()
    await page.get_by_role("button", name="Add to cart").nth(1).click()
    await page.get_by_text("The product has been added to").click()
    await page.get_by_text("The product has been added to").click()
    await page.get_by_role("link", name="Shopping cart (1)").click()
    await page.locator("input[name=\"removefromcart\"]").check()
    await page.locator("#termsofservice").check()

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
