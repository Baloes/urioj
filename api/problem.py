import copy

import problemconstructor


class Name:

    def __init__(self, problem):
        self.problem = problem

    def __eq__(self, name):
        problem = {}
        for _id, info in self.problem.items():
            if name in info['name'].lower():
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
            if cmp(int(info['solved'].replace('.', ''))):
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


class Accept:

    def __init__(self, problem):
        self.problem = problem

    def _return(self, cmp):
        problem = {}
        for _id, info in self.problem.items():
            if int(info['totsub']) != 0 and cmp(float(info['ac']) / int(info['totsub'])):
                problem[_id] = copy.deepcopy(self.problem[_id])
        return Problems(problem=problem)

    def __lt__(self, value):
        return self._return(lambda level: level < value)

    def __gt__(self, value):
        return self._return(lambda level: level > value)


class CompilationError:

    def __init__(self, problem):
        self.problem = problem

    def _return(self, cmp):
        problem = {}
        for _id, info in self.problem.items():
            if int(info['totsub']) != 0 and cmp(float(info['ce']) / int(info['totsub'])):
                problem[_id] = copy.deepcopy(self.problem[_id])
        return Problems(problem=problem)

    def __lt__(self, value):
        return self._return(lambda level: level < value)

    def __gt__(self, value):
        return self._return(lambda level: level > value)


class RuntimeError:

    def __init__(self, problem):
        self.problem = problem

    def _return(self, cmp):
        problem = {}
        for _id, info in self.problem.items():
            if int(info['totsub']) != 0 and cmp(float(info['rte']) / int(info['totsub'])):
                problem[_id] = copy.deepcopy(self.problem[_id])
        return Problems(problem=problem)

    def __lt__(self, value):
        return self._return(lambda level: level < value)

    def __gt__(self, value):
        return self._return(lambda level: level > value)


class TimeLimitExceed:

    def __init__(self, problem):
        self.problem = problem

    def _return(self, cmp):
        problem = {}
        for _id, info in self.problem.items():
            if int(info['totsub']) != 0 and cmp(float(info['tle']) / int(info['totsub'])):
                problem[_id] = copy.deepcopy(self.problem[_id])
        return Problems(problem=problem)

    def __lt__(self, value):
        return self._return(lambda level: level < value)

    def __gt__(self, value):
        return self._return(lambda level: level > value)


class PresentationError:

    def __init__(self, problem):
        self.problem = problem

    def _return(self, cmp):
        problem = {}
        for _id, info in self.problem.items():
            if int(info['totsub']) != 0 and cmp(float(info['pe']) / int(info['totsub'])):
                problem[_id] = copy.deepcopy(self.problem[_id])
        return Problems(problem=problem)

    def __lt__(self, value):
        return self._return(lambda level: level < value)

    def __gt__(self, value):
        return self._return(lambda level: level > value)


class WrongAnswer:

    def __init__(self, problem):
        self.problem = problem

    def _return(self, cmp):
        problem = {}
        for _id, info in self.problem.items():
            if int(info['totsub']) != 0 and cmp(float(info['wa']) / int(info['totsub'])):
                problem[_id] = copy.deepcopy(self.problem[_id])
        return Problems(problem=problem)

    def __lt__(self, value):
        return self._return(lambda level: level < value)

    def __gt__(self, value):
        return self._return(lambda level: level > value)


class PossibleRuntimeError:

    def __init__(self, problem):
        self.problem = problem

    def _return(self, cmp):
        problem = {}
        for _id, info in self.problem.items():
            if int(info['totsub']) != 0 and cmp(float(info['pre']) / int(info['totsub'])):
                problem[_id] = copy.deepcopy(self.problem[_id])
        return Problems(problem=problem)

    def __lt__(self, value):
        return self._return(lambda level: level < value)

    def __gt__(self, value):
        return self._return(lambda level: level > value)


class Problems:

    def __init__(self, problem=None):
        if problem is None:
            constructor = problemconstructor.ProblemConstructor()
            self.problem = constructor.construct()
        else:
            self.problem = problem
        self._set_total_submission()
        self.name = Name(self.problem)
        self.category = Category(self.problem)
        self.solved = Solved(self.problem)
        self.level = Level(self.problem)
        self.ac = Accept(self.problem)
        self.ce = CompilationError(self.problem)
        self.rte = RuntimeError(self.problem)
        self.tle = TimeLimitExceed(self.problem)
        self.pe = PresentationError(self.problem)
        self.wa = WrongAnswer(self.problem)
        self.pre = PossibleRuntimeError(self.problem)

    def _set_total_submission(self):
        for _id, info in self.problem.items():
            total_submission = int(info['ac']) \
                             + int(info['ce']) \
                             + int(info['rte']) \
                             + int(info['tle']) \
                             + int(info['pe']) \
                             + int(info['wa']) \
                             + int(info['pre'])
            self.problem[_id].update({'totsub': total_submission})

    def __len__(self):
        return len(self.problem)

    def __repr__(self):
        string = '{:<5} {:<44} {:<27} {:<7} {:<7} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5} {:<5}\n'\
            .format(
                'id', 'name', 'category', 'solved', 'level',
                'ac', 'ce', 'rte', 'tle', 'pe', 'wa', 'pre'
            )
        for key, value in self.problem.items():
            string += '{}  {name:<44} {category:<27} {solved:<7} {level:<7} ' \
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
    all = Problems()
    # print((all.category == 'Grafos').level > 6)
    # print(all.solved > 5000)
    print(all.pre > 0.00)

if __name__ == '__main__':
    main()
