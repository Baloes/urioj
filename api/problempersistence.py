import csv

import problemscraper


class ProblemPersistence:

    def __init__(self):
        pass

    @staticmethod
    def load(self):
        pass

    @staticmethod
    def save(data):
        with open('urioj_problems.csv', 'w+') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                'id', 'name', 'category', 'solved', 'level',
                'ac', 'ce', 'rte', 'tle', 'pe', 'wa', 'pre'
            ])
            for row in data:
                writer.writerow(row)


def main():
    scraper = problemscraper.ProblemScraper()
    problems = scraper.scap()
    ProblemPersistence.save(problems)


if __name__ == '__main__':
    main()