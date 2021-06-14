import random

class Entity:

    def __init__(self, entity_type:bool):

        self.type = entity_type
        self.alive = True


    def interact(self, interacted_entity):

        self.reproduce = False

        if interacted_entity != None:
            
            if self.type == True and interacted_entity.type == True:
                self.alive = False
            
            if self.type == False and interacted_entity.type == True:
                self.alive = random.choice([True, False])

            if self.type == True and interacted_entity.type == False:
                self.reproduce = random.choice([True, False])

            if self.type == False and interacted_entity.type == False:
                self.reproduce = random.choice([True, False])
        else:
            self.reproduce = True
        
