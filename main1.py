from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import pytz
import time

tz = pytz.timezone('US/Pacific') # Replace US/Pacific with your timezone

options = Options()
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-extensions')
# options.add_argument('--headless') # If you want to run Chrome in headless mode

driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd('Emulation.setTimezoneOverride', {'timezoneId': 'US/Pacific'})
driver.get('https://leetcode.com/manish123rajput/') # Replace example.com with the website you want to visit
time.sleep(50) # Wait for 5 seconds to let the page load
driver.quit()
