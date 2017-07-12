from urllib.request import urlopen
import re
import threading

from bs4 import BeautifulSoup


def _start_thread(n, target, args=None, args_list=None): # TODO: Jogar isso parar um modulo utilitario
    threads = []
    for i in range(n):
        if args_list:
            thread = threading.Thread(target=target, args=(args_list[i],))
        else:
            thread = threading.Thread(target=target, args=(args,))
        thread.start()
        threads.append(thread)
    return threads


def _join_threads(threads):
    for thread in threads:
        thread.join()


def _get_html(url):
    while True:
        try:
            html = BeautifulSoup(urlopen(url), 'html.parser')
        except:
            continue
        return html


def _remove_extra_spaces(text):
    return re.sub(' +', ' ', text).strip()


class ProfileScraper:

    _url_prefix = 'https://www.urionlinejudge.com.br/judge/pt/profile/'

    def __init__(self, id):
        self.id = id
        self.soup = _get_html(self._url_prefix + id)
        self.problems = []

    def _get_profile_info(self):
        keys = ['id', 'name', 'place', 'country', 'university', 'since', 'solved', 'tried', 'submission']
        values = [self.id]
        values.append(self.soup.find(itemprop='name').a.get_text())
        for li in self.soup.find(class_='pb-information').find_all('li'):
            _, value = re.sub(' |\n|\t', '', li.get_text()).split(':')
            values.append(value)
        return {key: value for key, value in zip(keys, values)}

    def _get_n_pages(self):
        content = self.soup.div.find(id='table-info').contents[0]  # i.e "1 of 32"
        return [int(i) for i in content.split() if i.isdigit()][-1]

    def _get_problems_solved_pages(self, url):
        n_pages = self._get_n_pages()
        for page in range(1, n_pages + 1):
            yield url + '?page=' + str(page)

    def _get_problems_solved(self, url):
        soup = _get_html(url)
        tbody = soup.find('tbody')
        problem_id = tbody.find_all(class_='id')
        problem_time = tbody.find_all(class_='small')[3::4]
        problem_date = tbody.find_all(class_='center')
        problems = []
        for id, time, date in zip(problem_id, problem_time, problem_date):
            _id = re.sub('\n|\t', '', id.get_text())
            _id = _remove_extra_spaces(_id)
            time = re.sub('\n|\t', '', time.get_text())
            date = re.sub('\n|\t', '', date.get_text())
            problems.append((_id, time, date))
        self.problems += problems # TODO: caso nao seja o CPython pode ter problema de sincronizacao

    def scrap(self):
        profile_info = self._get_profile_info()
        threads = []
        for page_html in self._get_problems_solved_pages(self._url_prefix + self.id):
            threads += _start_thread(1, self._get_problems_solved, args=page_html)
        _join_threads(threads)
        profile_info['problems_solved'] = self.problems
        return profile_info


def main():
    pass


if __name__ == '__main__':
    main()

'''
Profile.id
Profile.name
Profile.place
Profile.country
Profile.university
Profiel.since
Profile.solved
Profile.tried
Profile.submission
Profile.problem
'''

