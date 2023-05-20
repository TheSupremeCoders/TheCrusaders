import codeforces
from selenium import webdriver
from selenium import webdriver
url = 'https://codeforces.com/profile/ace01'

# create a driver
driver = webdriver.Chrome()
# get the problems solved
solved_questions = codeforces.get_problems_solved(driver, url)
# print the problems solved
for question in solved_questions:
    print(question.name, question.link)

# close the driver
driver.quit()