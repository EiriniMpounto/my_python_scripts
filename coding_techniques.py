''''The current file is a creation of Irene 
Bounto and contains basic coding techniques 
and initial python knowledge.
'''

'''First of all before we do any coding we need
to learn the basic logic of the software, therefore
the current line of code reveeals the Zen of python
writte by Tim Peters
'''
import this #script by Tim


# FUNCTIONS
'''Functions are like a blender or a bread 
maker, you put data into it, does things with 
the information and retuns them into a result, 
as it will be shown in the following lines.
'''
# creating the function 
def my_function(x):
    y=x**x
    print(x, 'raised to the power of', x, 'is', y)
    return y
# calling the function
result=my_function(5)
print(result)

# MODULES
'''Modules are text files that can contain any 
kind of Pyhton code, but a module usualy organizes 
tools that work in a different way for example'''
import math
math.pi
print('Pi is:',math.pi)

# CLASSES
'''A class is similar to both a factory and
a blueprint in that it makes copies of itself
'''
class SayMyName:
    def __init__(self, myname):
        self.myname = myname
    def say(self):
        print('Hello, my name is', self.myname)
name1 = SayMyName('Aahz')
# calling the function
name1.say()

