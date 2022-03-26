from televisores.tv import TV

class Control:
    _tv = None
    def __init__(self):
        pass
    
    def turnOn(self):
        self.turnOn = TV.turnON

    def turnOff(self):
        self.turnOff = TV.turnOff

    def canalUp(self):
        self.canalUp = TV.canalUp

    def canalDown(self):
        self.canalDown = TV.canalDown

    def volumenUp(self):
        self.volumenUp = TV.volumenUp

    def volumenDown(self):
        self.volumenDown = TV.volumenDown
    
    def setCanal(self, algo):
        self.setCanal = TV.setCanal

    def enlazar(self, televisor):
        self.settv = televisor
        TV.setControl = self.settv

    def settv(self, televisor):
        self._tv = televisor
    
    def gettv(self):
        return self._tv