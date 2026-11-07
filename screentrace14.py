#Screenshots store in photos folder 

# from playwright.async_api import expect
# import pytest
# from pathlib import Path

# PHOTO_DIR = Path("Photos")
# PHOTO_DIR.mkdir(parents=True, exist_ok=True)

# @pytest.mark.asyncio
# async def test_sc(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     products = async_page.locator(".product-title")
#     simple_comp = products.filter(has_text="Simple Computer")
#     await simple_comp.first.click()
#     ele = async_page.locator("//h1[@itemprop='name']")
#     await expect(ele).to_be_visible()
#     await async_page.screenshot(path=str(PHOTO_DIR / "Simple Computer.png"),full_page=True)
    

#Run - codegen 
#playwright codegen --target python-async https://demowebshop.tricentis.com/
#playwright codegen --target python-async https://demowebshop.tricentis.com/ -o democodegentest.py


#.....................................................................................................................
#Trace


from pathlib import Path
from playwright.async_api import expect
import pytest
from pathlib import Path
TRACE_DIR = Path("tracing1")
TRACE_DIR.mkdir(parents=True, exist_ok=True)
@pytest.mark.asyncio
async def test_sc(async_page):
    await  async_page.context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )
    await async_page.goto("https://demowebshop.tricentis.com/")
    products = async_page.locator(".product-title")
    simple_comp = products.filter(has_text="Simple Computer")
    await simple_comp.first.click()
    ele = async_page.locator("//h1[@itemprop='name']")
    await expect(ele).to_be_visible()
    await async_page.context.tracing.stop(path = str(TRACE_DIR/"trace1.zip"))
    
    
    #url > https://trace.playwright.dev > select trace file from folder 
    
    
