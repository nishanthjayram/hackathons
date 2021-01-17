"""
    Implements functionality to webscrape job information from LinkedIn pages.

    Author  :   Nishanth Jayram (https://github.com/njayram44)
                Sean Touchstone (https://github.com/seant001)
                Jay Wei         (https://github.com/Jay1020431)
    Date    :   January 16, 2021
"""

# Import packages to do webscraping
from bs4 import BeautifulSoup
import time
import requests

# Relevant, easy-to-scrape information contained in a list
DATA_LOC = [
    ('span', {'class' : 'topcard__flavor'}), ('span', {'class' : 'topcard__flavor topcard__flavor--bullet'}),
    ('h1', {'class' : 'topcard__title'})
]

# Used to handle more difficult scraping of job criteria further down the page
JOB_CRIT = ('span', {'class' : 'job-criteria__text job-criteria__text--criteria'})

"""Given a valid LinkedIn URL, scrapes pertinent information and returns a list of data values."""
def scrape_page(URL):
    r = requests.get(URL)
    html_content = r.text
    soup = BeautifulSoup(html_content, 'html.parser')

    try:
        info = [soup.find(*loc).text for loc in DATA_LOC]
        s_level = soup.find(*JOB_CRIT)
        e_type = s_level.find_next('span')
        info.extend([s_level.text, e_type.text])
        return info
    except AttributeError:
        return False

"""Given a file of several (valid) LinkedIn URLs, scrapes all and combines information into a
list of lists."""
def scraper(filename='jobslist.txt'):
    output = []
    job_dir = open('jobslist.txt', 'r')
    for job in job_dir:
        s = scrape_page(job)
        if not s:
            continue
        output.append(s)
    return output

# Debugging procedures
def main():
    print("Running webscrape on a single LinkedIn page: https://www.linkedin.com/jobs/view/2348402842/?refId=f1abe8b6-755d-4c06-a2db-f3bf1c70a591")
    print("Output:", scrape_page("https://www.linkedin.com/jobs/view/2348402842/?refId=f1abe8b6-755d-4c06-a2db-f3bf1c70a591"))

    print("Running webscrape on a text file of LinkedIn pages: jobslist.txt")
    print("Output:", scraper())

if __name__ == '__main__':
    main()