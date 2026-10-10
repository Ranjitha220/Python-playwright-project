# Amazon – Product Name and Price


def test_amazon (page):
    page.goto("https://www.amazon.in/")
    page.get_by_role("searchbox", name="Search Amazon.in").click()
    page.get_by_role("searchbox", name="Search Amazon.in").fill("books")
    page.get_by_role("searchbox", name="Search Amazon.in").press("Enter")
    page.wait_for_timeout(5000)
    
    product_name=page.locator("//div[contains(@class,'a-section a-spacing-small a-spacing-top-small')]/..//span[text()='The Psychology of Money']")

    print("product name:" , product_name.inner_text().strip())
    product_name.click()
    page.wait_for_timeout(5000)
    price=page.locator("xpath=//*[@id='corePriceDisplay_desktop_feature_div']/div/div[1]/span[3]/span[2]/span[2]")
    #print("product price:", price.inner_text())
    
   
   