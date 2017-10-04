import time,sys
import Queue as queue
from multiprocessing.managers import BaseManager

#create QueueManager
class QueueManager(BaseManager):
	pass
#this QueueManager just gets Quene from net,so only needs name
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#conneting the service which run the test_master.py
server_addr='127.0.0.1'
print('Connect tp server %s..'% server_addr)

m=QueueManager(address=(server_addr,5000),authkey=b'abc')

#connect net

m.connect()

#get Object of queue
task=m.get_task_queue()
result=m.get_Result_queue()


for i in range(10):
	try:
		n=task.get(timeout=1)
		print('run task %d*%d..'%(n,n))
		r='%d * %d =%d' %(n,n,n*n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('task queue is empty')

print('worker exit')

