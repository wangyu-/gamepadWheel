import math

range_degree=720.0
deadzone_degree=5.0
	
def variables():
	global v
	global round
def cal(a):
	if a>math.pi:
		return a-math.pi
	if a<-math.pi:
		return a+math.pi
	return a;
def update():
	global round,v

	vJoy[0].setButton(0, xbox360[0].a)
	vJoy[0].setButton(1, xbox360[0].b)
	vJoy[0].setButton(2, xbox360[0].x)
	vJoy[0].setButton(3, xbox360[0].y)
	vJoy[0].setButton(4, xbox360[0].leftShoulder)
	vJoy[0].setButton(5, xbox360[0].rightShoulder)
	vJoy[0].setButton(6, xbox360[0].start)
	vJoy[0].setButton(7, xbox360[0].back)
	
	vJoy[0].setButton(8, xbox360[0].down)
	vJoy[0].setButton(9, xbox360[0].up)
	vJoy[0].setButton(10, xbox360[0].left)
	vJoy[0].setButton(11, xbox360[0].right)

	vJoy[0].y=-vJoy[0].axisMax +2*xbox360[0].leftTrigger* vJoy[0].axisMax
	vJoy[0].z=-vJoy[0].axisMax +2*xbox360[0].rightTrigger* vJoy[0].axisMax
	r= math.sqrt(xbox360[0].leftStickX* xbox360[0].leftStickX  +  xbox360[0].leftStickY* xbox360[0].leftStickY)
	if r<0.25:
		v=0
		round=0
	else:
		u= -(-math.atan2(xbox360[0].leftStickX, xbox360[0].leftStickY))  /math.pi
		if u<-0.5 and v>0.5 :
			round=round+1
		elif u>0.5 and v<-0.5:
			round=round-1
		v=u
	x= (v+round*2)/ (range_degree/360.0) 
	if x>1:
		x=1
	if x<-1:
		x=-1
	dz=deadzone_degree/range_degree/2
	
	absx=abs(x)
	if x==0:
		sign=0
	else:
		sign=x/absx
	
	if(absx<dz):
		absx=0
	else:
		absx=(absx-dz)/(1-dz)
		
	adjusted_x=absx*sign

	vJoy[0].x=adjusted_x*vJoy[0].axisMax
	
	diagnostics.watch(r)
	diagnostics.watch(x)
	diagnostics.watch(adjusted_x)
	diagnostics.watch(v)
	diagnostics.watch(round)
	diagnostics.watch(vJoy[0].x)

if starting:
	global round,v
	round=0
	v=0
	freeTrack.update += update

