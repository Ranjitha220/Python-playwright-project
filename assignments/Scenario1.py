#DemoWebShop – Product Name to Add to Cart

from playwright.sync_api import sync_playwright, expect


def test_scenario_1():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open DemoWebShop
        page.goto("https://demowebshop.tricentis.com/")

        # Navigate to Books
        page.get_by_role("link", name="Books").first.click()

        # Product name
        product_name = "Computing and Internet"

        # Dynamic XPath based on product name
        product = page.locator(f"//h2/a[normalize-space()='{product_name}']")

        # Locate the product container
        product_container = product.locator("xpath=ancestor::div[contains(@class,'product-item')]")

        # Click Add to Cart for that product
        product_container.get_by_role("button",name="Add to cart").click()

         # Navigate to the cart 
        page.locator("xpath=//*[@id='topcartlink']/a/span[1]").click()
           
        # Verify the product is listed in the cart
        cart_product = page.locator(f"xpath=//tr[contains(@class, 'cart-item-row')]//a[@class='product-name' and normalize-space()='{product_name}']")
        expect(cart_product).to_be_visible()