import os

import problemscraper
import problempersistence


class ProblemConstructor:

    def _in_database(self):
        return os.path.exists(os.getcwd() + '/database/urioj_problems.csv')

    def construct(self):
        if self._in_database():
            return problempersistence.ProblemPersistence.load()
        else:
            scraper = problemscraper.ProblemScraper()
            return scraper.scrap()


def main():
    constructor = ProblemConstructor()
    for problem in constructor.construct():
        print(problem)


if __name__ == '__main__':
    main()