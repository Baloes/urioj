from urllib.request import urlopen
import re

from bs4 import BeautifulSoup

# import profile


def get_n_pages(soup):
    content = soup.div.find(id='table-info').contents[0]  # i.e "1 of 32"
    return [int(i) for i in content.split() if i.isdigit()][-1]

def get_problems_solved_pages(url, soup):
    n_pages = get_n_pages(soup)
    for page in range(1, n_pages + 1):
        page_soup = BeautifulSoup(urlopen(url + '?page=' + str(page)), 'html.parser')
        yield page_soup


class ProfileScraper:

    _url_prefix = 'https://www.urionlinejudge.com.br/judge/pt/profile/'

    def __init__(self, id):
        self.id = id
        self.soup = BeautifulSoup(urlopen(self._url_prefix + id), 'html.parser')

    def _get_profile_info(self):
        keys = ['id', 'name', 'place', 'country', 'university', 'since', 'solved', 'tried', 'submission']
        values = [self.id]
        values.append(self.soup.find(itemprop='name').a.get_text())
        for li in self.soup.find(class_='pb-information').find_all('li'):
            _, value = re.sub(' |\n|\t', '', li.get_text()).split(':')
            values.append(value)
        return {key: value for key, value in zip(keys, values)}

    def _get_problems_solved(self, soup):
        tbody = soup.find('tbody')
        problem_id = tbody.find_all(class_='id')
        problem_name = tbody.find_all(class_='wide')
        problem_time = tbody.find_all(class_='small')[3::4]
        problem_date = tbody.find_all(class_='center')
        for id, name, time, date in zip(problem_id, problem_name, problem_time, problem_date):
            print('---------')
            print(re.sub('\n|\t', '', id.get_text()))
            print(re.sub('\n|\t', '', name.get_text()))
            print(re.sub('\n|\t', '', time.get_text()))
            print(re.sub('\n|\t', '', date.get_text()))

    def get_data(self):
        for page_soup in get_problems_solved_pages(self._url_prefix + self.id, self.soup):
            self._get_problems_solved(page_soup)
        # return profile.Profile(**self._get_profile_info())


def main():
    scraper = ProfileScraper('36720')
    profile = scraper.get_data()
    print(profile)

main()

'''
Modulos publicos da API:
-Profile
-Problems = Coleção de Problemas
-University = Coleção de Alunos
'''