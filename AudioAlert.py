from playsound import playsound

PATH_AUDIO_CHUSO = 'CHUSO EL PATH DE TU AUDIO VA AQUI'
PATH_AUDIO_CHAT = 'CHUSO EL PATH DEL AUDIO PARA EL CHAT VA AQUI'

def alert_turnoChuso():
    playsound(PATH_AUDIO_CHUSO)

def alert_turnoChat():
    playsound(PATH_AUDIO_CHAT)