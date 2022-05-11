from random import randint, random
from termios import CIBAUD
from tkinter import Menu



##################################################################################
# creacion_historia function that create a story
def creacion_historia(historia_elegida):
    print(' ')

    if (historia_elegida == 1):
        print('⛺⛺⛺El valle encantado ⛺⛺⛺')
        nombre = input('Escoje un nombre ')
        hobby = input('Que te gusta hacer? ')
        gusto = input('Que otra cosa te gusta hacer? ')
        ropa = input('Cual es tu ropa favorita? ')
        animal = input('Escoje un animal ')
        animal_2 = input('Escoje otro animal ')
        emocion = input('Escoje una emocion ')
        historia = """
Habia una vez una niña llamada {} que le gustaba mucho {}, un dia
sus amigos la invitaron a {} al valle encantado, cuando llegaron se dieron cuenta 
que se les olvidaron las {} entonces tuvieron que caminar por el valle todo el dia asi.

En la noche estaban comiendo {}, cuando escucharon un ruido extraño que sonaba a {} 
se {} del susto, y mas nunca volvieron al valle encantado
        """.format(nombre,hobby,gusto,ropa,animal,animal_2,emocion)
        print(historia)

    elif (historia_elegida == 2):
        print('🛸🛸🛸Secuestro alienigena 🛸🛸🛸')
        dia = input('Escoje un dia cualquiera ')
        nombre = input('Escoje un nombre ')
        actividad = input('Escribe cualquier actividad ')
        lugar = input('Escoje un lugar cualquiera ')
        cosa = input('Escribe cualquier cosa ')
        forma = input('Escoje cualquier forma ')
        actividad_2 = input('Escribe cualquier actividad ')
        actividad_3 = input('Escribe cualquier actividad ')
        historia = """
Una noche del {} {} estaba {} cuando escucho unos ruidos extraños que venian 
del {}, se asomo y vio unos aliens en forma de {} que la agarraron y se la
llevaron en su nave espacial en forma de {}, le dijieron que querian {} 
la tierra.

Al escuchar esto {} se {} y mas nunca los volvio a ver.
        """.format(dia,nombre,actividad,lugar,cosa,forma,actividad_2,nombre,actividad_3)
        print(historia)

    elif (historia_elegida == 3):
        print('✈✈✈El viaje ✈✈✈')
        nombre = input('Di un nombre: ')
        emocion = input('Como te sientes en este momento? ')
        ciudad = input('Nombra una ciudad ')
        cosa = input('Escribe cualquier cosa ')
        reaccion = input('Escribe un sentimiento ')
        cosa_2 = input('Escribe cualquier cosa ')
        pais_imaginario = input('Escribe algun sition imaginario ')
        historia = """
{} a estado muy {} por su viaje a {}, tiene todo listo o al menos eso cree
rumbo al aeropuerto se da cuenta que se le olvidaron los {}, entonces al no poder hacer nada
se pone a {}.

Cuando se monta en el avion se da cuenta que tomo el vuelo equivocado, entonces cuando llega a {}
busca a su {} para ver como devolverse a {}. Que locura!!
        """.format(nombre,emocion,ciudad,cosa,reaccion,ciudad,cosa_2,pais_imaginario)
        print(historia)

    elif (historia_elegida == 4):
        print('🤑🤑🤑Mi trabajo favorito 🤑🤑🤑')
        nombre = input('Escribe un nombre ')
        cualidad = input('Escribe una cualidad ')
        nombre_2 = input('Escribe un nombre ')
        cualidad_2 = input('Escribe una cualidad ')
        sentimiento = input('Escribe un sentimiento ')
        accion = input('Escribe una accion ')
        cosa = input('Escribe cualquier cosa ')
        cosa_2 = input('Escribe cualquier cosa ')
        accion_2 = input('Escribe una accion ')
        lugar = input('Escribe un lugar ')
        historia = """
{} es la persona que mas quiero en este mundo, pienso que es alguien muy {}
mientras que {} es un {}, me cae muy {}.

Esta mañana mi jefe me {} porque me {} y no le avise, en fin que coma {},
mañana voy a {} en su {}
        """.format(nombre,cualidad,nombre_2,cualidad_2,sentimiento,accion,cosa,cosa_2,accion_2,lugar)
        print(historia)

    else:
        print('Lo sentimos solo tenemos las historias dentro del menu 😥')


##################################################################################
# seleccion_historia function that allows the user to choose which story he/she wants to play
def seleccion_historia():
    menu = """
    Estas son las historias que tenemos disponibles, selecciona el numero que quieras jugar:
    1. El valle encantado ⛺
    2. Secuestro alienigena 🛸
    3. El viaje ✈
    4. Mi trabajo favorito 🤑

    """

    historia_elegida = int(input(menu))
    creacion_historia(historia_elegida)


##################################################################################
# menu_historia function which allows the user to choose a fixed or random story
def menu_historia():
    menu= """
    Presiona 1 si quieres escojer tu propia historia, o presiona 2 si quieres una historia al azar:
    """
    valor_historia = int(input(menu))
    if (valor_historia == 1):
        #print('Escoje la historia que deseas')
        seleccion_historia()
    elif (valor_historia == 2):
        #print('Se selecciona una historia al azar')
        historia_random = randint(1,4)
        creacion_historia(historia_random)
    else:
        print('Lo sentimos pero solo permitimos opción 1 o 2 😥')


##################################################################################
# main function
def main():
    menu = """
    Hola bienvenido al increible mundo de Mad Libs, a continuacion te explicamos las reglas
    del juego:

    Para empezar tienes 2 modalidades de juego:
    a ) Escojes tu propia historia dentro del menu.
    b ) Escojes una historia aleatoria

    Una vez selecciones el tipo de historia que deseas, se te va a desplegar un menu,
    donde tendras que ingresar los datos que pida el juego. 

    Eso es todo, cuando termines de hacerlo podras leer la historia con tus datos ingresados.

    Disfruta!!! 🤪😜😝

    """
    print(menu)
    menu_historia()

if __name__=='__main__':
    main()