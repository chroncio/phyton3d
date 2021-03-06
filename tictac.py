import sys
print (sys.path)
from visual import *
from tictacdat import *

# scene settings
scene.width=800
scene.height=800
scene.title="KiK"
scene.center = (-1, -0.5, -1)
scene.forward = (-1, -.7, -.7)
scene.scale = (.2, .2, .2)


# colors
red = (1, 0, 0)
blue = (.3, .3, 1)
green = (.5, 1, 0)

# draw board
matrix = grid(n=3, ds=1, gridcolor=blue)

# get list of winning combinations
wins = win()

# select field
bars = {}
balls = {}

#texts
textWinnerRed = text(text='Red wins!', pos=(0, 1.5, 0), align='center', depth=-0.5, color=color.red, axis=(1,0,-0.7));
textWinnerRed.visible =0;
textWinnerBlue = text(text='Blue wins', pos=(0, 1.5, 0), align='center', depth=-0.5, color=color.blue, axis=(1,0,-0.7));
textWinnerBlue.visible = 0;



for x in arange(-1, 2, 1):
    for z in arange(-1, 2, 1):
        cyl = box(pos=(x,-.06,z), axis=(0,.12,0), radius=0.5, visible=1, opacity=0.1, color=blue)
        bars[(x, 0, z)] = cyl

visbar=None
bcolor = red
point = None
won = None

while len(balls) < 3*3:
    while True:
        rate(100)
        if scene.mouse.clicked:
            p = scene.mouse.getclick()
            point= p.project(normal=vector(0,1,0),d=0)   # 'None' if not in plane
            break

    # chose valid square
    if not (point==None):
        point=(round(point[0]), round(point[1]), round(point[2]))
        if not (visbar==None):visbar.visible=0
        if not (point in bars):
            continue
        visbar=bars[point]
        visbar.visible=0
        if bcolor==red:
            b = ring(pos=point, radius=0.3, color=bcolor, thickness=0.1, axis=(0,1,0))
        else:
            b = cone(pos=point, radius=0.3, color=bcolor, axis=(0,1,0))
        bpoint=(round(b.x), round(0), round(b.z))
        if not(bpoint in balls): # not already a ball there
            b.pos=bpoint
            balls[bpoint]=b
            if bcolor==red: bcolor=blue
            else:bcolor=red
        else:               ## already a ball there, so abort
            b.visible=0
        visbar=None

        # check for four in a row
        for a in wins:
            a0=a[0] in balls
            a1=a[1] in balls
            a2=a[2] in balls
            if a0 and a1 and a2:
                ccolor=balls[a[0]].color
                if balls[a[1]].color==balls[a[2]].color==ccolor:
                    won=ccolor
                    if ccolor==red:
                        print("***********")
                        print(" Red wins!")
                        print("***********")
                        textWinnerRed.visible  = 1;
                        winnerText = textWinnerRed;
                    else:
                        print("***********")
                        print(" Blue wins!")
                        print("***********")
                        textWinnerBlue.visible = 1;
                        winnerText = textWinnerBlue;

                    for flash in arange(0,10):
                        balls[a[0]].color=(1,1,1)
                        balls[a[1]].color=(1,1,1)
                        balls[a[2]].color=(1,1,1)
                        rate(1)
                        balls[a[0]].color=ccolor
                        balls[a[1]].color=ccolor
                        balls[a[2]].color=ccolor
                        rate(1)
                    break
        if not (won==None):
            if not 'winnerText' in vars():
                print("***********")
                print(" draw")
                print("***********")
                winnerText = text(text='draw', pos=(0, 1.5, 0), align='center', depth=-0.5, color=color.green)
            break
