
class TV:
    _numTV = 0
    def __init__(self,marca,estado):
        self._marca = marca
        self._estado = estado 
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        TV._numTV += 1
        
    def setCanal(self, numero):
        if self._estado == True:
            if numero >= 1 and numero <= 120:
                self._canal = numero

    def getCanal(self):
        return self._canal
    
    def setVolumen(self,numero):
        if self._estado == True and numero >= 0 and numero <= 7:
            self._volumen = numero
    
    def getVolumen(self):
        return self._canal

    def setPrecio(self, valor):
        self._precio = valor

    def getPrecio(self):
        return self._precio
    
    def setMarca(self, marca):
        self._marca  = marca

    def getMarca(self):
        return self._marca

    def setControl(self, control):
        self._control = control

    def getControl(self):
        return self._control

    @classmethod
    def setNumTV(cls):
        TV.numTV = cls._numTV
        
    @classmethod
    def getNumTV(cls):
        return cls._numTV

    def turnOn(self):
        self._estado = True
    
    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado


    def canalUp(self):
        if self._estado == True:
            if self._canal < 120:
                self._canal +=1 


    def canalDown(self):
        if self._estado == True:
            if self._canal:
                self._canal -= 1

    def volumenUp(self):
        if self._estado == True:
            if self._volumen <= 7 :
                self._volumen += 1
    
    def volumenDown(self):
        if self._estado == True:
            if self._volumen > 0:
                self._volumen -= 1





    


    