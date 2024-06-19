from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

from setting import *
import time

if __name__ == '__main__':
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": r"/Users/tanjunjie/Documents/Forms 365",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    browser = webdriver.Chrome(options=chrome_options)
    #   Remove Navigator.Webdriver Flag
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })
    # Set the timeout time
    browser.set_page_load_timeout(30)
    try:
        # visit Microsoft Forms URL
        web_link = 'https://forms.office.com/Pages/DesignPageV2.aspx?origin=NeoPortalPage&subpage=design&id=_WpaRngYPE67n3s3iakZfkkVD8aC8MFOqpPDdUTrZJpUQkZVSENBNEVONFdPMDJLRFdRT1I4Wk9IVy4u&#39';
        browser.get(web_link)

        #Maximize the browser window
        browser.maximize_window()
        time.sleep(5)

        # Locate the iframe, here we use the id attribute to locate
        iframe_element = browser.find_element(By.ID, "hrdIframe")

        #  Switch to iframe
        browser.switch_to.frame(iframe_element)
        # Click the email input box to enter the email
        email_input = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Email, phone, or Skype']")
        email_input.send_keys(Email_input)

        # Wait for a while to let the form process the input data
        WebDriverWait(browser, 30).until(lambda d: d.execute_script("return document.readyState;") == "complete")

        # Click the next button
        browser.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div[4]/input').click()
        time.sleep(4)

        browser.switch_to.default_content()

        password_input = browser.find_element(By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input')

        password_input.send_keys(Password_input)
        time.sleep(2)

        # click the login button
        login_button = browser.find_element(By.ID, "idSIButton9")
        login_button.click()
        time.sleep(3)

        # stay signed in
        login_button = browser.find_element(By.ID, "idSIButton9")
        login_button.click()
        time.sleep(3)

        # reponse tab
        login_button = browser.find_element(By.XPATH, '//div[@role="tab" and @aria-label="Responses Received 8 responses"]')
        login_button.click()
        time.sleep(3)

        # download the excel file
        download_link = browser.find_element(By.XPATH, "//span[text()='Download a copy in Excel']")
        download_link.click()
        time.sleep(5)



    except TimeoutException:
        print("Timeout waiting for page to load")

    finally:
        # Close the browser
        browser.quit()
