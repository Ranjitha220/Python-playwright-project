#  Transfer Funds & Verify Transaction

def test_refund(page):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    page.locator("//input[@name='username']").fill("ranju123")
    page.locator("//input[@name='password']").fill("123456")

    page.locator("//input[@value='Log In']").click()
    page.wait_for_timeout(5000)

    new_account= page.locator("//a[text()='Accounts Overview']")
    new_account.click()
    # all available account numbers
    all_accounts = page.locator("#accountTable tbody tr td:first-child a").all_text_contents()

    # print only  account numbers
    account1 = all_accounts[0].strip()
    account2 = all_accounts[1].strip()

    print("Account number 1:", account1)
    print("Account number 2:", account2)
    page.wait_for_timeout(2000)

    #Transfer fund
    transfer_fund = page.locator("//a[text()='Transfer Funds']")
    transfer_fund.click()
    page.wait_for_timeout(2000)
    
    #Enter amount
    amount = page.locator("//*[@id='amount']")
    amount.fill("50")
    page.wait_for_timeout(2000)

    # Select accounts
    page.locator("//*[@id='fromAccountId']").select_option("14343")
    page.locator("//*[@id='toAccountId']").select_option("14565")
    
    transfer= page.locator("//input[@value='Transfer']")
    transfer.click()
    page.wait_for_timeout(5000)

    #verify the amount trasferd

    page.locator("//*[@id='showResult']").wait_for(state="visible")
    
    title_text = page.locator("//*[@id='showResult']/h1").inner_text()
    amount = page.locator("//*[@id='amountResult']  ").inner_text()
    from_acc = page.locator("//*[@id='fromAccountIdResult']").inner_text()
    to_acc = page.locator("//*[@id='toAccountIdResult']").inner_text()
    
    print(f"Status: {title_text}")
    print(f"Amount Transferred: {amount}")
    print(f"From Account: #{from_acc}")
    print(f"To Account: #{to_acc}")

    #navigate to toaccount

    page.locator("//a[text()='Accounts Overview']").click()
    page.wait_for_timeout(2000)
    page.locator("//a[text()='14343']").click()
    page.wait_for_timeout(2000)
    transfer= page.locator("//input[@value='Transfer']")
    transfer.click()
    page.wait_for_timeout(5000)

    #verify the amount trasferd

    page.locator("//*[@id='showResult']").wait_for(state="visible")
    
    title_text = page.locator("//*[@id='showResult']/h1").inner_text()
    amount = page.locator("//*[@id='amountResult']  ").inner_text()
    from_acc = page.locator("//*[@id='fromAccountIdResult']").inner_text()
    to_acc = page.locator("//*[@id='toAccountIdResult']").inner_text()
    
    print(f"Status: {title_text}")
    print(f"Amount Transferred: {amount}")
    print(f"From Account: #{from_acc}")
    print(f"To Account: #{to_acc}")

    #navigate to account

    page.locator("//a[text()='Accounts Overview']").click()
    page.wait_for_timeout(2000)
    page.locator("//a[text()='18651']").click()
    page.wait_for_timeout(2000)
