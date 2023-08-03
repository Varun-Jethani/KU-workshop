from PIL import Image
import random

end = 100
ladder={8:26,21:82,43:77,50:91,54:93,62:96,66:87,80:100}
snakes={44:22,46:5,48:9,52:11,55:7,59:17,64:36,69:33,73:1,83:19,92:51,95:24,98:28}


def show_board():
    img = Image.open('sknlad.jpg')
    img.show()

def check_ladder(points):
    if points in ladder:
        points=ladder[points]
    return points

def check_snake(points):
    if points in snakes:
        points = snakes[points]
    return points

def reached_end(points):
    if points==end:
        return True
    else:
        return False

def play():
    p1_name = input("Player1, Please enter your Name")
    p2_name = input("Player2, Please enter your Name")
    pp1=0
    pp2=0

    turn=0

    while(1):
        if turn%2==0:
            print(p1_name,'your turn')
            c = input('Press 1 to continue, 0 to quit:')
            if c==0:
                print(p1_name,'Scored',pp1)
                print(p2_name,'Scored',pp2)
                print('Quitting the Gme, Thanks for playing')
                break
            dice = random.randint(1,6)
            print('Dice showed: ',dice)
            pp1 = pp1 + dice
            pp1= check_ladder(pp1)
            pp1= check_snake(pp1)
            if pp1>end:
                pp1=end
            print(p1_name,'Your Score: ', pp1)
            if reached_end(pp1):
                print(p1_name, 'won')
                break
            turn+=1
        else:
            print(p2_name,'your turn')
            c = input('Press 1 to continue, 0 to quit:')
            if c==0:
                print(p1_name,'Scored',pp1)
                print(p2_name,'Scored',pp2)
                print('Quitting the Gme, Thanks for playing')
                break
            dice = random.randint(1,6)
            print('Dice showed: ',dice)
            pp2 = pp2 + dice
            pp2= check_ladder(pp2)
            pp2= check_snake(pp2)
            if pp2>end:
                pp2=end
            print(p2_name,'Your Score: ', pp2)
            if reached_end(pp2):
                print(p2_name, 'won')
                break
            turn+=1

show_board()
play()