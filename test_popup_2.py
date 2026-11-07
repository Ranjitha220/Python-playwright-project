import pytest
from playwright.async_api import expect
from pathlib import Path

# File_downloads

@pytest.mark.asyncio
async def test_download(async_page):
    await async_page.goto("https://the-internet.herokuapp.com/download")
    async_page.wait_for_timeout(3000)
    download_folder = Path("downloads")
    download_folder.mkdir(
        exist_ok=True
    )
    download_link = async_page.get_by_text("app.js")
    async with async_page.expect_download() as download_info:
        await download_link.click()
    download = await download_info.value
    file_name = download.suggested_filename
    file_path = download_folder / file_name
    await download.save_as(
        str(file_path)
    )
    print("Downloaded:", file_path)
    assert file_path.exists()
    
    
@pytest.mark.asyncio
async def test_download(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    ele =  async_page.locator("(//a[contains(text(),'Computers')])[1]")
    await ele.hover()
    ele1 = async_page.locator("(//a[contains(text(),'Desktops')])[1]")
    await expect(ele1).to_be_visible()
    ele1.click()
    print(await async_page.title())
    async_page.wait_for_timeout(5000)
    
@pytest.mark.asyncio
async def test_download(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")
    button = async_page.get_by_text("Copy Text")
    await button.dblclick()
    ele = async_page.locator("#field2")
    print(await ele.input_value())
    
@pytest.mark.asyncio
async def test_double_click(async_page):
    await async_page.goto("https://demo.guru99.com/test/drag_drop.html")
    se =  async_page.locator("(//a[@class='button button-orange'])[5]")
    te = async_page.locator("(//li[@class='placeholder'])[1]")
    await se.drag_to(te)
    
@pytest.mark.asyncio
async def test_double_click(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")
    button =  async_page.get_by_text("Copy Text")
    await button.dblclick()
    ele = async_page.locator("#field2")
    print(await ele.input_value())
    
@pytest.mark.asyncio
async def test_download(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    ele =  async_page.locator("(//a[contains(text(),'Computers')])[1]")
    await ele.hover()
    ele1 = async_page.locator("(//a[contains(text(),'Desktops')])[1]")
    await expect(ele1).to_be_visible()
    ele1.click()
    print(await async_page.title())
    async_page.wait_for_timeout(5000)
    
@pytest.mark.asyncio
async def test_double_click(async_page):
    await async_page.goto("https://demo.guru99.com/test/drag_drop.html")
    se =  async_page.locator("(//a[@class='button button-orange'])[5]")
    te = async_page.locator("(//li[@class='placeholder'])[1]")
    await se.drag_to(te)


@pytest.mark.asyncio
async def test_double_click(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")
    button =  async_page.get_by_text("Copy Text")
    await button.dblclick()
    ele = async_page.locator("#field2")
    print(await ele.input_value())

@pytest.mark.asyncio
async def test_download(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    ele =  async_page.locator("(//a[contains(text(),'Computers')])[1]")
    await ele.hover()
    ele1 = async_page.locator("(//a[contains(text(),'Desktops')])[1]")
    await expect(ele1).to_be_visible()
    ele1.click()
    print(await async_page.title())
    async_page.wait_for_timeout(5000)
    