import csv


class ProblemPersistence:

    def __init__(self):
        pass

    @staticmethod
    def load():
        with open('urioj_problems.csv', 'r+') as csvfile:
            reader = csv.reader(csvfile)
            labels = next(reader)
            problem = {}
            for row in reader:
                _id = row[0]
                problem[_id] = {}
                for label, value in zip(labels[1:], row[1:]):
                    problem[_id][label] = value
            return problem

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
    # scraper = problemscraper.ProblemScraper()
    # problems = scraper.scap()
    # ProblemPersistence.save(problems)
    for problem in ProblemPersistence.load():
        print(problem)

if __name__ == '__main__':
    main()
