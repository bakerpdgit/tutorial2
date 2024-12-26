# NOTE: this code uses global variables where necessary as a conceptual exercise
# Tutorial 3 demonstrates better implementations using classes

def is_empty():
  return head == tail


def is_full():
  return tail == MAXSIZE - 1


def enqueue(item):
  global tail
  if is_full():
    raise Exception("Queue full error")
  tail += 1
  queue[tail] = item


def dequeue():
  global head
  if is_empty():
    raise Exception("Queue empty error")
  head += 1
  return queue[head]


def queue_repr():
  return str(queue)

###############
# MAIN PROGRAM
###############


MAXSIZE = 10
queue = [0] * MAXSIZE
head = -1
tail = -1

for i in range(9):
  enqueue(i)

print("Full check:", is_full())

while not is_empty():
  print(dequeue())

print("Empty check:", is_empty())

enqueue(9)

# can you see why this will raise an exception even though the queue only
# contains one element?
try:
  enqueue(10)
except Exception as err:
  print(err)
