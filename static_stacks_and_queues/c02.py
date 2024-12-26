# NOTE: this code uses global variables where necessary as a conceptual exercise
# Tutorial 3 demonstrates better implementations using classes

def is_empty():
  return top == -1


def is_full():
  return ________________________


def push(item):
  global top
  if __________():
    raise Exception("Stack overflow error")
  top += ____
  stack[________] = item


def pop():
  global top
  if __________():
    raise Exception("Stack empty error")
  output = __________[top]
  _________ -= 1
  return output


def peek():
  if ______________:
    raise Exception("stack empty error")
  return stack[top]


def matches(opening, closing):
  opens = "({["
  closes = ")}]"
  return opens.index(opening) == closes.index(closing)

###############
# MAIN PROGRAM
###############


MAXSIZE = 100
stack = [0] * MAXSIZE
top = _____

expression = input()
balanced = True

for char in expression:

  if char in "({[":
    push(_____)

  elif char in ")}]":
    if is_empty():
      balanced = False
      break
    top_char = _____()
    if not matches(top_char, ____):
      balanced = False
      break

print(balanced)
