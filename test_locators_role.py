# page.getByRole() to locate by explicit and implicit accessibility attributes.
# page.getByText() to locate by text content.
# page.getByLabel() to locate a form control by associated label's text.
# page.getByPlaceholder() to locate an input by placeholder.
# page.getByAltText() to locate an element, usually image, by its text alternative.
# page.getByTitle() to locate an element by its title attribute.
# page.getByTestId() to locate an element based on its data-testid attribute (other attributes can be configured).

from playwright.sync_api import expect

def test_locators_get_by_role(page):
     #register 
    page.goto("https://demowebshop.tricentis.com/")
    page.get_by_role("link", name="Register").click()
    page.get_by_role("radio", name="Female", exact=True).click()
    page.get_by_role("textbox", name="First name:").fill("ranjitha")
    page.get_by_role("textbox", name="Last name:").fill("d")
    page.get_by_role("textbox", name="Email").fill("abc@gmail.com")
    page.get_by_role("textbox", name="Confirm password:").fill("abc123")
    page.get_by_role("button", name="Register").click()
    page.wait_for_timeout(1000)
    
    #login
    page.goto("https://demowebshop.tricentis.com/")
    page.get_by_role("link", name="Log in").click()
    page.get_by_role("textbox", name="Email").fill("abc@gmail.com")
    page.get_by_role("textbox", name="Password").fill("abc123")
    page.get_by_role("button", name="Log in").click()
    page.wait_for_timeout(1000)
    

    






    

