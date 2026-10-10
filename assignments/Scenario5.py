#DemoWebShop – Product Name and Rating

def test_rating(page):
    # Open DemoWebShop
    page.goto("https://demowebshop.tricentis.com/")

    # Navigate to Computers category
    category = page.locator("//div[contains(@class,'block-category-navigation')]""//a[normalize-space()='Computers']")
    category.click()

    # Select Desktops category
    product_category = page.locator("//div[contains(@class,'sub-category-grid')]""//h2/a[normalize-space()='Desktops']")
    product_category.click()

    # Select the product by name
    choose_product = page.locator("//div[contains(@class,'product-grid')]""//h2/a[contains(normalize-space(),'Build your own cheap computer')]")
    choose_product.click()

    product_details = page.locator("//div[contains(@class,'product-essential')]")

    # Get the product name 
    product_name = product_details.locator("xpath=.//div[contains(@class,'product-name')]//h1")

    # Get the rating link 
    rating_locator = page.locator("//div[contains(@class,'product-review-links')]/a").first

    # Print product name and rating
    print("Product Name:", product_name.inner_text().strip())
    print("Rating:", rating_locator.inner_text().strip())

    page.wait_for_timeout(3000)

