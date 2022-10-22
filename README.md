
# TwitchPlaysDS
## Descipción
Este proyecto se compone de una serie de scripts modificados para que los usuarios del chat de un streamer puedan jugar al Dark Souls a través de mensajes del chat. Concretamente, se hizo a petición del streamer de Twitch [chusommontero](https://www.twitch.tv/chusommontero)

Sin embargo, con un par de modificaciones puede generalizarse el uso para cualquier propósito y usuario.

## Instalación
Descargar la carpeta raíz entera TwitchPlays_DS_Automatico.py y desde la carpeta ejecutar el comando ```python3 TwitchPlays_DS_Automatico.py``` or ```python TwitchPlays_DS_Automatico.py```. Si el archivo no puede ser ejecutado, instalar todos los módulos que falten que se indiquen en el mensaje de error. (WARNING: si quieres que se reproduzcan sonidos correctamente necesitas instalar version  la 1.2.2 del módulo playsound, con el comando ```pip install playsound==1.2.2```)

## Uso
Hay dos modos de ejecución:
 - Automático: los turnos del streamer y del chat se van cambiando automáticamente. Hay que ejecutar ```TwitchPlays_DS_Automatico.py``` y configurar las variables ```tiempo``` de TwitchPlays_DS_Automatico.py para ajustar los tiempo de cada turno. El tiempo de cada turno puede modificarse a cada turno con las variables ```incremento_turno```.  Al principio de cada turno sonará uno de los sonidos configurados en ```AudioAlert.py``` y se mostrará un mensaje en la consola. 
 - Manualmente: el turno por defecto será del chat y habrá que parar el script para que el streamer tenga el control. Hay que ejecutar ```TwitchPlays_DS_Manual.py```
 
 Para la seguridad del streamer se puede parar el funcionamiento del script pulsando las teclas ```shift+p``` y se puede reanudar con las teclas ```shift+o```
 
## Autores y reconocimiento
Los sripts iniciales se obtuvieron de [DogDoug](https://www.dougdoug.com/twitchplays).
Gracias a Chuso ( [chusommontero](https://www.twitch.tv/chusommontero) ) por el reconocimiento y la oportunidad de ayudarle.
Código final producido por Jesega ( (Jesús Serrano Gallán)[https://www.linkedin.com/in/jes%C3%BAs-serrano-gall%C3%A1n-b768a3175/] )
