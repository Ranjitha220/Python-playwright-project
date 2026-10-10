# DemoWebShop – Multiple Products
def test_get_options(page):
    page.goto("https://demowebshop.tricentis.com/", wait_until='domcontentloaded')
    page.locator("(//a[contains(text(), 'Books')])[3]").click()
    
    
    products_locators = page.locator("//h2[@class='product-title']")
    print("products list", products_locators.all_inner_texts())
    
    product_list = ["Computing and Internet", "Fiction", "Health Book", "Science"]
    
    for i in product_list:

        add_to_cart_btn = page.locator(f"//a[text()='{i}']/../..//input[@value='Add to cart']")
        
        # Identify the Add to Cart button for each product.
        if add_to_cart_btn.count() > 0:
        
            add_to_cart_btn.click()
            print(f"'{i}' added to cart.")
            page.wait_for_timeout(2000) 
        else:
            
            print(f"No Add to Cart button found for '{i}' ")