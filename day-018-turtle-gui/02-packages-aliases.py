# This will import everything from a module.
# This can be a bad idea as a large module can take time to load and chew up resources.
from turtle import *

# Ideally, only import what you are going to use:
from turtle import Turtle, Screen

# You can also set an alias for a module to reduce typing, especially for modules with long names:
import turtle as t
time = t.Turtle()