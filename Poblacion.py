import time
import random
from Individuo import Individuo 
from Materia import Materia

class Poblacion(object):

	'''  Constructor '''
	def __init__(self):
		self.listaIndividuos=[] #lista de individuos (de clase Individuo). MI POBLACION. Al principio esta vacia. 
		#Solo para saber, si quisiera devolver el tiempo actual en ms usaria la variable rand (de abajo). Si lo imprimo devuelve por ej. 1561686315243
		#self.rand = int(round(time.time() * 1000))  

	'''Para poder imprimir el objeto Poblacion en caso de necesitarlo:'''
	def __repr__(self):
		return "<Lista Individuos:%s> " % (self.imprimirIndividuo(self.listaIndividuos))


######################################## Definimos la 1ra generacion ########################################

	def primeraGeneracion(self, listaProfesores): #RECORDAR que hay que poner el self en la definicion de funciones!
		for x in range(0, 101): #x vale de 0 a 100 --> range(start, stop[, step])
			#Instanciamos un  Individuo:
			individuo = Individuo()
			for idmateria in range(1, 28): #idmateria vale de 1 a 27.
				#La funcion "random.randint(a, b)" retorna un int random "N" tal que a <= "N" <= b.
				diaOpcion1 = random.randint(1, 5)  #Dia random entre 1 y 5.
				turnoOpcion1 = random.randint(1, 2)  #Turno random entre 1 y 2.
				
				diaOpcion2 = random.randint(1, 5)  #Dia random entre 1 y 5.
				turnoOpcion2 = random.randint(1, 2)  #Turno random entre 1 y 2.
				
				profesorRandomDT1 = random.randint(1, 20) #Profe random entre 1 y 20.
				profesorRandomDT2 = random.randint(1, 20) #Profe random entre 1 y 20.

				#Con este algoritmo nos aseguramos que el profesor da esa materia:
				#Con "(listaProfesores[profesorRandomDT1 - 1].materiasProfesor)" obtenemos la lista de materias del profesor "profesorRandomDT1"
				#Y luego con count(idmateria) nos fijamos si esta esa materia en la lista: minitest de esto en el main.
				while( (( (listaProfesores[profesorRandomDT1 - 1]).materiasProfesor ).count(idmateria))==0):
					profesorRandomDT1 = random.randint(1, 20) #Elegimos otro profe random entre 1 y 20 si el anterior no da la materia.

				while( (( (listaProfesores[profesorRandomDT2 - 1]).materiasProfesor ).count(idmateria))==0):
					profesorRandomDT2 = random.randint(1, 20) #Elegimos otro profe random entre 1 y 20 si el anterior no da la materia.
				
				#Instanciamos las materias (ya que estamos en el bucle for hasta 27) con 2 profes que pueden dar las materias en los 2 dia-Turno:
				#Si queremos imprimir las materias que da el profesorRandomDT1 y DT2 (para corroborar que los while funcionan correctamente):
				#print(idmateria,profesorRandomDT1,profesorRandomDT2)
				materia = Materia(idmateria, [diaOpcion1,turnoOpcion1], [diaOpcion2,turnoOpcion2], profesorRandomDT1, profesorRandomDT2)
				individuo.listaMaterias.append(materia)
			#Fin 2do for.
			self.listaIndividuos.append(individuo)
		#Fin 1er for.
		#print(self.imprimirIndividuo(self.listaIndividuos))

	def imprimirIndividuo(self,listaIndividuos):
		for individuo in listaIndividuos:
			print(individuo) #iria al _repr_ de la CLase Individuo para imprimir la lista de materias.

######################################## Funcion Fitness ########################################

	#1ro recorremos la poblacion de individuos previamente creada.
	#2do si el individuo NO es valido le seteamos en puntajeFitness 0. 
	#3ro si el individuo ES valido entonces...:
			    #I. Si el individuo es valido, le subimos UN punto al fitness.
    			#II. Si ademas de I. algun profesor asignado cumple con el dia O el turno de la materia para la 1ra tupla de dia-turno, le subimos OTRO punto al fitness.
    			#III. Si ademas de de II. algun profesor asignado cumple con el dia Y turno de la materia para la 1ra tupla de dia-turno, le subimos OTRO punto al fitness.
    			#IV. Si ademas de I. algun profesor asignado cumple con el dia O el turno de la materia para la 2da tupla de dia-turno, le subimos OTRO punto al fitness.
    			#V. Si ademas de IV. algun profesor asignado cumple con el dia Y turno de la materia para la 2da tupla de dia-turno, le subimos OTRO punto al fitness.
	def fitness(self, listaProfesores):
		for x in range(0, 101): #recorremos cada individuo de nuestra poblacion (de nuestra listaIndividuos).  
			for individuo in  self.listaIndividuos: #anteriormente en listaIndividuos agregamos Individuos (de la Clase Individuo)
				valorFitness=0
				if(individuo.esValido()):  #metodo esValido dentro de la Clase Individuo. 
					valorFitness=valorFitness+1
					for materia in individuo.listaMaterias:
						profeMateriaActualDT1 = materia.profesorDT1  #profesor que asignamos en DT1.
						profeMateriaActualDT2 = materia.profesorDT2  #profesor que asignamos en DT2.
						indiceProfeMateriaActualDT1 = profeMateriaActualDT1-1  #indice que usaremos mas abajo.
						indiceProfeMateriaActualDT2 = profeMateriaActualDT2-1  #indice que usaremos mas abajo.
						#El -1 de arriba es porque... Por ejemplo arriba en materia.profesorDT1 esta el id del profe 1 (kipper)... entonces en profeMateriaActualDT1 se guarda el 1. 
						#Y abajo en listaProfesores el indice seria profeMateriaActualDT1-1 (osea 0), ya que el indice de la listaProfesores empieza en 0.
						
						#Ahora obtenemos el profesor (objeto) de la listaProfesores que nos pasaron por parametro:
						profesorLPDT1 = listaProfesores[indiceProfeMateriaActualDT1] #LP es por listaProfesores y DT por dia-turno
						profesorLPDT2 = listaProfesores[indiceProfeMateriaActualDT2]

						if(self.diaOTurno1Conciden(materia,profesorLPDT1)):
							valorFitness=valorFitness+1 #En Python NO existe i++, esto es igual a i+=1. 
							if(self.diaYTurno1Conciden(materia,profesorLPDT1)):
								valorFitness=valorFitness+1

						if(self.diaOTurno2Conciden(materia,profesorLPDT1)):
							valorFitness=valorFitness+1
							if(self.diaYTurno2Conciden(materia,profesorLPDT1)):
								valorFitness=valorFitness+1
			
					#Fin 2do for.	
					individuo.puntajeFitness=valorFitness #le seteamos el fitness al individuo correspondiente.
				
				else:
					individuo.puntajeFitness=0 #Si NO es valido le seteamos el fitness = 0 al individuo correspondiente.
				
		#Fin 1er for.
		#Ordenamos la poblacion: (la lista de individuos) en base a su puntajeFitness (de MAYOR a MENOR): ya probado en main como funciona.
		self.listaIndividuos.sort(key=lambda objeto: objeto.puntajeFitness, reverse=True) #asi se ordena una lista de objetos (en mi caso lista de Individuos) en base a un atributo (en mi caso "puntajeFitness")
		#Comprobamos que esta bien imprimiendo la lista y viendo que los 1ros resultados son los que tienen puntajeFitness MAYOR y los ultimos tienen 0 de puntajeFitness (la mayoria):
		#print(self.imprimirIndividuo(self.listaIndividuos))

	#Algoritmos para recorrer el profesor y ver si cumple con el horario asignado de la materia:
	
	#Algoritmos para el diaTurno1 (and y or):
	def diaYTurno1Conciden(self, materia, profesor): #funcion que devuelve un booleano.
	#recibimos un objeto materia y un objeto profesor.
		coincide=False
		for diaTurnoProfesor in profesor.diasTurnosProfesor: #ver composicion del atributo diasTurnosProfesor para entender... (lista de listas) 
			#cada "diaTurnoProfesor" es una LISTA del formato [dia,turno].
			#Comparamos los dias (0) y turnos (1) de las materias y profes para el diaTurno1:
			if((materia.diaTurno1[0] == diaTurnoProfesor[0]) and (materia.diaTurno1[1] == diaTurnoProfesor[1])):
				coincide=True
		return coincide
	
	def diaOTurno1Conciden(self, materia, profesor):
		coincide=False
		for diaTurnoProfesor in profesor.diasTurnosProfesor: #ver composicion del atributo diasTurnosProfesor para entender... (lista de listas) 
			#cada "diaTurnoProfesor" es una LISTA del formato [dia,turno].
			#Comparamos los dias (0) y turnos (1) de las materias y profes para el diaTurno1:
			if((materia.diaTurno1[0] == diaTurnoProfesor[0]) or (materia.diaTurno1[1] == diaTurnoProfesor[1])):
				coincide=True
		return coincide

	#Algoritmo para el diaTurno2 (and y or):
	def diaYTurno2Conciden(self, materia, profesor):  
		coincide=False
		for diaTurnoProfesor in profesor.diasTurnosProfesor:
			#Comparamos los dias (0) y turnos (1) de las materias y profes para el diaTurno2:
			if((materia.diaTurno2[0] == diaTurnoProfesor[0]) and (materia.diaTurno2[1] == diaTurnoProfesor[1])):
				coincide=True
		return coincide

	def diaOTurno2Conciden(self, materia, profesor):  
		coincide=False
		for diaTurnoProfesor in profesor.diasTurnosProfesor:
			#Comparamos los dias (0) y turnos (1) de las materias y profes para el diaTurno2:
			if((materia.diaTurno2[0] == diaTurnoProfesor[0]) or (materia.diaTurno2[1] == diaTurnoProfesor[1])):
				coincide=True
		return coincide

######################################## Cruzamiento ########################################

	#1ro ordenamos nuevamente la lista de individuos segun el fitness de cada una (mediante sort).
	#2do removemos la 2da mitad (la mitad con los peore puntajes Fitness).
	#3ro usamos la 1ra mitad (las listas con los mejores puntajes Fitness) para obtener una lista nueva que reemplazara a la 2da mitad removida anteriormente.
	def cruzamiento(self):
		#1ro:
		#Ordenamos nuevamente la poblacion: (la lista de individuos) en base a su puntajeFitness (de MAYOR a MENOR): ya probado en main como funciona.
		self.listaIndividuos.sort(key=lambda objeto: objeto.puntajeFitness, reverse=True) #asi se ordena una lista de objetos (en mi caso lista de Individuos) en base a un atributo (en mi caso "puntajeFitness")
		#print(self.imprimirIndividuo(self.listaIndividuos)) #imprimimos la lista para corroborar.

		#2do:
		for x in range(0, 50): #x vale de 0 a 49 (el ciclo se hace 50 veces). removemos la 2da mitad (los 50 ultimos, los de PEOR fitness)
				self.listaIndividuos.pop(49) #removemos el elemento con indice 49 de la lista (osea el el 50avo elemento)
				#Le ponemos un numero fijo (49) y no x ya que cuando se borra un elemento de una lista nos desplaza la lista una posicion a la izquierda:
				#Por ejemplo si tenemos lista=[7,4,1,8] y hacemos pop(0) nos dejaria 4,1,8 y ahora el 4 pasaria a ser la 1ra posicion, entonces
				#luego habria que hacer pop(0) nuevamente para eliminar el 4, luego pop(0) para el 1 y asi. NO habria que hacer pop(1), pop(2),etc... 
		#3ro:
		for x in range(0, 50,2): #range(start, stop[, step]). x vale de 0 a 48 (y va de 2 en 2: 0,2,4,6,....,48).
			individuo1 = self.listaIndividuos[x] #0,2,4,.....,48.
			individuo2 = self.listaIndividuos[x+1] #1,3,5,....,49.
			self.cruzar(individuo1, individuo2)
		
	def cruzar(self, individuo1,  individuo2):
		#Instanciamos nuevos individuos:
		individuoHijo1 = Individuo()
		individuoHijo2 = Individuo()
		
		#Recorremos las materias del invdividuo 1:
		#Creamos una nueva materia con los datos del individuo 2.
		#Luego de crear la materia, la agrega al nuevo individuo creado (individuoHijo1).
		for materia in individuo1.listaMaterias:
			#1ro obtenemos la materia del individuo 2 que corresponde a la misma materia del individuo 1 (reconocible por su ID)
			materiaIndividuo2 = (individuo2.listaMaterias)[(materia.IdMateria)-1] #-1 por el indice. materia.IdMateria vale 1 para la 1er vuelta, luego 2,.... y por ultimo 27 (Ya que eran 27 materias).
			#Luego creamos la materia con dichos datos:
			materiaHijo1 = Materia(materia.IdMateria, materiaIndividuo2.diaTurno1, materiaIndividuo2.diaTurno2, materiaIndividuo2.profesorDT1, materiaIndividuo2.profesorDT2)
			#Se le agregamos al hijo:
			(individuoHijo1.listaMaterias).append(materiaHijo1)
		
		#Ahora recorremos las materias del invdividuo 2 y hacemos lo mismo:
		#Creamos una nueva materia con los datos del individuo 1.
		#Luego de crear la materia, la agrega al nuevo individuo creado (individuoHijo2).
		for materia in individuo2.listaMaterias:
			materiaIndividuo1 = (individuo1.listaMaterias)[(materia.IdMateria)-1] #-1 por el indice.
			materiaHijo2 = Materia(materia.IdMateria, materiaIndividuo1.diaTurno1, materiaIndividuo1.diaTurno2, materiaIndividuo1.profesorDT1, materiaIndividuo1.profesorDT2)
			individuoHijo2.listaMaterias.append(materiaHijo2)

		self.listaIndividuos.append(individuoHijo1)
		self.listaIndividuos.append(individuoHijo2)

######################################## Mutacion ########################################

	#1ro agarramos 10 individuos al azar (mutacion del 10%)
	#2do le cambiamos el valor a todas sus materias.
	
	def mutacion(self, listaProfesores):
		for x in range(0, 10): #x vale de 0 a 9 (el ciclo se hace 10 veces).
			individuoAzar = random.randint(1, 100)  #valor entre 1 y 100 (inclusive ambos)
			for materia in ( (self.listaIndividuos[individuoAzar-1]).listaMaterias ): #-1 ya que es el indice. 
				self.mutando(materia, listaProfesores)
	
	#Le cambiamos los valores a una sola materia de manera random. Hicimos practicamente lo mismo en el metodo primeraGeneracion().
	def mutando(self, materia, listaProfesores):
		
		diaOpcion1 = random.randint(1, 5)  #Dia random entre 1 y 5.
		turnoOpcion1 = random.randint(1, 2)  #Turno random entre 1 y 2.
		
		diaOpcion2 = random.randint(1, 5)
		turnoOpcion2 = random.randint(1, 2)

		profesorRandomDT1 = random.randint(1, 20) #Profe random entre 1 y 20.
		profesorRandomDT2 = random.randint(1, 20)

		#Con este algoritmo (estos 2 while's) nos aseguramos que el profesor da esa materia:
		while( (( (listaProfesores[profesorRandomDT1 - 1]).materiasProfesor ).count(materia.IdMateria))==0):
			profesorRandomDT1 = random.randint(1, 20) #Elegimos otro profe random entre 1 y 20 si el anterior no da la materia.

		while( (( (listaProfesores[profesorRandomDT2 - 1]).materiasProfesor ).count(materia.IdMateria))==0):
			profesorRandomDT2 = random.randint(1, 20) 

		#Asignamos a la materia los valores de dias-Turnos y profesores previamente definidos (arriba):
		materia.diaTurno1 = [diaOpcion1,turnoOpcion1]
		materia.diaTurno2 = [diaOpcion2,turnoOpcion2]
		materia.profesorDT1 = profesorRandomDT1
		materia.profesorDT2 = profesorRandomDT2