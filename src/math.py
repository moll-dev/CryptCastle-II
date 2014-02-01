def vectorAdd(loc,direction):
    north = ["north","n"]
    south = ["south","s"]
    east = ["east","e"]
    west = ["west","w"]
    up = ["up","u"]
    down = ["down","d"]

    if direction in north:
        loc[0]-=1
    elif direction in south:
        loc[0]+=1
    elif direction in east:
        loc[1]+=1
    elif direction in west:
        loc[1]-=1
    elif direction in up:
        loc[2]+=1
    elif direction in down:
        loc[2]-=1

