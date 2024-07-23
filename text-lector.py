from pyttsx3 import init
engine = init()
engine.getProperty('volume')
engine.setProperty('volume', -0.50)
engine.say("hello world")
engine.runAndWait()
