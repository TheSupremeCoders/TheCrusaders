from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# Launch the browser
driver = webdriver.Chrome()

# Navigate to the website and wait until it's fully loaded
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 40)

try:
    wait.until(EC.presence_of_element_located((By.ID, "wa-popovers-bucket")))
except TimeoutException:
    print("Timed out waiting for page to load")

# Get the cookies
cookies = driver.get_cookies()

# Store the cookies in a file for reuse
with open('cookies.txt', 'w') as f:
    f.write(str(cookies))

# Close the browser
driver.quit()
