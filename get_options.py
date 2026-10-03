##count method [multiple elements]   
# def test_get_options(page):
#     page.goto("https://demowebshop.tricentis.com/",wait_until="domcontentloaded")
#     #page.locator("(//a[contains(text(),'Books')])[3]").click()
#     page.locator("(//li[@class='inactive'])[1]/a").click()
#     products_locators = page.locator("//h2[@class='product-title']")
    
    
#     print("num of books =" , products_locators.count()) #get the no. of products
    
#     print("first book is",products_locators.nth(0).all_text_contents())
    
    #print("product list",products_locators.all_inner_texts()) #get all product text 
    
   ##products in the list with product names 
    # product_list = ["Computing and Internet","Fiction","Health Book"]
    # for i in product_list:
    #     product = page.locator(f"//a[text()='{i}']/../..//input[@value='Add to cart']")
    #     product.click()
        
def test_collecting_all_links(page):
    page.goto("https://www.amazon.com/",wait_until='domcontentloaded')
    links = page.locator("//a")
    for i in links.all():
        print("link" , i.get_attribute("href"),flush=True)
        
   
    links.last.click()
    links.first.click()
    links.nth(0).click()

     
   
    
    
