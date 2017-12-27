from visual import *

def grid(n=5, ds = 1., gridcolor = (.6, .6, .6)):
    assert n > 2, "n must be > 2"
    j=n//2
    k=j*2
    if k==n: offset=0
    else: offset = ds/2.
    grid = curve(color = gridcolor)
    for z in arange (-(j+offset)*ds, (j+offset+1)*ds, ds):
        for x in arange(-(j+offset)*ds, (j+offset+1)*ds, ds):
            grid.append(pos=(x, 0, z))
            if x == (j+offset) and not z==(j+offset):
                grid.append (pos=(-(j+offset)*ds,0,z))
                grid.append (pos=(-(j+offset)*ds,0,z+1))
    grid.append(pos=((j+offset)*ds,0,-(j+offset)*ds))
    grid.append (pos=(-(j+offset-1)*ds,0,-(j+offset)*ds))

    for x in arange (-(j+offset)*ds, (j+offset)*ds, ds):
        for z in arange (-(j+offset)*ds, (j+offset+1)*ds, 1):
            grid.append (pos=(x, 0, z))
            if z == (j+offset):
                grid.append (pos=(x,0,-(j+offset)*ds))
                grid.append (pos=(x+1, 0, -(j+offset)*ds))
    return grid

def win():
    wins1=[]
    wins2=[]
    wins=[]

    # planar rows & columns
    for y in arange (-1,2,1):
        z=-2
        for x in arange(-1,2,1):
            col=[(x,y,z+1), (x,y,z+2), (x,y,z+3)]
            wins1.append(col)
        x=-2
        for z in arange(-1,2,1):
            row=[(x+1,y,z), (x+2,y,z),(x+3,y,z)]
            wins1.append(row)

    # planar diagonals
    x=-2
    z=-2
    for y in arange (-1,2,1):
        wins2.append([(x+1,y,z+1), (x+2,y,z+2), (x+3,y,z+3)])
        wins2.append([(x+3,y,z+1), (x+2,y,z+2), (x+1,y,z+3)])

    wins=wins1+wins2
    return wins
