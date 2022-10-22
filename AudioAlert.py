from playsound import playsound

PATH_AUDIO_STREAMER = "./sound1.mp3"
PATH_AUDIO_CHAT = "./sound2.mp3"

def alert_turnoStreamer():
    playsound(PATH_AUDIO_STREAMER)

def alert_turnoChat():
    playsound(PATH_AUDIO_CHAT)