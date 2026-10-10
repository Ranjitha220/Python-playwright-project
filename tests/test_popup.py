import pytest
from playwright.async_api import expect

##file upload 
   
# @pytest.mark.asyncio
# async def test_frm(async_page):
#    await async_page.goto("https://the-internet.herokuapp.com/upload")
#    file_input = async_page.locator("#file-upload")
#    await file_input.set_input_files("/home/user/Documents/DOB admin.odt")
#    await async_page.locator("#file-submit").click()
#    await async_page.wait_for_timeout(5000)
#    msg = async_page.get_by_text("File Uploaded!")
#    await expect(msg).to_be_visible()


##image popup
@pytest.mark.asyncio
async def test_frm(async_page):
    await async_page.goto("https://demo.guru99.com/test/guru99home/", wait_until="load")
    
    frame = async_page.frame_locator("#a077aa5e")
    
    img =  frame.locator("//img[@src='Jmeter720.png']")
    await expect(img).to_be_visible()
    await img.click()

    email =  async_page.get_by_placeholder("Enter Email")
    await expect(email).to_be_visible()
    await email.fill("abc@gmail.com")
    print(await email.input_value())    