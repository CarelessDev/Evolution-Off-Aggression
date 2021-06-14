import random

from entity import Entity


class Simulator:

    def __init__(self, n_Hawk:int, n_Dove:int):

        self.Hawk = [Entity(entity_type=True) for n in range(n_Hawk)]
        self.Dove = [Entity(entity_type=False) for n in range(n_Dove)]

        self.all_entity = self.Hawk + self.Dove


    def Fight(self):

        next_gen = []

        # * Shuffle
        random.shuffle(self.all_entity)
        if len(self.all_entity) % 2 != 0:
            next_gen.append(Entity(entity_type=self.all_entity.pop(0).type))

        for n in range((len(self.all_entity)-2)//2):
                Entity_0 = self.all_entity[2*n]
                Entity_1 = self.all_entity[2*n+1]

                Entity_0.interact(Entity_1)
                Entity_1.interact(Entity_0)

                if Entity_0.alive == True:
                    next_gen.append(Entity(entity_type=Entity_0.type))
                if Entity_1.alive == True:
                    next_gen.append(Entity(entity_type=Entity_1.type))
                
                if Entity_0.reproduce == True:
                    next_gen.append(Entity(entity_type=Entity_0.type))
                if Entity_1.reproduce == True:
                    next_gen.append(Entity(entity_type=Entity_1.type))

        self.all_entity = next_gen

    def loop(self, iter:int):
        all_loop = []
        i = 1
        while i<=iter:

            self.Fight()
            n_Dove = 0
            n_Hawk = 0

            loop = []
            for entity in self.all_entity:
                if entity.type == True:
                    n_Hawk += 1
                else:
                    n_Dove += 1
                loop.append([n_Dove, n_Hawk])
            print("\n-------------------")
            print(f"Dove : {n_Dove}")
            print(f"Hawk : {n_Hawk}")
            print("--------------------")
            all_loop.append(loop[-1])
            i += 1
            
        return all_loop
