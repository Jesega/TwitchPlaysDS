import random

NAME = ["chuso", "chungo", "chingo", 
        "curro", "chucho"]
SURNAME = [ "montero", "mototruco", "montevideo", 
            "montenegro", "montapuercos"]

def crear_mensaje_turno_chuso():
    msg = "Turno del " + crear_nombre() + "!"
    return msg

def crear_nombre():
    n = random.choice(NAME)
    s = random.choice(SURNAME)
    return n + " " + s