from threading import Thread
import time


class myThread(Thread):
 	"""docstring for myThread"""
 	def __init__(self, downtime, jump):
 		super(myThread, self).__init__()
 		self.downtime=downtime
 		self.jump=jump

 	def run(self):
 		while self.downtime:
 			time.sleep(self.jump)
 			self.downtime-=1

try:
 	thread1 = myThread(10, 1)
 	thread1.start()
except:
 	print("Error")