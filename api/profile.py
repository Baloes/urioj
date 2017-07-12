import profileconstructor
import problem

class Profile:

    def __init__(self, id):
        constructor = profileconstructor.ProfileConstructor()
        self.__dict__.update(constructor.construct(id))
        self.problem = problem.Problem() & [info[0] for info in self.problems_solved]

    def __str__(self):
        return '- %s (%s) -\nPlace: %s\nCountry: %s\nUniversity: ' \
               '%s\nSince: %s\nSolved: %s\nTried: %s\nSubmissions: %s' % \
               (self.name, self.id, self.place, self.country, self.university,
                self.since, self.solved, self.tried, self.submission)


def main():
    renan = Profile('36720')
    luis = Profile('20268')
    print(renan)
    print('****')
    print(luis)


if __name__ == '__main__':
    main()