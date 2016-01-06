#!/usr/bin/python

def Hello(name):
   print("Hello, {0}!".format(name))

class Person():
    def __init__(self, name):
        self.name = name

    def hello(self, name="Kino"):
    	print("{0} says hello to {1}!".format(self.name, name))

zhou = Person("Zhou")
Hello(zhou.name)
zhou.hello()
