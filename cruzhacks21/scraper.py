# Import packages to do webscraping
from bs4 import BeautifulSoup
import requests

# Relevant, easy-to-scrape information
DATA_LOC = [
    ('span', {'class' : 'topcard__flavor'}), ('span', {'class' : 'topcard__flavor topcard__flavor--bullet'}),
    ('h1', {'class' : 'topcard__title'})
]

# Used to scrape job criteria further down the page
JOB_CRIT = ('span', {'class' : 'job-criteria__text job-criteria__text--criteria'})

# Scrapes job info from a given LinkedIn URL
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

def scraper(filename='jobslist.txt'):
    output = []
    job_dir = open('jobslist.txt', 'r')
    for job in job_dir:
        s = scrape_page(job)
        if not s:
            continue
        output.append(s)
    return output
        
def main():
    print(scraper())

if __name__ == '__main__':
    main()