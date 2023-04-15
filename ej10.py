nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David',
'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica', 
'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge',
'JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana','LAUTARO', 'Leonel', 'Luisa', 
'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás',  'Nancy', 'Noelia', 'Pablo', 
'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''
notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12, 77, 
           13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18, 7, 
           74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64, 13, 8,
           87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47, 15, 31,
           39, 15, 74, 33, 57, 10]
#10. Dada una lista de nombres de estudiantes y dos listas con sus notas en un curso, escriba un programa que manipule dichas estructuras de datos para poder resolver los siguientes puntos:

#    1. Generar una estructura con todas las notas relacionando el nombre del estudiante con las notas. Utilizar esta estructura para la resolución de los siguientes items.

#El archivo de nombres lo convertimos en una lista

lista=nombres.replace('\n',' ').replace('\'','').split(',')

print(lista)

                      
#Genero un diccionario para utilizar en los proximos items, este sera la estructura a utilizar. Convertimos las tres listas en un diccionario. Donde los nombres sean las claves y las notas los valores.

estructura= {}

for i in range(len(notas_1)): #Todas tiene el mismo largo asi que no importa cual use.
    
    estructura[lista[i]]=[notas_1[i],notas_2[i]]
print(estructura) 



#2. Calcular el promedio de notas de cada estudiante.

#Determinamos el promedio de notas 1 y 2 de cada alumnx.
print()
print()

def prom(**kwargs):


    for clave, valor in kwargs.items():  #Recorremos el diccionario

        k=0      #k sera la suma de las notas para luego calcular el promedio
        c=0      #c se refiere a un contador que contara las notas, ya que desconocemos la
                 #cantidad de notas 

        for i in valor:
            k+=i
            c+=1

        k/=c     #una vez que c conto las notas, dividira k para obtener el promedio.

        print(f"el promedio de {clave} sera {k}")

#3. Calcular el promedio general del curso.
    
#Ahora calculo el promedio general de todxs lxs estudiantes. Mediante una funcion que calcula el promedio individual de cada estudiante a partir de las notas proporcionadas y guarda los resultados en un diccionario. Luego, utiliza los promedios individuales para calcular el promedio general de la clase y devolver un nuevo diccionario con los promedios individuales y el promedio general de la clase.

def general(**kwargs):

    pgeneral=0

    reg_prom={}

    for clave, valor in kwargs.items():

        k=0
        c=0

        for i in valor:
            k+=i
            c+=1                  

        k/=c

                                   #Sumamos la nota del alumnx al promedio general.
        pgeneral+=k

    pgeneral/=len(kwargs)      
                               #Dividimos la suma del promedio general por la cantidad de alumnxs para el promedio de la clase. 
    print()
    print(f"""El promedio general de la clase sera {pgeneral}""")


    
def registro_promedio(**kwargs):
    """Este programa tiene como objetivo procesar un diccionario que contiene información de los estudiantes y sus respectivas notas. A partir de este diccionario, se calcula el promedio de notas de cada estudiante y se imprime por pantalla el resultado junto con el nombre correspondiente. Además, se utiliza la información de los promedios individuales para calcular el promedio general de la clase. Finalmente, se devuelve un diccionario que contiene el promedio de cada estudiante y el promedio general de la clase."""

    pgeneral=0

    for clave, valor in kwargs.items():

        k=0
        c=0

        for i in valor:
            k+=i
            c+=1
        k/=c

        kwargs[clave].append(k)   
    print()

prom(**estructura) #Llamamos a la funcion previamente definida sobre el diccionario que creamos. 
general(**estructura)
registro_promedio(**estructura)        

# 4. Identificar al estudiante con la nota promedio más alta.

#Identificamos al estudiante con la nota promedio mas alta.

print()


high_value= max(estructura.items(), key=lambda item: item[1][2]) 

print(f"El mejor promedio sera {high_value[0]} con {high_value[1][2]}.")

print()

#5. Identificar al estudiante con la nota más baja.

MIN1=min(estructura.items(), key=lambda item: item[1][0])
MIN2=min(estructura.items(), key=lambda item: item[1][1])


for name in estructura.keys():
    if MIN1 <= MIN2:
        if estructura[name][0]==MIN1[1][0]:
            print(f"La menor nota es{name} con {estructura[name][0]} en el 1er examen")
    elif MIN2 < MIN1:
        if estructura[name][1]==MIN2[1][1]:
            print(f"La menor nota es{name} con {estructura[name][1]} en el 2do examen")            

  
    
    
    
