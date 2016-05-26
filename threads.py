#import threading
from threading import Thread
import time

def timer (name, delay, repeat):
	print("Timer", name, "started")
	while repeat > 0:
		time.sleep(delay)
		print (name, " : ", str(time.ctime(time.time())))
		repeat-=1
	print("timer" + name + "scompleted")

def Main():
	t1 = Thread(target = timer, args=("timer1", 1, 5))
	t2 = Thread(target = timer, args=("timer2", 2, 5))
	t1.start()
	t2.start()

	print("Main completed")

if __name__ == '__main__':
	Main()
