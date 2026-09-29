def test_count_the_link(page):
    page.goto("https://demowebshop.tricentis.com/")
    links = page.locator("//a").all() #displays links in list 
    
    print(len(links)) #length of elements in the list 
    print(type(links))
    
    for i in links: #print link one by one 
        print(i.text_content()) #text of the link 
        
    print("*" * 50)
    
    for i in links:
        print(i.get_attribute("href")) #href of the attribute 
        
#Run ->  python -m pytest tables.py --headed -s -v
    
