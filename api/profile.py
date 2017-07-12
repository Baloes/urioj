import profilepersistence
import profilescraper
import problem

class Profile:

    def __init__(self, id, name, place, country, university, since, solved, tried, submission, problems_solved):
        self.id = id
        self.name = name
        self.place = place
        self.country = country
        self.university = university
        self.since = since
        self.solved = solved
        self.tried = tried
        self.submission = submission
        self._problem_solved_info = problems_solved
        self.problem = problem.Problems() & [info[0] for info in problems_solved]


    def __str__(self):
        return '- %s (%s) -\nPlace: %s\nCountry: %s\nUniversity: ' \
               '%s\nSince: %s\nSolved: %s\nTried: %s\nSubmissions: %s' % \
               (self.name, self.id, self.place, self.country, self.university,
                self.since, self.solved, self.tried, self.submission)

def main():
    pass


if __name__ == '__main__':
    main()