# import  pytest
# @pytest.mark.asyncio
# async def test_dropdowns(async_page):
#     await async_page.goto("https://www.amazon.in/")
#     drop_down = async_page.locator("#searchDropdownBox")
#     #selct by index
#     await drop_down.select_option(index=5)
#     #select by value
#     await drop_down.select_option(value="search-alias=baby")
#     #select by label
#     await drop_down.select_option(label="Electronics")

#========================================================================

# import pytest
# from playwright.async_api import Page


# @pytest.mark.asyncio
# async def test_drop_down(async_page: Page):
#     await async_page.goto("https://www.amazon.in/")

#     search_box = async_page.locator("#twotabsearchtextbox")
#     await search_box.fill("books")

#     # Dynamic dropdown suggestions
#     suggestions = async_page.locator(
#         "div.s-suggestion.s-suggestion-ellipsis-direction"
#     )

#     # Wait for at least one suggestion
#     await suggestions.first.wait_for(state="visible")

#     count = await suggestions.count()
#     print("Total number of options =", count)

#     # Print all suggestions with index
#     for i in range(count):
#         text = await suggestions.nth(i).inner_text()
#         print(f"{i}: {text}")

    
#     await async_page.get_by_text("for kids 9-12 years").click()
#     await async_page.wait_for_timeout(2000)
#========================================================================
# import pytest
# from playwright.async_api import Page
# @pytest.mark.asyncio
# async def test_drop_downs_select_with_keybord(async_page):
#     await async_page.goto("https://www.amazon.in/")
#     search_box = async_page.locator("#twotabsearchtextbox")
#     await search_box.fill("books")
#     await async_page.wait_for_timeout(2000)

#     await search_box.press("ArrowDown")
#     await search_box.press("ArrowDown")
#     await search_box.press("ArrowDown")
#     await search_box.press("Enter")
#     await async_page.wait_for_timeout(2000)


#====================================================================================================

                
#========================================================================

import pytest

@pytest.mark.asyncio
async def test_drop_downs_select_with_sorted(async_page):
    await async_page.goto("https://www.amazon.in/")

    search_box = async_page.locator("#twotabsearchtextbox")
    await search_box.fill("books")

    # Wait for suggestions
    suggestions = async_page.locator(
        "//div[@class='s-suggestion s-suggestion-ellipsis-direction']"
    )

    await suggestions.first.wait_for()

    # Get all suggestion texts
    options = await suggestions.all_inner_texts()

    # Sort alphabetically
    sorted_options = sorted(options, key=str.lower)

    # Select the 4th item (index 3)
    expected_text = sorted_options[3]

    count = await suggestions.count()

    for i in range(count):
        suggestion_text = await suggestions.nth(i).inner_text()

        if suggestion_text == expected_text:
            await suggestions.nth(i).click()
            break

    # Verify selected value
    assert (await search_box.input_value()).lower() == expected_text.lower()