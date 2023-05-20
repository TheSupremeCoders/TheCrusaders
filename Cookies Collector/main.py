from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


# Launch the browser
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://web.whatsapp.com/")

# Define the cookies as a list of dictionaries
cookies = [
    {
        "domain": ".whatsapp.com",
        "expirationDate": 1685710139.140026,
        "hostOnly": False,
        "httpOnly": True,
        "name": "wa_beta_version",
        "path": "/",
        "sameSite": "Lax",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "production%2F1683748333%2F2.2320.10",
        "id": 1
    },
    {
        "domain": ".whatsapp.com",
        "expirationDate": 1683920864,
        "hostOnly": False,
        "httpOnly": False,
        "name": "dpr",
        "path": "/",
        "sameSite": "Lax",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "1.25",
        "id": 2
    },
    {
        "domain": ".whatsapp.com",
        "expirationDate": 1683918874.194311,
        "hostOnly": False,
        "httpOnly": False,
        "name": "wa_lang_pref",
        "path": "/",
        "sameSite": "Lax",
        "secure": True,
        "session": False,
        "storeId": "0",
        "value": "en",
        "id": 3
    }
]

# Add the cookies to the browser
for cookie in cookies:
    driver.add_cookie(cookie)

# Refresh the page to use the cookies
driver.refresh()
wait = WebDriverWait(driver, 40)

try:
    wait.until(EC.presence_of_element_located((By.ID, "wa-popovers-bucket")))
except TimeoutException:
    print("Timed out waiting for page to load")

# Close the browser
driver.quit()