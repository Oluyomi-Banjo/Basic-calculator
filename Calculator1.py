def add(n1, n2):
    return (n1+n2)

def sub(n1, n2):
    return (n1-n2)
   
def mul(n1, n2):
    return (n1*n2)

def div(n1, n2):
    return (n1/n2)
should_continue=True
n1 = int(input(f"What's the first Number"))
while should_continue:
    options ={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
        }

    n2 = int(input(f"What's the second Number"))

    key=""
    for keys in options:
        key += keys+", "
    operation=input(f"Which of these operations would you like to perform {key}\n")
    print(f"{n1} {operation} {n2}")

    calcfunction = options[operation]
    answer = calcfunction(n1, n2)
    print(answer)
    restart = (input(f"would you like to continue with this number or start over? Y/N")).upper()

    if restart =="Y":
        n1 = answer
    else:
        should_continue = False

    