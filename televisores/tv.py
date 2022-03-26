
class TV:
    _canal = 1
    _volumen = 1
    _precio = 500
    _numTV = 0
    _control = None
    def __init__(self,marca,estado):
        self._marca = marca
        self._estado = estado 
        
    def setCanal(self, numero):
        self._canal = self._canal + numero
    
    def getCanal(self,):
        return self._canal
    
    def setVolumen(self,numero):
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

    
    def setNumTV(self):
        self._numTV 
        

    def getNumTV():
        return TV._numTV

    def turnON(self, encendido):
        if self._estado == False:
            if encendido == True:
                self._estado = encendido
    
    def turnOff(self, apagar):
        if self._estado == True:
            if apagar == True:
                self._estado == False

    def getEstado(self):
        return self._estado


    def canalUp(self, pasar):
        if self._estado == True:
            if (self._canal + pasar) >= 1 and (self.canal + pasar) <= 120:
                return self._canal


    def canalDown(self,bajar):
        if self._estado == True:
            if (self._canal - bajar) >= 1 or (self.canal - bajar) <= 120:
                return self._canal

    def volumenUp(self, subirvol):
        if self._estado == True:
            if (self._volumen + subirvol) >= 0 or (self._volumen + subirvol):
                return self._volumen 
    
    def volumenDown(self, bajarvol):
        if self._estado == True:
            if (self._volumen - bajarvol) >= 0 or (self._volumen + bajarvol):
                return self._volumen





    


    