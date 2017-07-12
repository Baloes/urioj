import csv


class ProfilePersistence:

    @staticmethod
    def load(id):
        profile_info = {}
        with open('database/%s.csv' % id, 'r+') as csvfile:
            reader = csv.reader(csvfile)
            info_label = next(reader)
            info_data = next(reader)
            for label, data in zip(info_label, info_data):
                profile_info[label] = data
            problems_solved_label = next(reader)
            profile_info['problems_solved'] = list(reader)
        return profile_info

    @staticmethod
    def save(id, data):
        with open('database/%s.csv' % id, 'w+') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                'name', 'id', 'place', 'country', 'university',
                'since', 'solved', 'tried', 'submission'
            ])
            writer.writerow([
                data['name'], data['id'], data['place'], data['country'], data['university'],
                data['since'], data['solved'], data['tried'], data['submission']
            ])
            writer.writerow(['id', 'time', 'date'])
            for row in data['problems_solved']:
                writer.writerow(row)


def main():
    # scraper = problemscraper.ProblemScraper()
    # problems = scraper.scap()
    # ProblemPersistence.save(problems)
    for problem in ProfilePersistence.load():
        print(problem)

if __name__ == '__main__':
    main()
