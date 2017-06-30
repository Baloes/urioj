import profilepersistence
import profilescraper
import problemparser

class Profile:

    def __init__(self, id, name, place, country, university, since, solved, tried, submission):
        self.id = id
        self.name = name
        self.place = place
        self.country = country
        self.university = university
        self.since = since
        self.solved = solved
        self.tried = tried
        self.submission = submission

    def __str__(self):
        return '- %s (%s) -\nPlace: %s\nCountry: %s\nUniversity: ' \
               '%s\nSince: %s\nSolved: %s\nTried: %s\nSubmissions: %s' % \
               (self.name, self.id, self.place, self.country, self.university,
                self.since, self.solved, self.tried, self.submission)

if __name__ == '__main__':
    pass