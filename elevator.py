'''
Puzzle: The elevator
In this tower, the architect has designed an elevator which is able to serve all floors but both in the elevator or on each floor there are only two buttons to make it work or to call it. If the elevator is at the level N, the button U(up) makes the elevator go up to level N+8 if N+8 is less than or equal to the total number of floors in the tower, otherwise it doesn't move. And there is a button D(down) which makes the elevator go down to level N-11 if of course N is at least 11, otherwise it doesn't move. We also know that if the building had a floor less than it has now, the elevator could not serve all floors. 
What is the height of the tower?
'''
def visiting(floor,Floorlist,maxbound):
    if Floorlist[floor] == True:
        pass
    else:
        Floorlist[floor] = True
        if floor+8 <= maxbound:
            visiting(floor+8,Floorlist,maxbound)
        if floor-11 >=0:
            visiting(floor-11,Floorlist,maxbound)
        
def AllAcessible(numberoffloor):
    Floornotvisited = {}
    for i in range(0,numberoffloor+1,1):
        Floornotvisited[i] = False
    visiting(0, Floornotvisited, numberoffloor)
    for floor in Floornotvisited:
        if Floornotvisited[floor] == False:
            return False
    return True
    
index = 1
found = False
while found == False:
    found = AllAcessible(index) 
    if found ==True:
        print index
    index+=1
    