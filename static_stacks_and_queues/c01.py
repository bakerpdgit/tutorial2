# NOTE: this code uses global variables where necessary as a conceptual exercise
# Tutorial 3 demonstrates better implementations using classes

def is_empty():
  return top == -1


def is_full():
  return top == MAXSIZE - 1


def push(item):
  global top
  if is_full():
    raise Exception("Stack overflow error")
  top += 1
  stack[top] = item


def pop():
  global top
  if is_empty():
    raise Exception("Stack empty error")
  output = stack[top]
  top -= 1
  return output


def peek():
  if is_empty():
    raise Exception("stack empty error")
  return stack[top]


###############
# MAIN PROGRAM
###############

MAXSIZE = 3
stack = [0] * MAXSIZE
top = -1

push(5)
push(4)
push(3)

print("Full check:", is_full(), ", Empty check:", is_empty())  # True, False

try:
  push(2)
except Exception as err:
  print(err)

print(peek())  # 3
print(pop())   # 3

print("Full check:", is_full(), ", Empty check:", is_empty())

for _ in range(2):
  print(pop())
print("Full check:", is_full(), ", Empty check:", is_empty())

try:
  pop()
except Exception as err:
  print(err)
