from playsound import playsound

PATH_AUDIO_CHUSO = "./pingo.mp3"
PATH_AUDIO_CHAT = "./conio.mp3"

def alert_turnoChuso():
    playsound(PATH_AUDIO_CHUSO)

def alert_turnoChat():
    playsound(PATH_AUDIO_CHAT)