import pytest

@pytest.mark.asyncio
# async def test_dropdowns(async_page):
#     await async_page.goto("https://www.amazon.in/")
#     search_box = async_page.locator("#twotabsearchtextbox")
#     await search_box.fill("books")
    
#  #dynamic drop down
#     lists= async_page.locator("//div[@class='s-suggestion s-suggestion-ellipsis-direction']")
  
#   #list all suggesion
#     await lists.first.wait_for()
  
#   #print the no of lists
#     count=await lists.count()
#     print("Total lists: ", count)
  
#   #print lists using with index
  
#     for i in range(count):
#      text= await lists.nth(i).inner_text()  
#      print(f"{i} : {text}")
      
#     await async_page.get_by_text("helf for home").click()  
#...............................................................    
async def test_drop(async_page):
  await async_page.goto("https://www.amazon.in/")
  drop_down= async_page.locator("#searchDropdownBox")
    
    #select index
  await drop_down.select_option(index=5)

#select by value

  await drop_down.select_option(value="search-alias=baby")
  
  #select by label
  await drop_down.select_option(label="Electronics")
##...........................................................
#  async def test_drop(async_page):
#     await async_page.goto("https://www.amazon.in/")

#     search_box = async_page.locator("#twotabsearchtextbox")
#     await search_box.fill("books")

#     lists = async_page.locator("//div[@class='s-suggestion s-suggestion-ellipsis-direction']")

#     await lists.first.wait_for()

#     options = await lists.all_inner_texts()
#     options.sort(key=str.lower)

#     expected_text = options[3]

    
#     suggestion = lists.filter(has_text=expected_text).first

#     await suggestion.click()

#     act = await search_box.input_value()

#     assert act.lower() == expected_text.lower()