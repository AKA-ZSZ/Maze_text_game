class Player:
    def __init__(self,backpack=[]):
        if type(backpack)!=list:
            raise TypeError
        # [item1,item2...]
        self._backpack=backpack

    @property
    def backpack(self):
        return self._backpack

    def pickup(self,item):
        if item not in self.backpack:
            self.backpack.append(item)
        # else:
        #     self.backpack[item]+=1

    
    