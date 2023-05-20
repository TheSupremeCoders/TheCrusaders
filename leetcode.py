import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
from problem import problem

def get_problems_solved(driver, url):
    # Extract the username from the LeetCode ID
    # pattern = r'https://leetcode.com/([^/]+)/?'
    # username = re.search(pattern, self.leetcode_id).group(1)
    problems_leetcode = []
    driver.get(url)
    time.sleep(3)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extract the titles of the most recent problems solved
    div = soup.find_all('div', attrs={'data-title': True})
    for i in div:
        children = i.findChildren('span')
        pattern = r'^(a\ minute\ ago|a\ few\ seconds\ ago|an\ hour\ ago|\d+\ hours\ ago|\d+\ minutes\ ago)$'
        match = re.search(pattern, children[1].text)
        # concatenate the link with the base url
        if match:
            problems_leetcode.append(problem( i['data-title'], f"https://leetcode.com{i.parent['href']}" ))
        else:
            break

    return problems_leetcode