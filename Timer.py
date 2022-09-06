from lib2to3.pgen2.token import NAME
import time
from ChusoNames import * 

def cuenta_atras_chuso(t):
    cuenta_atras(t, crear_mensaje_turno_chuso())

def cuenta_atras_chat(t):
    cuenta_atras(t, "Turno del chat!")

def cuenta_atras(t, msg):
    while(t):
        timefile = open("./counter.txt", "w")
        mins, secs = divmod(t, 60)
        timeformat = f"{msg} {mins:01d}:{secs:02d}"
        timefile.write(timeformat)
        timefile.close()
        time.sleep(1)
        t -= 1