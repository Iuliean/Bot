from .resources.last_names import last_names
from .resources.first_names_male import first_names_male
from .resources.first_names_female import first_names_female
from numpy import random

def generate_male():
    print (first_names_male[random.randint(0,len(first_names_male))] +" "+last_names[random.randint(0,len(last_names))])
    return (first_names_male[random.randint(0,len(first_names_male))] +" "+last_names[random.randint(0,len(last_names))])

def generate_female():
    print (first_names_female[random.randint(0,len(first_names_female))] +" "+last_names[random.randint(0,len(last_names))])
    return (first_names_female[random.randint(0,len(first_names_female))] +" "+last_names[random.randint(0,len(last_names))])
