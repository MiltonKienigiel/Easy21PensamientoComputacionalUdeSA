############################# NO TOCAR ESTE CÓDIGO ############################
from random import randint

def sacar_carta():
    '''
    Esta función toma una carta de un mazo de forma aleatoria. La carta está numerada del 1 al 10 (inclusive).

    params:
        Esta función no tiene parámetros de entrada.
    out:
        carta: int. El número de la carta sacada.
    '''
    carta = randint(1,10)
    return carta


######################## EJEMPLO DE USO DE SACAR_CARTA ########################
#c = sacar_carta()
#print(c)
#En la consola se vería:    8

########################### AQUÍ COMIENZA TU CÓDGIO ###########################
seguir_jugando = True
jugo_otro = False
plata_jugador = 500
listaGanadores = []
while(seguir_jugando): # Repetición del juego
    #Tu código va acá
    juega_jugador = True
    juega_crupier = True
    crupier_perdio = False
    jugador_perdio = False
    print("Bienvenid@ a la mesa de Easy 21")
    if not jugo_otro:
        nombreJugador = input("¿Cual es tu nombre?")
    
    print("Empieza la partida")
    crupier_cartas = []
    jugador_cartas = []
    
    carta_crupier = sacar_carta()
    crupier_cartas.append(carta_crupier)
    
    print("El crupier saca un ", carta_crupier)
    print("Por el momento sacó las cartas: ", crupier_cartas)
    apuesta_bool = input(f"¿Quiere apostar {nombreJugador}? (s/n)")
    apuesta_jugador = 0
    if apuesta_bool == "s":
        puede_apostar = True
        while(puede_apostar):
            apuesta_jugador = int(input(f"¿Cuánto quiere apostar {nombreJugador}? (Max ${plata_jugador})"))
            if apuesta_jugador < 0 :
                print("Tienes que apostar algo de plata!")
            elif apuesta_jugador > plata_jugador:
                print("No puedes apostar mas plata de la que tenes")
            elif apuesta_jugador == plata_jugador:
                print("ALL IN!")
                puede_apostar = False
            else:
                puede_apostar = False
    
    while(juega_jugador):
        carta_jugador = sacar_carta()
        jugador_cartas.append(carta_jugador)
        print("Usted saca un ", carta_jugador)
        print("Por el momento sacó las cartas: ", jugador_cartas)
        
        sacar_otra_carta = input("¿Quieres sacar otra carta? (s/n)")
        if sacar_otra_carta == "s":
            saco_mas_cartas = True
            while(saco_mas_cartas):
                    carta_jugador = sacar_carta()
                    jugador_cartas.append(carta_jugador)
                    print(f"{nombreJugador} sacaste un {carta_jugador} su total es {sum(jugador_cartas)}")
                    print("Por el momento sacó las cartas: ", jugador_cartas)
                   
                    if sum(jugador_cartas)> 21:
                        saco_mas_cartas = False
                        juega_jugador = False
                        jugador_perdio = True
                    if not jugador_perdio:
                        sacar_otra_carta = input("¿Quieres sacar otra carta? (s/n)")
                        if sacar_otra_carta == "n":
                            saco_mas_cartas = False
                            juega_jugador = False
                    
        else :
            juega_jugador = False
            
    while(juega_crupier and not jugador_perdio):
        print("----------Juega el crupier----------")
        print("--")
        print("--")
        carta_crupier = sacar_carta()
        crupier_cartas.append(carta_crupier)
        print(f"El crupier saca un {carta_crupier} su total es {sum(crupier_cartas)}")
        print("Por el momento las cartas son : ", crupier_cartas)
        
        while (sum(crupier_cartas) < 16 ):
            print("--")
            print("Pide otra carta")
            carta_crupier = sacar_carta()
            crupier_cartas.append(carta_crupier)
            print(f"El crupier saca un {carta_crupier} su total es {sum(crupier_cartas)}")
            print("Por el momento las cartas son : ", crupier_cartas)
        if sum(crupier_cartas)>21:
            crupier_perdio = True
        juega_crupier = False   
        
    if jugador_perdio and not crupier_perdio: #El jugador se paso de cantidad de cartas
        listaGanadores.append("Crupier")
        print("La partida termina, el crupier gana")
        if apuesta_bool == "s":
            plata_jugador = plata_jugador - apuesta_jugador
        print(f"Le quedan ${plata_jugador}")             
    if crupier_perdio and not jugador_perdio: #El crupier se paso y el jugador no
        listaGanadores.append(nombreJugador)
        print("La partida termina. GANASTE!")
        if apuesta_bool == "s":
            plata_jugador = plata_jugador -apuesta_jugador+ apuesta_jugador*2
        print(f"Le quedan ${plata_jugador}")
   
    elif not jugador_perdio and not crupier_perdio: #El jugador no se paso de 21 y el crupier tampoco
        if sum(jugador_cartas)> sum(crupier_cartas): #El jugador estuvo mas cerca de 21 que el crupier
            listaGanadores.append(nombreJugador)

            print("La partida termina. GANASTE!")
            if apuesta_bool == "s":
                plata_jugador = plata_jugador -apuesta_jugador + apuesta_jugador*2
            print(f"Le quedan ${plata_jugador}")
        else:
            listaGanadores.append("Crupier")
            print("La partida termina, el crupier gana")
            if apuesta_bool == "s":
                plata_jugador = plata_jugador - apuesta_jugador
            print(f"Le quedan ${plata_jugador}")   
            
    if jugo_otro:
        print(f"El historial de partidas es: {listaGanadores}")
        
    jugar_otro = input("¿Quieres jugar otro? (s/n)")
    if jugar_otro == "n" :
        seguir_jugando = False
        
    else: 
        jugo_otro = True
        
 
        
    
    
    

