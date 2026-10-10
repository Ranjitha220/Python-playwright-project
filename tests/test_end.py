#scrolling 
import pytest
@pytest.mark.asyncio
async def test_end_2_end(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    #_________________________________________________---
    #    Items
    #-----------------------------------------------------
    item = "Books"
    locator_item = async_page.locator(f"(//a[contains(text(),'{item}')])[3]")
    await expect(locator_item).to_be_visible()
    await locator_item.click()
    # ---------------------------------------------
    #   collect all products
    #------------------------------------------------
    products = ["Computing and Internet","Fiction","Health Book"]
    for i in products:
        book = async_page.locator(f"//a[text()='{i}']/../..//input[@value='Add to cart']")
        await expect(locator_product).to_be_visible()
        await book.click()
        await async_page.wait_for_timeout(2000)

    ############===-----------------------------
    # click on the add to cart
    # --------------------------------------------------

    add_to_cart = async_page.locator("//span[text()='Shopping cart']")
    await expect(add_to_cart).to_be_visible()
    await add_to_cart.click()

    terms_cond = async_page.locator("//input[@id='termsofservice']")
    await expect(terms_cond).to_be_visible()
    await terms_cond.click()

    check_out = async_page.locator("//button[@id='checkout']")
    await expect(check_out).to_be_visible()
    await check_out.click()

    reg = async_page.locator("//input[@value='Register']")
    await expect(reg).to_be_visible()
    await reg.click()
    #===================================================
    # = Reg
    #===================================================

    Female = async_page.get_by_text("Female")
    await expect(Female).to_be_visible()
    await Female.click()
    await async_page.get_by_label("First name:").fill("abc")
    await async_page.get_by_label("Last name:").fill("a")
    await async_page.get_by_label("Email:").fill("abcnew123@gmail.com")
    await async_page.get_by_label("Password:").fill("123456789")
    await async_page.get_by_label("Confirm password:").fill("123456789")
    await async_page.locator("#register-button")
    try:
        async_page.get_by_text("Log out")
    except Exception as e:
        print("user not reg")

    #======================================================
    #  order
    #=========================================================
    add_to_cart = async_page.locator("//span[text()='Shopping cart']")
    await expect(add_to_cart).to_be_visible()
    await add_to_cart.click()

    terms_cond = async_page.locator("//input[@id='termsofservice']")
    await expect(terms_cond).to_be_visible()
    await terms_cond.click()

    check_out = async_page.locator("//button[@id='checkout']")
    await expect(check_out).to_be_visible()
    await check_out.click()

    await async_page.locator("#BillingNewAddress_Company").fill("Demo")
    await async_page.locator("#BillingNewAddress_CountryId").select_text(label = "India")
    await async_page.locator("#BillingNewAddress_City").fill("Mysore")
    await async_page.locator("#BillingNewAddress_Address1").fill("Srinagar")
    await async_page.locator("#BillingNewAddress_Address2").fill("Srinagar")
    await async_page.locator("#BillingNewAddress_ZipPostalCode").fill("5056256")
    await async_page.locator("#BillingNewAddress_PhoneNumber").fill("123456789")
    await async_page.locator("#BillingNewAddress_FaxNumber").fill("12345")
    await async_page.locator("(//input[@title='Continue'])[1]").click()
    await async_page.wait_for_timeout("5000")
    await async_page.locator("#PickUpInStore").click()
    await async_page.locator("(//input[@title='Continue'])[2]").click()
    await async_page.wait_for_timeout("5000")
    await async_page.locator("#paymentmethod_0").click()
    await async_page.locator("(//input[@value='Continue'])[4]").click()
    await async_page.wait_for_timeout(2000)
    await async_page.locator("(//input[@value='Continue'])[5]

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
#     await async_page.mouse.wheel(0,500)
#     await async_page.wait_for_timeout(5000)
#     await async_page.mouse.wheel(0, -500)
#     await async_page.wait_for_timeout(5000)
    
# @pytest.mark.asyncio
# async def test_scroll(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     await async_page.mouse.wheel(0,500)
#     await async_page.wait_for_timeout(5000)
#     await async_page.mouse.wheel(0, -500)
#     await async_page.wait_for_timeout(5000)
#     # await async_page.evaluate("window.scrollTo(0,1000)")
#     await async_page.evaluate("window.scrollTo(0,document.body.scrollHeight)")
#     await async_page.wait_for_timeout(5000)
    
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
        
#     @pytest.mark.asyncio
#     async def test_date_picker(async_page):
#         await async_page.goto("https://jqueryui.com/datepicker/")
#         frame = async_page.frame_locator(".demo-frame")
#         date_input = frame.locator("#datepicker")
#         await date_input.fill("15/09/2026")
#         await date_input.press("Enter")
#         await async_page.wait_for_timeout(5000)
            
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
    await frame.get_by_text(user_day).click()
    await async_page.wait_for_timeout(5000)
    