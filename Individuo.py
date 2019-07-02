from Materia import Materia #lo necesitamos en el metodo esvalido()

class Individuo(object):

	'''  Constructor '''
	def __init__(self):
		self.listaMaterias=[] #lista ints
		self.puntajeFitness=0 #int

	'''Para poder imprimir el objeto Individuo en caso de necesitarlo:'''
	def __repr__(self):
		return "<Lista Materias:%s Puntaje Fitness:%s> " % (self.imprimirLista(self.listaMaterias), self.puntajeFitness)

	def imprimirLista(self,lista): #usado aca por el __repr__
		for elemento in lista:
			print(elemento)

	def imprimirLista2(self): #usado en el main para imprimir la mejor lista.
		" ciclos para encontrarla."
		print "El fitness del individuo es: ", self.puntajeFitness
		for materia in self.listaMaterias:
			print "La materia: ", materia.IdMateria
			print "Se da el dia (Dia 1): ", materia.diaTurno1[0], " en el turno (Turno 1): ", materia.diaTurno1[1], ", teniendo como profesor a: ", materia.profesorDT1
			print "Y se da el dia (Dia 2): ", materia.diaTurno2[0], " en el turno (Turno 2): ", materia.diaTurno2[1], " teniendo como profesor a: ", materia.profesorDT2
			#diaTurno 1 y 2 de un objeto materia: [diaOpcion1,turnoOpcion1], [diaOpcion2,turnoOpcion2]

	def esValido(self): #devuelve un boolean. Lo usamos en el metodo fitness() de Poblacion
	#Un individuo es valido si sus asignaciones de profesores y horarios no se pisan (por ej. un mismo profesor no
	#puede dar al mismo tiempo (dia y turno) 2 materias a la vez. Tampoco ninguna materia debe coincidir los dias y turnos
	#de sus tuplas dia-Turno 1 y Dia-Turno 2.
		es_Valido=True
		#Con los 2 for comparamos a TODAS las materias entre si 
		for materiaActual in self.listaMaterias:
			for materiaComparo in self.listaMaterias:

				#Si los IDs de materias son distintos...
				if(materiaActual.IdMateria!=materiaComparo.IdMateria):

					#Mismo profesor en diaTurno1 da la misma materia en el mismo dia y turno....
					if(materiaActual.profesorDT1==materiaComparo.profesorDT1):
						#materiaActual.diaTurno1[0] es el DIA (indice 0) de la amteria del diaTurno1. 
						#materiActual.diaTurno2[1] es el TURNO (indice 1) de la materia del diaTurno2.
						#Si los dias Y los turnos entre las materias que comparamos del DT1 coinciden...
						if(materiaActual.diaTurno1[0]==materiaComparo.diaTurno1[0] & materiaActual.diaTurno1[1]==materiaComparo.diaTurno1[1]):
							es_Valido=False

					#Mismo profesor en diaTurno2 da la misma materia en el mismo dia y turno....
					if(materiaActual.profesorDT2==materiaComparo.profesorDT2):
						#Si los dias Y los turnos entre las materias que comparamos del DT2 coinciden...
						if(materiaActual.diaTurno2[0]==materiaComparo.diaTurno2[0] & materiaActual.diaTurno2[1]==materiaComparo.diaTurno2[1]):
							es_Valido=False

					#Mismos profesores en diaTurno1 y diaTurno2 dan la misma materia en el mismo dia y turno....
					if(materiaActual.profesorDT1==materiaComparo.profesorDT2):
						if(materiaActual.diaTurno1[0]==materiaComparo.diaTurno2[0] & materiaActual.diaTurno1[1]==materiaComparo.diaTurno2[1]):
							es_Valido=False

				#Si los IDs de las materias son iguales...
				#Hay que corroborar que distintos profesores no den la materia al mismo momento
				else:
					if(materiaActual.diaTurno1[0]==materiaComparo.diaTurno2[0] & materiaActual.diaTurno1[1]==materiaComparo.diaTurno2[1]):
						es_Valido=False
		return es_Valido