
from playwright.async_api._generated import Browser
import pytest
from playwright.async_api import async_playwright, expect

# @pytest.mark.asyncio
# async def test_multi_page(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     #_________________________________________________---
#     #    Items
#     #-----------------------------------------------------
#     item = "Books"
#     locator_item = async_page.locator(f"(//a[contains(text(),'{item}')])[3]")
#     await expect(locator_item).to_be_visible()
#     await locator_item.click()
#     # validate :-- books
#     books_page = async_page.locator("//h1[text()='Books']")
#     try:
#         expect(books_page).to_be_visible()
#         print("user naviagte to Books page")
#     except Exception as e:
#         print("user not naviagte to Books page")

#     # ---------------------------------------------
#     #   collect all products
#     #------------------------------------------------
#     products = ["Computing and Internet","Fiction","Health Book"]
#     for i in products:
#         book = async_page.locator(f"//a[text()='{i}']/../..//input[@value='Add to cart']")
#         await expect(book).to_be_visible()
#         await book.click()
#         await async_page.wait_for_timeout(2000)
#     count_of_cart = await async_page.locator("//span[text()='(3)']").inner_text()
#     try:
#         assert count_of_cart == len(products)
#         print(count_of_cart , "add to cart")
#     except Exception as e:
#         print(products , "not add to cart")
#     await async_page.wait_for_timeout(2000)

#     ############===-----------------------------
#     # click on the add to cart
#     # --------------------------------------------------

#     add_to_cart = async_page.locator("//span[text()='Shopping cart']")
#     await expect(add_to_cart).to_be_visible()
#     await add_to_cart.click()

#     product_in_cart = await async_page.locator("//td[@class='product']/a").all_text_contents()
#     try:
#         assert product_in_cart == products
#         print(add_to_cart , "add to cart")
#     except Exception as e:
#         print(add_to_cart, "not in add to cart")
        
        
# @pytest.mark.asyncio
# async def test_multi_step_form(async_page):
#     await async_page.goto("https://demoqa.com/automation-practice-form")
#     fn  =  async_page.locator("//input[@id='firstName']")
#     await fn.fill("abc")
#     ln = async_page.locator("#lastName")
#     await ln.fill("a")
#     email = async_page.locator("#userEmail")
#     await email.fill("abc@gmail.com")
#     g = async_page.locator("#gender-radio-1")
#     await g.click()
#     ph = async_page.locator("#userNumber")
#     await ph.fill("1234567899")
#     # date = async_page.locator("#dateOfBirthInput")
#     # await date.clear()
#     # await date.click()
#     # date_ = async_page.locator("//div[text()='9']")
#     # await date_.click()
#     # sub = async_page.locator("//div[@class='subjects-auto-complete__input-container css-19bb58m']")
#     # await sub.fill("abc")

#     assert await fn.input_value() == "abc"
#     assert await ln.input_value() == "a"
#     assert await email.input_value() == "abc@gmail.com"
#     await expect(g).to_be_checked()
#     assert await ph.input_value() == "1234567899"
#     # assert await date.input_value() == "09 Oct 2026"
#     # assert await sub.input_value() == "abc"
#     submit = async_page.locator("//button[@id='submit']")
#     await submit.click()
    
    
# @pytest.mark.asyncio
# async def test_auth_form(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     await async_page.get_by_text("Log in").click()
#     await async_page.locator("#Email").fill("abcnew1234@gmail.com")
#     await async_page.locator("#Password").fill("123456789")
#     await async_page.locator("//input[@value='Log in']").click()
#     try:
#         async_page.get_by_text("Log out")
#     except Exception as e:
#         print("user not login")
#     #auth.josn
#     await async_page.context.storage_state(
#         path="auth.json"
#     )


# @pytest.mark.asyncio
# async def test_store_stage(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     await async_page.get_by_text("Log in").click()
#     await async_page.locator("#Email").fill("abcnew1234@gmail.com")
#     await async_page.locator("#Password").fill("123456789")
#     await async_page.locator("//input[@value='Log in']").click()
#     try:
#         async_page.get_by_text("Log out")
#     except Exception as e:
#         print("user not login")
#     #auth.josn
#     await async_page.context.storage_state(
#         path="session.json"
#     )

# @pytest.mark.asyncio
# async def test_restore_session():
#     async with async_playwright() as p:
#     Browser = await p.chromium.launch(headless=False)
#     context = await Browser.new_context(storage_state="session.json")
#     page = await context.new_page()
#     await page.goto("https://demowebshop.tricentis.com/")
#     await page.wait_for_timeout(5000)
    
    
    
@pytest.mark.asyncio
async def test_api_data_validation(async_page):
    Base_url = "https://parabank.parasoft.com/parabank"
    end_point = "register.htm"
    username = "Ranju"
    password = "abc@123"
    await async_page.goto(Base_url+"/"+end_point)

    await async_page.locator("#customer\\.firstName").fill("Ranjitha")
    await async_page.locator("#customer\\.lastName").fill("D")
    await async_page.locator("#customer\\.address\\.street").fill(
        "100 Test Street"
    )
    await async_page.locator("#customer\\.address\\.city").fill(
        "Bengaluru"
    )
    await async_page.locator("#customer\\.address\\.state").fill(
        "Karnataka"
    )
    await async_page.locator("#customer\\.address\\.zipCode").fill(
        "560068"
    )
    await async_page.locator("#customer\\.phoneNumber").fill(
        "8073368401"
    )
    await async_page.locator("#customer\\.ssn").fill("123456789")
    await async_page.locator("#customer\\.username").fill(username)
    await async_page.locator("#customer\\.password").fill(password)
    await async_page.locator("#repeatedPassword").fill(password)

    await async_page.locator("input[value='Register']").click()

    # Verify registration result
    await expect(
        async_page.locator("#rightPanel")
    ).to_contain_text("successfully", ignore_case=True)

    print("Customer registered:", username)