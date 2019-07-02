class Materia(object):

	'''  Constructor '''
	def __init__(self,IdMateria,diaTurno1,diaTurno2,profesorDT1,profesorDT2):
		self.IdMateria=IdMateria #int
		#Si queda tiempo declarar todas estas variables y metodos privados (con el __ son metodos privados), asi no puedo acceder a ellos directamente desde el main (Creo que es por esto).
		#Por ej. self.__IdMateria=IdMateria;
		self.diaTurno1=diaTurno1 #DUPLA de int dia e int turno.
		self.diaTurno2=diaTurno2
		self.profesorDT1=profesorDT1 #int.
		self.profesorDT2=profesorDT2

	'''Para poder imprimir el objeto Materia en caso de necesitarlo:'''
	def __repr__(self):
		return "<ID materia:%s Dia-Turno 1:%s Dia-Turno 2:%s Profesor para el D.T. 1:%s Profesor para el D.T. 2:%s> " % (self.IdMateria, self.diaTurno1, self.diaTurno2, self.profesorDT1, self.profesorDT2)
    
        