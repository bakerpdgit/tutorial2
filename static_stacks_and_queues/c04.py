# NOTE: this code uses global variables where necessary as a conceptual exercise
# Tutorial 3 demonstrates better implementations using classes

def is_empty():
  return queue_size == 0


def is_full():
  return queue_size == ____________


def enqueue(item):
  global tail, queue_size
  if ___________():
    raise Exception("Queue full error")
  tail = (tail + ______) % ________
  queue[tail] = item
  queue_size += ____


def dequeue():
  global head, queue_size
  if is_empty():
    raise Exception("Queue empty error")
  head = (_________ + 1) % ________
  queue_size -= ____
  return queue[_________]


###############
# MAIN PROGRAM
###############


MAXSIZE = 10
queue = [0] * MAXSIZE
head = -1
tail = -1
queue_size = 0

for i in range(9):
  enqueue(i)

print(str(queue))

while not is_empty():
  dequeue()

enqueue(9)
enqueue(10)

print(str(queue))
