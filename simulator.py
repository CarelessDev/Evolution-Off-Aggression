from entity import Entity


class Simulator:

    def __init__(self, n_Hawk:int, n_Dove:int):

        self.n_Hawk = [Entity(entity_type=True) for n in range(n_Hawk)]
        self.n_Dove = [Entity(entity_type=False) for n in range(n_Dove)]

        self.all_entity = []

        '''for n in range(self.n_Hawk):
            self.all_entity.append(Entity(entity_type=True))

        for n in range(self.n_Dove):
            self.all_entity.append(Entity(entity_type=False))
'''