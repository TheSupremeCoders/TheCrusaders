from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from problem import problem

def get_problems_solved(driver, url):
    driver.get(url)
    # Find the table of recently solved questions
    table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@class='dataTable']/tbody")))

    pattern = r"\d{1,2}\s(sec|min|hour)s?\sago"

    # Extract the list of solved questions
    solved_questions = set()
    try: 
        for row in table.find_elements("xpath", ".//tr"):
            tim = row.find_elements("xpath", ".//td")[0].get_attribute("title")
            # print the title of span inside td[2]
            status = row.find_elements("xpath", ".//td")[2].find_element("xpath", ".//span").get_attribute("title")
            title = row.find_elements("xpath", ".//td")[1].text
            link = row.find_elements("xpath", ".//td")[4].find_element("xpath", ".//a").get_attribute("href")
            if re.match(pattern, tim) and status == "accepted":
                solved_questions.add(problem(title, link)) 
    except: 
        print("Wrong ID?")


    for i in range(3):
        # Click the next button to get the next page of the table
        try: 
            next_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, './/a[@onclick="onload_getpage_recent_activity_user(\'next\');"]' )))
            driver.execute_script("arguments[0].click();", next_button)

            # Wait for the table to become stale
            WebDriverWait(driver, 10).until(EC.staleness_of(table))

            # Wait for the new table to be loaded and fully rendered
            table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@class='dataTable']/tbody")))

            for row in table.find_elements("xpath", ".//tr"):
                tim = row.find_elements("xpath", ".//td")[0].get_attribute("title")
                title = row.find_elements("xpath", ".//td")[1].text
                link = row.find_elements("xpath", ".//td")[4].find_element("xpath", ".//a").get_attribute("href")
                link = f'https://www.codechef.com{link}'
                if re.match(pattern, tim):
                    solved_questions.add(problem(title, link)) 
        except:
            print("Wrong ID?")
    return solved_questions
