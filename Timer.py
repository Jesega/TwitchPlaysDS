import time

def cuenta_atras(t):
    while(t):
        timefile = open("./counter.txt", "w")
        mins, secs = divmod(t, 60)
        timeformat = f"{mins:01d}:{secs:02d}"
        timefile.write(timeformat)
        timefile.close()
        time.sleep(1)
        t -= 1