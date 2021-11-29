import math # This is so i can access all the trigonometric functions 

import streamlit as st
import numpy as np
import pandas as pd



def degrees_to_radians(x): 
    """This is to convert the users imput of degrees to radians so that the answer can be calculated."""
    return x*math.pi/180 

def radians_to_degrees(a): 
    """This is to convert the calculated answer from radians to degrees so they get the answer in the units they are looking for.""" 
    return (a/math.pi)*180


st.write('## Here is my first calculator')

symbol = st.selectbox("What sum would you like to do?", ['TRIG', 'RECT']) #Primary question


if symbol == "TRIG":
    answer = st.selectbox("which trig?", ["COS", "TAN", "SIN", "ACOS", "ASIN", "ATAN"]) #Secondary question
    if answer == "COS": #If a user st.text_inputs the answer of cos the OUTPUT will be as follows
        x = float(st.text_input("Angle?"))
        x_rad = degrees_to_radians(x)
        hyp = float(st.text_input("Hypotenuse?"))
        cosAnswer = hyp * math.cos(x_rad)
        st.write(cosAnswer)
