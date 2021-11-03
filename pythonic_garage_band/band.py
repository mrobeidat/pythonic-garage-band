from abc import ABC, abstractmethod, abstractstaticmethod


class Musician(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass
   
    
class Guitarist(Musician):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo" 


class Drummer(Musician):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    def get_instrument(self):
        return "drums"
    def play_solo(self):
        return "rattle boom crash" 


class Bassist(Musician):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    def get_instrument(self):
        return "bass"
    def play_solo(self):
        return "bom bom buh bom" 



class Band(Musician):

    def __init__(self, name, members):
        self.name = name
        self.members=members

    def __str__(self):
        return 
    def __repr__(self):
        return 

