import stack

def is_pringles_out():
    return stack.is_empty() == True
    #return stack.size() == 0 --> this also works

def eat():
    eaten = stack.pop()
    print(f"The pringle {eaten} was eaten")


def create_new_pringle():
    print("Creating a new pringle stack")
    for i in range(100,0,-1):
        print(f"Adding the chip:{i} to the stack")
        stack.push(i)

def remains():
    return stack.size()


def main():
    create_new_pringle()
    while not is_pringles_out():
        chip_remains = remains()
        print(f"Remains:{chip_remains}")
        total_to_eat = int(input("How many chips do you want to eat:"))
        if total_to_eat >  chip_remains:
            print(f"You cant do that! There are only {chip_remains} chip remains")
            continue
        else:
            for repeat in range(total_to_eat):
                eat()
        

#call the main
main()