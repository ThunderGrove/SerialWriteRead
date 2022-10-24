import serial
import threading

from tkinter import *

class serialThread(object):
	def __init__(self, interval=1):
		self.interval=interval
		thread=threading.Thread(target=self.run,args=())
		thread.daemon=True
		thread.start()
	def run(self):
		global var1
		ser=serial.Serial('/dev/ttyUSB0',115200)#115200
		count=0
		serialBuffer=[-1,-1,-1,-1]
		while True:
			for line in ser.read():
				match count:
					case 0:
						if line==115:
							count=count+1
						else:
							print('Invalid start 0')
					case 1:
						if line==116:
							count=count+1
						else:
							print('Invalid start 1')
							count=0
					case 2:
						if line==114:
							count=count+1
						else:
							print('Invalid start 2')
							count=0
					case 3:
						if line==116:
							count=count+1
						else:
							print('Invalid start 3')
							count=0
					case 4:
						serialBuffer[0]=line
						count=count+1
					case 5:
						serialBuffer[1]=line
						count=count+1
					case 6:
						serialBuffer[2]=line
						count=count+1
					case 7:
						serialBuffer[3]=line
						count=count+1
					case 8:
						if line==101:
							count=count+1
						else:
							print('Invalid end 0')
							count=0
							serialBuffer[0]=-1
							serialBuffer[1]=-1
							serialBuffer[2]=-1
							serialBuffer[3]=-1
					case 9:
						if line==110:
							count=count+1
						else:
							print('Invalid end 1')
							count=0
							serialBuffer[0]=-1
							serialBuffer[1]=-1
							serialBuffer[2]=-1
							serialBuffer[3]=-1
					case 10:
						if line==100:
							count=0
						else:
							print('Invalid end 2')
							count=0
							serialBuffer[0]=-1
							serialBuffer[1]=-1
							serialBuffer[2]=-1
							serialBuffer[3]=-1
				print(serialBuffer)
				if serialBuffer[0]!=-1 and serialBuffer[1]!=-1 and serialBuffer[2]!=-1 and serialBuffer[3]!=-1:
					var1.set(serialBuffer[0])
					var2.set(serialBuffer[1])
					var3.set(serialBuffer[2])
					var4.set(serialBuffer[3])
					root.update_idletasks()
		ser.close()

root=Tk()

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()

btn7=1
btn10=1

R1=Radiobutton(root,text="Button 1 status",variable=var1,value=btn7,state=DISABLED)
R1.pack(anchor=W)
R2=Radiobutton(root,text="Button 2 status",variable=var2,value=btn10,state=DISABLED)
R2.pack(anchor=W)

label1=Label(root)
label1.config(text="Analog 1")
label1.pack()

scale1=Scale(root,variable=var3,state=DISABLED,from_=0,to=255,orient=HORIZONTAL)
scale1.pack(anchor = CENTER)

label2=Label(root)
label2.config(text="Analog 2")
label2.pack()

scale2=Scale(root,variable=var4,state=DISABLED,from_=0,to=255,orient=HORIZONTAL)
scale2.pack(anchor = CENTER)

bg=serialThread()

root.mainloop()

