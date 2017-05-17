
refresh_rate = 1000
turn_speed = 20
def ballInView():
    return True

ball_x = 0
ball_y = 0
px = 0
focal = 200

def goToGoal():
    print("going to goal")

def turnRight():
    print("turning right")
def turnLeft():
    print("turning left")
def getBallCoordinates():
    return [0, 0]
def move(direction, speed, len):
    print("moving")

ballPos2d = [None] * 2

def distFromBall(focal, width, px):
    dist = focal*width/px
    return dist

def getDirection(ball_x):
    if ball_x >= 0 and ball_x < 128:
        return -2
    elif ball_x >= 128 and ball_x < 256:
        return -1
    elif ball_x >= 256 and ball_x < 384:
        return 0
    elif ball_x >= 384 and ball_x < 512:
        return 1
    elif ball_x >= 512 and ball_x <= 640:
        return 2

while(ballInView()):
    
    dist = distFromBall(focal, 7, px)
    
    if getDirection(getBallCoordinates()) < 0:
        while(getDirection(getBallCoordinates()) < 0):
            turnLeft()
        goToGoal()
    
