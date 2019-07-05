from Materia import Materia
from Profesor import Profesor 
from Poblacion import Poblacion
from Individuo import Individuo 

######################################## CARGA DE DATOS (profesores) ########################################

#Definimos nuestra lista de profesores (inicialmente vacia):
listaProfesores=[]

#Definimos 2 listas para el primer profesor (1-Kipper):
listaDiasTurnos1=[[1,2],[2,2],[3,2],[4,2],[5,2],[1,1],[2,1],[3,1],[4,1],[5,1]] 
#Preferencia de horarios del profe. Dupla [dia,turno] donde "dia" es 1-lunes,...,5-viernes y "turno" es 1-manana o 2-tarde.
listaMaterias1=[15,16,17,18]  #Materias que puede dar el profe.

#Instanciamos un objeto Profesor (instanciamos al objeto Kipper):
Kipper = Profesor(1,'Kipper',listaDiasTurnos1,listaMaterias1) #es el new Profesor(...) de Java. Esto "machearia con lo que esta en el metodo init de Profesor (es el "constructor" de Java).
listaProfesores.append(Kipper) #agregamos a la lista de profesores al objeto Kipper con sus atributos.

#Ahora hacemos lo mismo para el profesor 2 (Miguel):
#Definimos 2 listas para el segundo profesor (2-Miguel)
listaDiasTurnos2=[[3,2],[3,3],[5,3],[1,1],[2,1]] 
listaMaterias2=[25,3,4,9,5]  

#Instanciamos un objeto Profesor (instanciamos al objeto miguel):
Miguel = Profesor(2,'Miguel',listaDiasTurnos2,listaMaterias2)
listaProfesores.append(Miguel)

#Y ahora hacemos lo mismo para el resto (18) de los profesores:
listaDiasTurnos3=[[1,2],[2,2],[3,2],[4,2],[5,2],[1,1],[2,1],[3,1],[4,1],[5,1]]
listaMaterias3=[5,6,7,8]  
Dubinsky = Profesor(3,'Dubinsky',listaDiasTurnos3,listaMaterias3)
listaProfesores.append(Dubinsky)

listaDiasTurnos4=[[1,1],[2,1],[3,1],[4,1],[5,1]]
listaMaterias4=[26]  
Lagostena = Profesor(4,'Lagostena',listaDiasTurnos4,listaMaterias4)
listaProfesores.append(Lagostena)

listaDiasTurnos5=[[5,2],[5,1]]
listaMaterias5=[10]  
Roldan = Profesor(5,'Roldan',listaDiasTurnos5,listaMaterias5)
listaProfesores.append(Roldan)

listaDiasTurnos6=[[4,1],[4,2],[5,1],[5,2],[3,1],[3,2]]
listaMaterias6=[21,3,5,12]  
Barrios = Profesor(6,'Barrios',listaDiasTurnos6,listaMaterias6)
listaProfesores.append(Barrios)

listaDiasTurnos7=[[1,1],[2,1],[3,1],[1,2],[2,2],[3,2]]
listaMaterias7=[12,19,21]  
Kenobi = Profesor(7,'Kenobi',listaDiasTurnos7,listaMaterias7)
listaProfesores.append(Kenobi)

listaDiasTurnos8=[[5,1],[4,1],[4,2]]
listaMaterias8=[13,23,27,14]  
Machuca = Profesor(8,'Machuca',listaDiasTurnos8,listaMaterias8)
listaProfesores.append(Machuca)

listaDiasTurnos9=[[1,1],[5,1],[3,1]]
listaMaterias9=[18,11,24]  
Balboa = Profesor(9,'Balboa',listaDiasTurnos9,listaMaterias9)
listaProfesores.append(Balboa)

listaDiasTurnos10=[[1,1],[1,2]]
listaMaterias10=[26,11]  
FunesMori = Profesor(10,'FunesMori',listaDiasTurnos10,listaMaterias10)
listaProfesores.append(FunesMori)

listaDiasTurnos11=[[1,2],[2,2],[3,2],[4,2],[5,2]]
listaMaterias11=[27,18,9]  
Poe = Profesor(11,'Poe',listaDiasTurnos11,listaMaterias11)
listaProfesores.append(Poe)

listaDiasTurnos12=[[1,2],[2,2],[3,2],[4,2],[5,2],[1,1]]
listaMaterias12=[19,3,5]  
Koeman = Profesor(12,'Koeman',listaDiasTurnos12,listaMaterias12)
listaProfesores.append(Koeman)

listaDiasTurnos13=[[1,2],[2,2],[3,2],[4,2],[5,2],[1,1],[2,1]]
listaMaterias13=[20,2,9,11]  
Ginobili = Profesor(13,'Ginobili',listaDiasTurnos13,listaMaterias13)
listaProfesores.append(Ginobili)

listaDiasTurnos14=[[1,2],[2,2],[3,2],[4,2],[5,2],[1,1],[2,1],[3,1],[4,1],[5,1]]
listaMaterias14=[21,11,3,5]  
Zonzatera = Profesor(14,'Zonzatera',listaDiasTurnos14,listaMaterias14)
listaProfesores.append(Zonzatera)

listaDiasTurnos15=[[1,2],[1,1],[3,1],[3,2],[5,1],[5,2]]
listaMaterias15=[1,5,21,26]  
Jasen = Profesor(15,'Jasen',listaDiasTurnos15,listaMaterias15)
listaProfesores.append(Jasen)

listaDiasTurnos16=[[3,1],[3,2],[4,2],[5,2],[2,1],[2,2]]
listaMaterias16=[11,23,22]  
Montecchia = Profesor(16,'Montecchia',listaDiasTurnos16,listaMaterias16)
listaProfesores.append(Montecchia)

listaDiasTurnos17=[[1,2],[2,2],[3,2],[4,2],[5,1],[5,2]]
listaMaterias17=[1,2,3,14]  
Sanchez = Profesor(17,'Sanchez',listaDiasTurnos17,listaMaterias17)
listaProfesores.append(Sanchez)

listaDiasTurnos18=[[1,2],[2,2],[3,2],[4,2],[5,2]]
listaMaterias18=[3,4,5,9]  
Smith = Profesor(18,'Smith',listaDiasTurnos18,listaMaterias18)
listaProfesores.append(Smith)

listaDiasTurnos19=[[1,1],[2,2]]
listaMaterias19=[9,18,21,25]  
Perez = Profesor(19,'Perez',listaDiasTurnos19,listaMaterias19)
listaProfesores.append(Perez)

listaDiasTurnos20=[[1,1],[2,1],[3,1],[4,1],[5,1]]
listaMaterias20=[1,2]  
Allen = Profesor(20,'Allen',listaDiasTurnos20,listaMaterias20)
listaProfesores.append(Allen)

#Asi imprimimos el id del primer profe (posicion 0 en la lista), osea de Kiper:
#print (listaProfesores[0].idProfesor) 
#Asi imprimimos la 1ra dupla (posicion 0) de la lista de turnos del profesor 19 (posicion 18):
#print (listaProfesores[18].diasTurnosProfesor[0])
#Asi imprimimos la 1ra materia (posicion 0) de la lista de materias del profesor 20 (posicion 19):
#print (listaProfesores[19].materiasProfesor[0]) 

#Ver si tengo que hacer una lista de materias.

######################################## Definimos nuestra poblacion ########################################

#Instanciamos una poblacion:
poblacion = Poblacion()  #va al def __init__(self) de Poblacion (al "constructor")
#Generamos nuestra primera poblacion:
poblacion.primeraGeneracion(listaProfesores)

############################################### TESTEOS #####################################################

#PROXIMAMENTE HACER ESTOS TESTs APARTE DEL MAIN (con unitTest, PD1 ver)

#Testeamos lo que esta dentro del while dentro del metodo primeraGeneracion de la clase Poblacion:
#((listaProfesores[profesorRandomDT1 - 1]).materiasProfesor ).count(idmateria):
#Por ej. mi profesor random toco el 9 (Balboa). Y las masterias del profe son 18,11 y 24. 
#print(( (listaProfesores[9 - 1]).materiasProfesor))
#Ahora probamos el count (en idmateria si ponemos 18 nos debe dar true el count):
#print( ((listaProfesores[9 - 1]).materiasProfesor).count(18))

#Saber: Este for te imprime todos los Profesores de la listaProfesores:
#for profe in listaProfesores:
	#print(profe)

#Testeamos poblacion.fitness(listaProfesores):
#poblacion.fitness(listaProfesores)

#Testeamos sort para ordenar las listas:
#Ejemplo de sort (para ordenar la lista "listaIndividuos" luego de asignar los fitness a cada individuo). Asi, queremos
#poner a los de mayor fitness en los 1ros puestos (ordenar de MENOR a MAYOR segun su puntaje de fitness)
#Por ejemplo si tenemos esto: [Individuo1(con sus materias y puntajeF=0), Individuo2(con sus M. y PF.=20), Individuo3(consus M. y PF.=2)]
#A la salida queremos la siguiente lista --> [Individuo1, Individuo3, Individuo2] --> por sus PF.

"""
individuo1=Individuo()
individuo2=Individuo()
individuo3=Individuo()

individuo1.puntajeFitness=4
individuo2.puntajeFitness=20
individuo3.puntajeFitness=2

materia1 = Materia(1, [2,3], [1,2], 3, 4,0)
materia2 = Materia(1, [2,3], [1,2], 3, 4,0)
materia3 = Materia(1, [2,3], [1,2], 3, 4,0)

individuo1.listaMaterias.append(materia1)
individuo1.listaMaterias.append(materia2)
individuo2.listaMaterias.append(materia2)
individuo3.listaMaterias.append(materia3)

poblacion2 = Poblacion()
poblacion2.listaIndividuos = [individuo1,individuo2,individuo3]
"""

#print("Lista desordenada: ")
#print(poblacion2)
#print(poblacion2.listaIndividuos)
#Ordenamos la poblacion (la lista de individuos) en base a su puntajeFitness (de MAYOR a MENOR):
#poblacion2.listaIndividuos.sort(key=lambda objeto: objeto.puntajeFitness, reverse=True) #asi se ordena una lista de objetos (en mi caso lista de Individuos) en base a un atributo (en mi caso "puntajeFitness")
#Si queremos que sea de MAYOR a MENOR simplemente ponemos "reverse=True"
#print("Lista ordenada: ")
#print(poblacion2)
#print(poblacion2.listaIndividuos)

#Probamos pop para eliminar elementos de listas:
#for x in range(0, 2): 
#				print(x)
#				poblacion2.listaIndividuos.pop(0) 
				#es pop(0) y no pop(x): explicado en poblacion.
				#removemos el elemento con indice x de la lista (por ej. lista.pop(0) elimina el 1er elemento)
#				print(poblacion2.listaIndividuos.pop(x))
#poblacion2.listaIndividuos.pop(0)
#poblacion2.listaIndividuos.pop(1)
#print("Lista sin elemento1: ")
#print(poblacion2.listaIndividuos)

#Probamos un for de 2 en 2:
#for x in range(0, 52,2): #x vale de 0 a 100 --> range(start, stop[, step])
#	print (x) #si, de 2 en 2. De 0 hasta 50 llega. 

####################### Aplicamos fitness, cruzamiento y mutacion para obtener la mejor lista ##########################

listaEncontrada=False
ciclosEvolutivos=0

while(listaEncontrada == False):
	poblacion.fitness(listaProfesores)
	#El metodo de arriba nos devuelve la poblacion (la lista de individuos) ordenada en base a su puntajeFitness de MAYOR a MENOR.
	#De esta manera tenemos una lista con el MEJOR puntaje de fitness en la 1ra posicion (indice 0), entonces agarramos este elemento y 
	#lo evaluamos hasta que su puntajeFitness mayor o igual a 90 (condicion de corte).
		
	if((poblacion.listaIndividuos[0].puntajeFitness)>=90):
		listaEncontrada=True
	else:
		poblacion.cruzamiento()
		poblacion.mutacion(listaProfesores)
	
	ciclosEvolutivos=ciclosEvolutivos+1
	print ("Ciclo numero: ", ciclosEvolutivos)
	print ("Puntaje Fitness del 1er elemento de la lista de individuos (el de MEJOR fitness):")
	print (poblacion.listaIndividuos[0].puntajeFitness)

print ("Mejor solucion (individuo) encontrada/o: ")
print ("Se necesitaron: ", ciclosEvolutivos, " ciclos para encontrarla.")
print ("Y la mejor lista es:")
poblacion.listaIndividuos[0].imprimirLista2() #Imprimimos la mejor lista (la 1ra, que tendra el mejor fitness)
