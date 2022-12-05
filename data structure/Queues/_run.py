import QueuesConstructor

my_queue = QueuesConstructor.Queues(4)

my_queue.enqueue(5)
#my_queue.print_queue()

print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())