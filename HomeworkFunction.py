#FUNCTIE CU PARAMETRII NEDEFINITI

def function(*args,**kwargs):
    return(sum(x for x in args if type(x) == int))

print(function(1,-3,5,"abc",[12,56,"cad"]))
print(function())
print(function(2,4,"abc",param1=2))

#FUNCTII RECURSIVE

def sum_upto(n):
    return n + sum_upto(n-1) if n else 0

print(sum_upto(10))

def sum_even(n):
    count = 0
    for i in range(0, n + 1):
        if(i % 2 == 0):
            count += i
    return count

print(sum_even(10))

def sum_odd(n):
    count = 0
    for i in range(0, n):
        if(i % 2 != 0):
            count += i
    return count

print(sum_odd(10))


# FUNCTIE CARE CITESTE DE LA TASTATURA
def user_inp():

    user_input = input("Give me a number")
    while user_input == None or type(user_input) is not float:

        try:
            user_input = float(user_input)
            print("Your number is", user_input, "!")

        except ValueError:
            return 0

print(user_inp())









