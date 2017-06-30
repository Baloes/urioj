import copy

import problemconstructor


class Name:

    def __init__(self, problem):
        self.problem = problem

    def __contains__(self, name):
        problem = {}
        for _id, info in self.problem.items():
            if name in info['name']:
                problem[_id] = copy.deepcopy(self.problem[_id])
        return Problems(problem=problem)


class Category:

    def __init__(self, problem):
        self.problem = problem

    def __eq__(self, category):
        problem = {}
        for _id, info in self.problem.items():
            if category == info['category']:
                problem[_id] = copy.deepcopy(self.problem[_id])
        return Problems(problem=problem)


class Solved:

    def __init__(self, problem):
        self.problem = problem

    def _return(self, cmp):
        problem = {}
        for _id, info in self.problem.items():
            if cmp(int(info['solved'])):
                problem[_id] = copy.deepcopy(self.problem[_id])
        return Problems(problem=problem)

    def __eq__(self, value):
        return self._return(lambda solved: solved == value)

    def __lt__(self, value):
        return self._return(lambda solved: solved < value)

    def __gt__(self, value):
        return self._return(lambda solved: solved > value)


class Level:

    def __init__(self, problem):
        self.problem = problem

    def _return(self, cmp):
        problem = {}
        for _id, info in self.problem.items():
            if cmp(int(info['level'])):
                problem[_id] = copy.deepcopy(self.problem[_id])
        return Problems(problem=problem)

    def __eq__(self, value):
        return self._return(lambda level: level == value)

    def __lt__(self, value):
        return self._return(lambda level: level < value)

    def __gt__(self, value):
        return self._return(lambda level: level > value)


class Problems:

    def __init__(self, problem=None):
        if not problem:
            constructor = problemconstructor.ProblemConstructor()
            self.problem = constructor.construct()
        else:
            self.problem = problem
        self.name = Name(self.problem)
        self.category = Category(self.problem)
        self.level = Level(self.problem)

    def __len__(self):
        return len(self.problem)

    def __repr__(self):
        string = '{:<5} {:<40} {:<10} {:<7} {:<7} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}\n'\
            .format(
            'id', 'name', 'category', 'solved', 'level',
            'ac', 'ce', 'rte', 'tle', 'pe', 'wa', 'pre'
        )
        for key, value in self.problem.items():
            string += '{}  {name:<40} {category:<10} {solved:<7} {level:<7} ' \
                      '{ac:<5} {ce:<5} {rte:<5} {tle:<5} {pe:<5} {wa:<5} {pre:<5}\n'\
                .format(key, **value)
        return string

    def __and__(self, other):
        problem = {}
        for _id in self.problem.keys():
            if _id in other.problem:
                problem[_id] = copy.deepcopy(self.problem[_id])
        for _id in other.problem.keys():
            if _id in self.problem:
                problem[_id] = copy.deepcopy(other.problem[_id])
        return Problems(problem=problem)

    def __or__(self, other):
        problem = {}
        problem.update(copy.deepcopy(self.problem))
        problem.update(copy.deepcopy(other.problem))
        return Problems(problem=problem)

    def __sub__(self, other):
        problem = {}
        for _id in self.problem.keys():
            if _id not in other.problem:
                problem[_id] = copy.deepcopy(self.problem[_id])
        return Problems(problem=problem)


def main():
    base = Problems()
    print((base.category == 'Grafos').level > 6)

if __name__ == '__main__':
    main()
