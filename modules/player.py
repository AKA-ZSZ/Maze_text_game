class Player:
    def __init__(self):
        self._backpack={}

    @property
    def backpack(self):
        return self._backpack

    def pick_up_item(self,item):
        if item not in self.backpack:
            self.backpack[item]=1
        else:
            self.backpack[item]+=1

    
    