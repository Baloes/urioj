import csv


class ProblemPersistence:

    @staticmethod
    def load():
        with open('database/urioj_problems.csv', 'r+') as csvfile:
            reader = csv.reader(csvfile)
            labels = next(reader)
            problem = {}
            for row in reader:
                _id = row[0]
                problem[_id] = {}
                for label, data in zip(labels[1:], row[1:]):
                    problem[_id][label] = data
            return problem

    @staticmethod
    def save(data):
        with open('database/urioj_problems.csv', 'w+') as csvfile:
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
