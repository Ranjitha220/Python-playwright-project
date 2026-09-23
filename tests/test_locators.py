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
    
def test_get_by_text(page):
    page.goto("https://www.facebook.com")
    login_to_facebook_text = page.get_by_text("Log in to Facebook")
    expect(login_to_facebook_text).to_be_visible()
    forgot_password_button = page.get_by_text("Forgotten password")
    forgot_password_button.click()
    page.wait_for_timeout(1000)
    

def test_get_by_label(page):
    page.goto("https://demowebshop.tricentis.com/")
    register_link = page.get_by_text("Register")
    register_link.click()
    page.get_by_label("Male").nth(0).check()
    page.get_by_label("First name:").fill("ranju")
    page.get_by_label("Last name:").fill("d")
    page.get_by_label("Email:").fill("ranji@gmail.com")
    page.get_by_label("Password:").nth(0).fill("ranji123")
    page.wait_for_timeout(1000)

def test_get_by_placeholder(page):
    page.goto("https://www.amazon.in/")
    page.wait_for_timeout(10)
    page.get_by_placeholder("Search Amazon.in").fill("mobiles")
    page.wait_for_timeout(10)
    page.keyboard.press("Enter")
    page.wait_for_timeout(10)


def test_get_by_alt_text(page):
    page.goto("https://demowebshop.tricentis.com/")
    logo = page.get_by_alt_text("Tricentis Demo Web Shop")
    expect(logo).to_be_visible()

def test_get_by_title(page):
    page.goto("https://demowebshop.tricentis.com/")
    logo = page.get_by_title("Tricentis Demo Web Shop")
    logo.click()
    
    
def test_get_by_test_id(page):
    page.goto("https://demowebshop.tricentis.com/")
    page.wait_for_timeout(1000)
    logo = page.get_by_test_id("Tricentis Demo Web Shop")
    logo.click()
    expect(logo).to_be_visible()
    

