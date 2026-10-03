import pytest 

async def handle_alerts(dialog ):
    print("alert type = " , dialog.type)
    print("alter msg", dialog.message)
    await dialog.accept
    
@pytest.mark.asyncio
async def test_alerts(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    #lamda arg : exp
    # page.on( lamda dialog : handle_alerts(dialog) )
    async_page.on("dialog",lambda dialog :  handle_alerts(dialog))
    await async_page.locator("//input[@type='submit']").click()
    await async_page.locator("#small-searchterms").fill("abc")
    
