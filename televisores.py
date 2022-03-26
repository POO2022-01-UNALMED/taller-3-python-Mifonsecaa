
class Marca:
    def  __init__ (self,nombre):
        self._nombre = nombre
    
    def getNombre(self):
        return self._nombre

    def setNombre(self,nombre2):
        self._nombre = nombre2
    
class TV:
    _canal = 1
    _volumen = 1
    _precio = 500
    _numTV = 0
    def __init__(self,marca,estado,control):
        self._marca = marca
        self._estado = estado 
        self._control = control

    def setCanal(self,numero):
        self._canal = numero
    
    def getCanal(self):
        return self._canal
    
    def setVolumen(self, numero):
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

    
    def setNumTV(self, cuenta):
        if type(cuenta) == TV:
            self._numTV +=1
        else:
            self._numTV 

    def getNumTV(self):
        return self._numTV

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


class Control:
    def __init__(self, tv):
        self._tv = tv
    
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
    
    def setCanal(self):
        self.setCanal = TV.setCanal

    def enlazar(self, televisor):
        self.settv = televisor

    def settv(self, televisor):
        self._tv = televisor
    
    def gettv(self):
        return self._tv


    


    