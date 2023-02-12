class SituationBase:
    name = ""
    WinSit = -1
    LoseSit = -1
    
class Tas(SituationBase):
    def __init__(self):
        self.name = "Taş"
        self.WinSit = 2
        self.LoseSit = 4

class Makas(SituationBase):
    def __init__(self):
        self.name = "Makas"
        self.WinSit = 3
        self.LoseSit = 2

class Kagit(SituationBase):
    def __init__(self):
        self.name = "Kagit"
        self.WinSit = 4
        self.LoseSit = 3