#Amazon – Select Product from Search Results

def test_amazon_relative_xpath(page):
    page.goto("https://www.amazon.in/")

    # 1. Search
    search_box = page.locator("//input[@id='twotabsearchtextbox']")
    search_box.click()
    search_box.fill("books")
    search_box.press("Enter")
    page.wait_for_load_state("domcontentloaded")

    # 2. Product card
    product_card = page.locator("//div[@data-component-type='s-search-result'][.//span[normalize-space()='The Psychology of Money']]").first
    product_card.wait_for(state="visible")

    # 3. Image
    print("image src:", product_card.locator("xpath=.//img").first.get_attribute("src"))

    # 4. Price
    price = product_card.locator("xpath=.//span[@class='a-price-whole']").first
    print("product price:", price.inner_text().strip())

    
    product_link = product_card.locator("xpath=.//a[.//h2]").first
    href = product_link.get_attribute("href")
   
    if href and href.startswith("/"):
        href = "https://www.amazon.in" + href
    print("Navigating to:", href)
    page.goto(href)


    product_name = page.locator("//span[@id='productTitle']")
    product_name.wait_for(state="visible", timeout=15000)
    print(f"Detail Page Title: {product_name.inner_text().strip()}")