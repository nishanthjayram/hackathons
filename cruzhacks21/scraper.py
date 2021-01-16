# Import packages to do webscraping
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

# Relevant, easy-to-scrape information
COL_NAMES = ['Company Name', 'Location', 'Job Title']

DATA_LOC = [
    ('span', {'class' : 'topcard__flavor'}), ('span', {'class' : 'topcard__flavor topcard__flavor--bullet'}),
    ('h1', {'class' : 'topcard__title'})
]

# Used to scrape job criteria further down the page
JOB_CRIT = ('span', {'class' : 'job-criteria__text job-criteria__text--criteria'})

# Scrapes job info from a given LinkedIn URL
def scrape_page(URL):
    info = {}
    r = requests.get(URL)
    html_content = r.text
    soup = BeautifulSoup(html_content, 'html.parser')

    try:
        for col, loc in zip(COL_NAMES, DATA_LOC):
            info[col] = soup.find(*loc).text
        s_level = soup.find(*JOB_CRIT)
        e_type = s_level.find_next('span')

        info['Seniority Level'] = s_level.text
        info['Employment Type'] = e_type.text
        return info
    except AttributeError:
        print('Invalid page! Please supply a URL preceding with \'https://www.linkedin.com/jobs/view/\'.')

def main():
    info = scrape_page('https://www.linkedin.com/jobs/view/')
    if (info):
        print(info)

if __name__ == '__main__':
    main()