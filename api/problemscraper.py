from urllib.request import urlopen
import queue
import re
import threading
import time

from bs4 import BeautifulSoup


_urioj_url = 'https://www.urionlinejudge.com.br'
_urioj_problem_url = _urioj_url + '/judge/pt/problems/all?page='
_urioj_problem_rank_url = _urioj_url + '/judge/pt/ranks/problem/'


def _start_thread(n, target, args=None, args_list=None):
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


class ProblemScraper:

    def __init__(self, n_thread_per_problem_list=25):
        self.n_thread_per_problem_list = n_thread_per_problem_list
        self.pages_to_process = queue.Queue()
        self.problem_info = {}
        self.problems_scrapped = 0

    def _scrap_problem_statistic(self, problems_url):
        while not problems_url.empty():
            url = problems_url.get()
            html = _get_html(url)
            for script in html.find_all('script'):
                if '$(document).ready(' in script.get_text():
                    start = script.get_text().find('[')
                    end = script.get_text().find('];')
                    text = re.sub('/.+/|\[|{|}|\]|\n|\t|', '', script.get_text()[start:end + 1])
                    text = _remove_extra_spaces(text)
                    submission_counter = []
                    for item in text.split(','):
                        key, value = item.split(':')
                        if 'value' in key:
                            value = _remove_extra_spaces(value)
                            submission_counter.append(value)
                    problem_id = url.rsplit('/', 1)[-1]
                    for counter in submission_counter:
                        self.problem_info[problem_id].append(counter)
            self.problems_scrapped += 1
            print(self.problems_scrapped)

    def _scrap_problem_info(self, html):
        for tr in html.tbody.find_all('tr'):
            info = []
            for td in tr.find_all('td'):
                data = re.sub('\n|\t', '', td.get_text())
                data = _remove_extra_spaces(data)
                if data:
                    info.append(data)
            if info:
                problem_id, problem_info = info[0], info[1:]
                self.problem_info[problem_id] = problem_info

    def _generate_problems_url(self, html):
        problems_url = queue.Queue()
        for td in html.tbody.find_all(class_='id'):
            problem_number = td.a['href'].rsplit('/', 1)[-1]
            problems_url.put(_urioj_problem_rank_url + problem_number)
        return problems_url

    def _get_problem_info(self):
        threads = []
        while not self.pages_to_process.empty():
            html = self.pages_to_process.get()
            self._scrap_problem_info(html)
            problems_url = self._generate_problems_url(html)
            threads += _start_thread(
                self.n_thread_per_problem_list,
                self._scrap_problem_statistic,
                args=problems_url
            )
        _join_threads(threads)

    def _get_n_pages(self, root):
        content = root.find(id='table-info').get_text()
        return int([i for i in content.split() if i.isdigit()][-1])

    def _download_problem_page_list(self, url):
        self.pages_to_process.put(_get_html(url))

    def _travel_problem_list(self):
        page_url = _urioj_problem_url + '1'
        root = BeautifulSoup(urlopen(page_url), 'html.parser')
        self.pages_to_process.put(root)
        n_pages = self._get_n_pages(root)
        args_list = [_urioj_problem_url + str(n)for n in range(2, n_pages + 1)]
        threads = _start_thread(
            n_pages - 1,
            self._download_problem_page_list,
            args_list=args_list
        )
        _join_threads(threads)

    def scap(self):
        self._travel_problem_list()
        self._get_problem_info()
        sorted_problems = sorted(self.problem_info.items(), key=lambda x: x[0])
        return [tuple([key] + value) for key, value in sorted_problems]

    def update(self):
        pass


def main():
    t0 = time.time()
    scraper = ProblemScraper()
    problem_info = scraper.scap()
    for problem in problem_info:
        print(problem)
    print(time.time() - t0)
    print(problem_info.__sizeof__())


if __name__ == '__main__':
    main()