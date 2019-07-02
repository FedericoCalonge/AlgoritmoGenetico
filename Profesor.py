class Profesor(object):
	
	'''  Constructor '''
	def __init__(self,idProfesor,nombreProfesor,diasTurnosProfesor,materiasProfesor):
		self.idProfesor=idProfesor #int
		self.nombreProfesor=nombreProfesor #string
		self.diasTurnosProfesor=diasTurnosProfesor  #lista de duplas ints dia-turno
		self.materiasProfesor=materiasProfesor #lista de ints.

	'''Para poder imprimir el objeto Profesor en caso de necesitarlo:'''
	def __repr__(self):
		return "<ID:%s Nombre:%s Dias-Turnos:%s Materias:%s> " % (self.idProfesor, self.nombreProfesor, self.diasTurnosProfesor, self.materiasProfesor)
    
        