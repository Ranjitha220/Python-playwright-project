
#DemoWebShop – Select Product by Price
def test_cart(page):
    page.goto("https://demowebshop.tricentis.com/")
    product=page.locator("xpath=//ul[@class='top-menu']//a[contains ( text(), 'Books')]")
    product.click()
    
    price="10.00"
  
    product = page.locator("//h2/a[normalize-space()='Computing and Internet']")

    product_container = product.locator(
    "xpath=ancestor::div[contains(@class,'product-item')]")

    product_container.locator('input[value="Add to cart"]').click()
    page.wait_for_timeout(5000)
    
    # Navigate to the cart 
    page.locator("xpath=//*[@id='topcartlink']/a/span[1]").click()
    page.wait_for_timeout(5000)
   
   
    