#########################################################################
# problem.py é um espelho dos problemas disponíveis do uri, com apenas um
# subconjunto das informações.
#
# Fazer primeiro o problem.py, porque os outros tem dependencia dele
#
#########################################################################

# Interface
class Problems():

    def __init__(self): # Primeiro passo: Verificar se existe uma base de dados com os problemas
        pass            # Segundo passo: Caso sim, carrega os dados na memória, caso contrário
                        #                verifica se o usuáro quer baixar pela primeira vez a
                        #                base de dados.

    def update(self, flag=None): # ideia da flag é se quer fazer uma soft-update (só verifica se possui)
        pass                     # problemas novos, ou hard-update, se deseja verificar toda a base de
                                 # dados

    def get(self, id=None, name=None): # Retorna um Problem
        pass


# get by id
# get by name
# get by category
# get by most solved
# get by level
# allow expression like Problems.level < X and problems.category == 'Grafos'
# or Problems.solved[-5] and Problems.category.grafos


# Problems.id -> return a list of ID's
# Problems.name -> return a list of names
# Problems.categoty -> return a list of categories
# Problems.level -> return a list of levels
#