animal_noises = {"dog": "woof", "cat": "meow", "bird": "tweet", "mouse": "squeek", "cow": "moo", "frog": "croak"}

num_noises_made = 0


def make_animal_noise(animal):
    global num_noises_made

    if animal in animal_noises:
      print(animal_noises[animal])
      num_noises_made = num_noises_made + 1
    else:
      print("Sorry, I don't know that animal")


while True:
    option = input("Enter animal, or enter nothing to end: ")
    if option == "":
        break
    make_animal_noise(option)
print(num_noises_made, "noises were made in total")
