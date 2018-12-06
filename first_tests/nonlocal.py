def function1():

    def function2():

        nonlocal x
        x = 5
    x = 1
    function2()
    print(x)


print("HI")
function1()
