#tables found in html tables 
def test_table(page):
    page.goto("https://www.w3schools.com/html/html_tables.asp")
    count_tables = page.locator("//table").count() #no. of tables present 
    print(count_tables,flush=True) #run - python -m pytest test_loc1.py --headed -s -v
    
