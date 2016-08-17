#read pos return orinetaion
#you will have 8 directions     _\|/_
#                                /|\
#and stop function when the child reaches the destination
#x1, y1 are your current location
#x2, y2 are the locatin of the parent
#where y+ is north, y- south ,x+ east, x- south for  both parent and child
#fucntion GetOrientation returns the orientaion of the child (N,S,E,W,NE,NW,SE,SW)
#function DispDirection, diplaies the direction to the child to walk to base on the child and parent positions and
#on the child orientaion, in the form of arrows in 8 directions (Right,Left,Forward,Backward,RF,RB,LF,LB)
# both x and y cannot be negative 
import math
phi  = 31.2622771 
dictn = {'N':0, 'S': 1, 'E':2 ,'W':3,'NE':4,'NW':5,'SE':6,'SW':7,'STOP':8} #dictionary
#Orientaion will be the same chars
Dir = [ ['F' ,'B','L','R','LF','RF','LB','RB'], ['B' ,'F','R','L','RB','LB','RF','LF'] , ['R' ,'L','F','B','RF','RB','LF','LB'], \
['L' ,'R','B','F','RB','LF','RB','RF'] , ['RF' ,'RB','LF','LB','F','R','L','B'], ['LF' ,'LB','RB','RF','R','F','B','L']\
, ['LB' ,'LF','RF','RB','L','B','F','R'], ['RB' ,'RF','LB','LF','B','L','R','F'],['STOP','STOP','STOP','STOP','STOP','STOP','STOP','STOP']]
def GetAngle(): #return the angle based on the hardware(compass + processor) used 
        return 250
def ConvertToX(lat,lon): #convet for GPS latitude and longitude to X 
	#x = lon  * r 
	x = lon * 6371000
	return  x  
def ConvertToY(lat ,lon): #convet for GPS latitude and longitude to X 
    	#y = lat * r * cos(phi0)
	y = lat * 6371000 * math.cos((3.14*phi)/180.0)
	return y
def GetOrientation(): #wrapper function convert angle value from compass to decrete directions 
    angle = GetAngle()
    angle_str = 'None'
    if ( (angle <= 20) or (angle >= 340) ):
        angle_str = 'N'
    elif((angle > 20) and (angle <= 70) ):
        angle_str = 'NE'
    elif((angle > 70) and (angle <= 110)):
        angle_str = 'E'
    elif((angle > 110 ) and (angle <= 160)):
        angle_str = 'SE'
    elif((angle > 160 ) and (angle <= 200 )):
        angle_str = 'S'
    elif((angle > 200) and (angle <= 250)):
        angle_str = 'SW'
    elif((angle > 250) and (angle <= 290)):
        angle_str = 'W'
    elif((angle > 290) and (angle < 340) ):
        angle_str = 'NW'
    return  angle_str
def DispDirection(parentorin): #display the direction to follow, the output can be redirected any were (file, socket ....)
    childorin = GetOrientation()
    print parentorin + " -> " + Dir[dictn[parentorin]][dictn[childorin]]
def GTG(x1,y1,x2,y2): #the main function that is called by user
    xabs = x1 - x2
    yabs = y1 - y2 
    if (xabs == 0):
        if(yabs == 0):
            DispDirection('STOP')
        elif(yabs > 0):
             DispDirection('S')
        elif (yabs < 0):
             DispDirection('N')
    elif (xabs > 0):    
        angle = math.tan(float(yabs)/float(xabs))
        if (angle <= 0.36 and angle >= -0.36):
            DispDirection('W')
        elif (angle >=  2.75 ):
            DispDirection('N')
        elif(angle <= -2.75):
            DispDirection('S')
        elif(angle < 2.75 and angle > 0.36 ):
            DispDirection('SW')
        elif(angle > -2.75 and angle < -0.36 ):
            DispDirection('NW')
                
    elif (xabs < 0):
        xabs = - xabs 
        angle = math.tan(float(yabs)/float(xabs))
        if (angle < 0.36 and angle > -0.36):
            DispDirection('E')
        elif (angle >=  2.75 ):
            DispDirection('N')
        elif(angle <= -2.75):
            DispDirection('S')
        elif(angle < 2.75 and angle > 0.36 ):
            DispDirection('SE')
        elif(angle > -2.75 and angle < -0.36 ):
            DispDirection('NE')
#Test Cases
#fetch form parent, then convert  
xp = ConvertToX(31.2703523,30.0028184)
yp = ConvertToY(31.2703523,30.0028184)
print 'xp = ' , xp
print 'yp = ', yp
#fetch from child, then convert 
xc = ConvertToX(31.2706474,30.0025345)
yc = ConvertToY(31.2706474,30.0025345)
print 'xc = ' , xc
print 'yc = ', yc

GTG(5,4,1,1) #SW -> RB
GTG(5,4,5,4) #STOP -> STOP
GTG(5,4,5,10)#N -> F
GTG(10,1,0,0)#W - > L 
GTG(1,1,10,10)#NE-> LF
GTG(1,1,2,100)#N -> F
GTG(4,4,5,4)#E - > R 
GTG(10,10,15,5)#SE - > LB
GTG(1,1,10,10)#NE -> RF
GTG(4,100,5,1)#S -> B
            
