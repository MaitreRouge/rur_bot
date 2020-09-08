"""
Ce programme a été optimisé au maximum prck fuck
La variable a représente le nombre de billes récupérés par le robot
"""
a=0
while (a!=5): #Si le bot n'a pas encore récup les 5 billes, on continue
    if(on_beeper()): # Si le bot est sur une bille, on la récup et on incrémente a
        pick_beeper() 
        a+=1
    elif(not right_is_clear() and front_is_clear()): move() #Si on a un mur a droite et rien devant on avance
    elif(right_is_clear()): #Si on a rien a droite on tourne a droite et on avance
        for i in range(0,3): turn_left() #Vu qu'il n'y a pas de turn_right(), tourner 3 fois a gauche reviens a faire la même chose
        move()
    elif(not front_is_clear()): turn_left() #Si il y a quelquechose devant alors on tourne a gauche
turn_off() #Dés que le rebot a récupéré toutes ses billes, il peut dormir

"""
Total lines : 19
Code lines : 11
Comments lines : 16
"""
