import random,time
import Queue as queue
from multiprocessing.managers import BaseManager

#send msg queue
task_queue=queue.Queue()

#receive msg queue
result_queue=queue.Queue()

#QueueManager extends from BaseManager
class QueueManager(BaseManager):
	pass
#register queues to net,callable connect with Queue Object
QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)

#bind 5000port and set the identifying code as 'abc'
manager=QueueManager(address=('',5000),authkey=b'abc')

#start queue

manager.start()

#get Object from net who is request the Queue
task=manager.get_task_queue()
result=manager.get_result_queue()

#put the mission

for i in range(10):
	n=random.randint(0,10000)  #0<n<10000
	print('put task %d...'%n)
	task.put(n)
#get results from result queue
print('Try get results...')
for i in range(10):
	r=result.get(timeout=10)
	print('Result:::%s'%r)
#close
manager.shundown()
print('master exit')
