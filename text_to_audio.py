from  gtts import gTTS 
import os

mytext="Hello everyone. How are you doing"
language='en'

myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save("welcome.mp3")