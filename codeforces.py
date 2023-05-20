import time
from problem import problem
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import date, timedelta
import datetime
import re
import pytz

def get_problems_solved(driver, url):
    # use regular expressions to extract the username
    match = re.search(r"/?profile/(/?\w+/?)", url)
    username = match.group(1).strip("/")
    url = f"https://codeforces.com/submissions/{username}"
    driver.get(url)
    # Wait for the page to load
    time.sleep(5)

    # Get the HTML content of the page
    html = driver.page_source

    # Parse HTML content using Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all the rows in the submissions table
    rows = soup.find_all('tr')

    # Extract the problem codes of all the accepted submissions
    solved_problems = set()
    for row in rows[1:]:  # Ignore the first row (table header)
        cols = row.find_all('td')
        if(len(cols) != 0):
            # take only first 11 characters of the cols[1].text.strip()
            # because it contains the date and time in the format
            # write today in the format May/04/2023 from asia/kolkata timezone
            tz = pytz.timezone('Asia/Kolkata')
            today = datetime.datetime.now(tz).strftime("%b/%d/%Y")  # Fixed this line
            yesterday = (datetime.datetime.now(tz) - timedelta(1)).strftime("%b/%d/%Y")

            if len(cols) > 1 and (cols[1].text.strip()[0:11] == today or cols[1].text.strip()[0:11] == yesterday):
            # if cols[1].text.strip()[0:11] == today:
                verdict = cols[5].span.get('submissionverdict')
                if verdict == "OK":
                    problem_code = cols[3].a.text
                    solved_problems.add(problem(problem_code.strip(), url))

    return solved_problems
