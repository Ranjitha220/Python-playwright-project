import pytest 
from playwright.async_api import expect 

async def handle_alerts(dialog ):
    print("alert type = " , dialog.type)
    print("alter msg", dialog.message)
    await dialog.accept()
    
#Simple alert,confirm alert,prompt alert  

@pytest.mark.asyncio
async def test_alerts(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    #lamda arg : exp
    # page.on( lamda dialog : handle_alerts(dialog) )
    async_page.on("dialog",lambda dialog :  handle_alerts(dialog))
    await async_page.locator("//input[@type='submit']").click()
    await async_page.locator("#small-searchterms").fill("abc")

async def handle_confirm_alerts(dialog ):
    print("alert type = " , dialog.type)
    print("alter msg", dialog.message)
    await dialog.dismiss()  
    
@pytest.mark.asyncio
async def test_confirm_alert(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")
    await async_page.locator("#confirmBtn").click()
    async_page.on("dialog", lambda dialog: handle_confirm_alerts(dialog))
    
async def handle_confirm_alerts(dialog ):
    print("alert type = " , dialog.type)
    print("alter msg", dialog.message)
    await dialog.accept("Abc")   
    
@pytest.mark.asyncio
async def handle_prompt_alert(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")
    await async_page.locator("#promptBtn").click()
    async_page.on("dialog", lambda dialog: handle_prompt_alert(dialog))
    msg = async_page.locator("#demo")
    print(msg.inner_text())
    expect(msg).to_have_text("Hello Harry Potter! How are you today?")
 
#checkbox and radio button   
@pytest.mark.asyncio
async def test_checkbox(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")
    check_boxes = await async_page.locator("//label[text()='Days:']/..//input[@type='checkbox']").all()
    for check_box in check_boxes:
        await check_box.click()
        
    # check_box = async_page.locator("#sunday")
    # await expect(check_box).not_to_be_checked()
    # await check_box.check()
    # await expect(check_box).to_be_checked()
   
@pytest.mark.asyncio
async def test_radio_button(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")
    radio_buttons = await async_page.locator("//label[text()='Gender:']/..//input[@class='form-check-input']").all()
    for radio in radio_buttons:
        await radio.click() 
        await expect(radio).to_be_checked()
        

       