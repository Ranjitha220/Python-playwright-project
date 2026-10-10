#Amazon – Search Results
import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_selection(async_page):
        await async_page.goto("https://www.amazon.in/")
        
        search_box= async_page.locator("#twotabsearchtextbox")
        
        await search_box.fill("book")
        await async_page.wait_for_timeout(5000)
        suggestions = async_page.locator('(//div[@class="s-suggestion s-suggestion-ellipsis-direction"])[1]')
        await suggestions.click()
        book = async_page.locator("(//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal'])[1]")
        name = await book.inner_text()
        print("Product Name:", name)
        async_page.locator("(//input[@name='submit.addToCart'])[1]")