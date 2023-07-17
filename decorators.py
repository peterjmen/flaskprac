# python decorator function looks like, normal function
#  to control the calling of the function that was passed in
import time


def decorator_function(
    function,
):  #  allows for changing of function that is passed in, enabling adding additional functionality
    def wrapper_function():  # just wraps
        function()

    return wrapper_function


def delay_decorator(function):
    def function_wrapper():
        start = time.time()
        function()
        time.sleep(2)
        fin = time.time()
        time_taken = start - fin
        print(f"Time taken for function = {time_taken}")

    return function_wrapper


@delay_decorator  #  <- syntactic sugar aka decorated_function() = delay_decorator(say_greeting) // decorated_function()
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


say_hello()
say_bye()

# # primer on functions:
# # ?exp below
# #  sign is a python decorator - decrator and ad functionalities to functions, a function that will give additional functionality
# # @app.route("/")
# # def hello_world():
# #     return "<p>Hello, World!</p>"


# def add(n1, n2):
#     return n1 + n2


# def subtract(n1, n2):
#     return n1 - n2


# # ?python functions are first class objects
# # we can taket hese functions and build another function that uses them ie.


# def calcuclate(calc_function, n1, n2):
#     return calc_function(n1, n2)


# result = calcuclate(add, 1, 2)
# print(result)


# # nested functions
# def outer_function():
#     print("i'm outer")

#     # scope only availible inside the outer function so cant just do nested_function()
#     def nested_function():
#         print("I'm inner")

#     nested_function()  #  this can be done


# outer_function()

# # functions can be returned from other functions

# # to run function by using return


# # nested functions
# def outer_function():
#     print("i'm outer")

#     # scope only availible inside the outer function so cant just do nested_function()
#     def nested_function():
#         print("I'm inner")

#     return nested_function  #  this can be done


# inner_function = outer_function()
# inner_function()
