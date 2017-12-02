from asignacionHistorias import models
from . import asignacion as asig
import numpy 

    

def construirModeloLineal(asignacion):
    """
    Construir un modelo de programacion lineal basado en el tipo de asignacion.
    Keyword arguments:
    asignacion -- Asignacion dada, asignacion.Asignacion
    """
    if (asignacion.tipo == asig.TipoAsignacion.sencilla):
        return 0

class FabricaModeloLinealUnicaPonderacion:
    asignacion = None
    def __init__(self, newAsignacion):
        self.asignacion = newAsignacion    
        
    def construirModeloLinealUnicaPonderacion(self):
        """
        Construir un modelo de programacion lineal basado en el tipo de asignacion.
        Keyword arguments:
        asignacion -- Asignacion dada, asignacion.Asignacion
        """
    
    def construirTotalRestricciones(self):
        restriccionesEquilibrio, vectorTopeEquilibrio = self.restriccionesEquilibrioAsignacion()
        restriccionesCumplirCadaHistoria, vectorTopeCumplirCada = self.restriccionesCumplirTodasHistorias()
        vectorTope = []
        vectorTope.append(vectorTopeEquilibrio,vectorTopeCumplirCada,vectorTopeBool)
        
        
        
    def cantidadVariablesDesicion(self):
        return self.asignacion.cantidadHistorias + self.asignacion.cantidadDesarrolladores
        
    def restriccionesEquilibrioAsignacion(self):
        topeMaximo = self.asignacion.getMediaPuntosGeneralesHistorias() + self.asignacion.getDesvEstPuntosGeneralesHistorias()
        vectorTope = [topeMaximo for i in range(0, self.asignacion.cantidadDesarrolladores  )]
        restricciones = [[1 for x in range (0, self.cantidadVariablesDesicion() )] for j in range (0,self.asignacion.cantidadDesarrolladores)]
        return restricciones, vectorTope

    def funcionMaximizar(self):
        return [1 for x in range(self.cantidadVariablesDesicion() )]
    
    def restriccionesCumplirTodasHistorias(self):
        restricciones = numpy.zeros((  self.asignacion.cantidadHistorias*2, self.cantidadVariablesDesicion() ))
        topePositivo = [1 for i in range(0, self.asignacion.cantidadHistorias )]
        topeNegativo = [-1 for i in range(0, self.asignacion.cantidadHistorias  )]
        
        for x in range (0, self.asignacion.cantidadHistorias):
            for i in range (0, self.cantidadVariablesDesicion() , self.asignacion.cantidadDesarrolladores):
                restricciones[x][i:self.asignacion.cantidadDesarrolladores] = [1 for x in range(0, self.asignacion.cantidadDesarrolladores)]
                
        for x in range (self.asignacion.cantidadHistorias - 1, (self.asignacion.cantidadHistorias * 2) -1):
            for i in range (0, self.cantidadVariablesDesicion() , self.asignacion.cantidadDesarrolladores):
                restricciones[x][i:self.asignacion.cantidadDesarrolladores] = [-1 for x in range(0, self.asignacion.cantidadDesarrolladores)]
        return restricciones, topePositivo.extend(topeNegativo)
    
    def restriccionesVariablesBooleanas(self):
        return [(1,1) for x in range(0, self.cantidadVariablesDesicion())]
                