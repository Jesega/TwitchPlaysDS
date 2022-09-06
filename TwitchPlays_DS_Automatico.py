# Written by DougDoug and DDarknut

# Hello! This file contains the main logic to process Twitch chat and convert it to game commands.
# The code is written in Python 3.X
# There are 2 other files needed to run this code:
    # TwitchPlays_KeyCodes.py contains the key codes and functions to press keys in-game. You should not modify this file.
    # TwitchPlays_Connection.py is the code that actually connects to Twitch. You should not modify this file.

# The source code primarily comes from:
    # Wituz's "Twitch Plays" tutorial: http://www.wituz.com/make-your-own-twitch-plays-stream.html
    # PythonProgramming's "Python Plays GTA V" tutorial: https://pythonprogramming.net/direct-input-game-python-plays-gta-v/
    # DDarknut's message queue and updates to the Twitch networking code

# Disclaimer: 
    # This code is NOT intended to be professionally optimized or organized.
    # We created a simple version that works well for livestreaming, and I'm sharing it for educational purposes.

##########################################################

TWITCH_CHANNEL = 'chusommontero'#'chusommontero' # Replace this with your Twitch username. Must be all lowercase.

##########################################################

from pickle import TRUE
import keyboard
import TwitchPlays_Connection
import pydirectinput
import random
import pyautogui
import concurrent.futures
from TwitchPlays_KeyCodes import *
from AudioAlert import *
from Timer import *

##########################################################

# MESSAGE_RATE controls how fast we process incoming Twitch Chat messages. It's the number of seconds it will take to handle all messages in the queue.
# This is used because Twitch delivers messages in "batches", rather than one at a time. So we process the messages over MESSAGE_RATE duration, rather than processing the entire batch at once.
# A smaller number means we go through the message queue faster, but we will run out of messages faster and activity might "stagnate" while waiting for a new batch. 
# A higher number means we go through the queue slower, and messages are more evenly spread out, but delay from the viewers' perspective is higher.
# You can set this to 0 to disable the queue and handle all messages immediately. However, then the wait before another "batch" of messages is more noticeable.
MESSAGE_RATE = 0.5
# MAX_QUEUE_LENGTH limits the number of commands that will be processed in a given "batch" of messages. 
# e.g. if you get a batch of 50 messages, you can choose to only process the first 10 of them and ignore the others.
# This is helpful for games where too many inputs at once can actually hinder the gameplay.
# Setting to ~50 is good for total chaos, ~5-10 is good for 2D platformers
MAX_QUEUE_LENGTH = 1  
MAX_WORKERS = 100 # Maximum number of threads you can process at a time 
thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)
timer_thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)
active_tasks = []

# CHUSO AQUÍ CAMBIAS LOS TIEMPOS
# Incremento de tiempo del chat (segundos) en cada cambio de turno (dejalo a 0 si no quieres que aumente el tiempo de cada turno)
incremento_turno_chat = 0
# Incremento de tiempo del chat (segundos) en cada cambio de turno (dejalo a 0 si no quieres que aumente el tiempo de cada turno)
incremento_turno_chuso = 0
# Tiempo con el que empezará el turno de chuso (segundos)
tiempo_chuso = 10
# Tiempo con el que empezará el turno del chat (segundos)
tiempo_chat = 10

pyautogui.FAILSAFE = False

##########################################################

# An optional count down before starting, so you have time to load up the game

#Cambia el valor de countdown para meter una cuaenta atrás
countdown = 0
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

t = TwitchPlays_Connection.Twitch();
t.twitch_connect(TWITCH_CHANNEL);

def handle_message(message):
    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        print("Got the message: [" + msg + "] from user [" + username + "]")

        # Now that you have a chat message, this is where you add your game logic.
        # Use the "HoldKey(KEYCODE)" function to press and hold down a keyboard key.
        # Use the "ReleaseKey(KEYCODE)" function to release a specific keyboard key.
        # Use the "HoldAndReleaseKey(KEYCODE, SECONDS)" function press down a key for X seconds, then release it.
        # Use the pydirectinput library to press or move the mouse

# CHUSO AQUÍ CAMBIAS LAS TECLAS
        if msg == "w": 
            HoldAndReleaseKey(W, 1)

        if msg == "a": 
            HoldAndReleaseKey(A, 1)

        if msg == "s": 
            HoldAndReleaseKey(S, 1)

        if msg == "d": 
            HoldAndReleaseKey(D, 1)

        if msg == "roll": 
            HoldAndReleaseBothKeys(W, SPACE, 0.2)

        if msg == "rollback": 
            HoldAndReleaseBothKeys(S, SPACE, 0.2)

        if msg == "rolldere": 
            HoldAndReleaseBothKeys(D, SPACE, 0.2)

        if msg == "rollizq": 
            HoldAndReleaseBothKeys(A, SPACE, 0.2)

        if msg == "mondongo": 
            HoldAndReleaseKey(G, 0.2)
            HoldAndReleaseKey(E, 0.2)

        if msg == "estus": 
            HoldAndReleaseKey(R, 0.5)

        if msg == "cam": 
            HoldAndReleaseKey(Q, 0.5)

        if msg == "mano": 
            pydirectinput.mouseDown(button="right")
            time.sleep(0.5)
            pydirectinput.mouseUp(button="right")

        if msg == "hit": 
            pydirectinput.mouseDown(button="left")
            time.sleep(0.5)
            pydirectinput.mouseUp(button="left")

        ####################################
        ####################################

    except Exception as e:
        print("Encountered exception: " + str(e))

def turno_chat(tiempo_chat):
    last_time = time.time()
    message_queue = []
    global thread_pool
    global timer_thread_pool
    global active_tasks
    alert_turnoChat()
    f = timer_thread_pool.submit(cuenta_atras, tiempo_chat)
    print('Turno del chat!')
    while not f.done():
        active_tasks = [t for t in active_tasks if not t.done()]

        #Check for new messages
        new_messages = t.twitch_receive_messages();
        if new_messages:
            message_queue += new_messages; # New messages are added to the back of the queue
            message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

        messages_to_handle = []
        if not message_queue:
            # No messages in the queue
            last_time = time.time()
        else:
            # Determine how many messages we should handle now
            r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
            n = int(r * len(message_queue))
            if n > 0:
                # Pop the messages we want off the front of the queue
                messages_to_handle = message_queue[0:n]
                del message_queue[0:n]
                last_time = time.time();

        # If user presses Shift+Backspace, automatically end the program
        if keyboard.is_pressed('shift+backspace'):
            exit()

        # Si pulsas Shift + p, el script se parará en el turno del chat
        if keyboard.is_pressed('shift+p'):
            # Si pausamos borramos la cola de mensajes para que no quede basura
            message_queue = []
            print('Pausado')
            pause = True
            while pause:
                # Si pulsas Shift + o, el script se reanudará en el turno del chat
                if keyboard.is_pressed('shift+o'):
                    pause = False
                    print('Reanudado')

        if not messages_to_handle:
            continue
        else:
            for message in messages_to_handle:
                if len(active_tasks) <= MAX_WORKERS:
                    active_tasks.append(thread_pool.submit(handle_message, message))
                else:
                    print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')

def turno_chuso(t):
    global timer_thread_pool
    alert_turnoChuso()
    print('Turno del chingo montenegro!')
    cuenta_atras(t)

while True:
    turno_chuso(tiempo_chuso)
    turno_chat(tiempo_chat)
    tiempo_chuso += incremento_turno_chuso
    tiempo_chat += incremento_turno_chat