while True:
    userinput = input()
    total = 0
    for i in userinput.split():
        total += len(i)
    print(total / len(userinput.split()))
