# -*- coding: utf-8 -*-
"""Activity1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Kr99a5WDTeLh2DC-nOMoa5zE-pb9E2C9
"""

# Creating class
class Compute:
  def __init__(self, a, b):
    self.a = a
    self.b = b

  # compute methods
  def add(self):
    return self.a + self.b

  def multiply(self):
    return self.a * self.b

  def subtract(self):
    return self.a - self.b

  def divide(self):
    return self.a / self.b

 # Instance of compute class
my_compute = Compute(9, 3)

def test(values):
   print (values.add())
   print (values.multiply())
   print (values.subtract())
   print (values.divide())

test(my_compute)