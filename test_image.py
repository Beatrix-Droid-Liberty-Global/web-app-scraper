from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

import logging
# create the logging configuration
logging.basicConfig(level=logging.INFO,  format='%(asctime)s :: %(levelname)s :: %(message)s')

# configure the browser driver
options = FirefoxOptions()
options.add_argument("start-maximized")
options.binary = FirefoxBinary("/usr/bin/firefox")   
options.add_argument("--headless")

#firefox_service = FirefoxService(GeckoDriverManager().install())

logging.info("configured the browser")
# initialise an instance of the browser
browser = webdriver.Firefox(options=options)#service=firefox_service, options=options)
sleep(2)


logging.info("trying to open docker image web app")
browser.get("https://opulent-funicular-r4gpr79wwwgg3pxq-99.app.github.dev:99")

page_has_loaded=browser.find_elements(By.TAG_NAME,"label")

text=[label.text for label in page_has_loaded]
print(text)
if not page_has_loaded:
        browser.save_full_page_screenshot("home_page_not_found.png")
        logging.error("homepage not loaded correctly, exiting script")
        browser.quit()
        quit()
else:
    logging.info("image built successfully, pushing it to the docker registry")