from pyttsx3 import init
book = open(r"book.txt")
book_text = book.readlines()
engine = init()
for i in book_text:
    engine.say(i)
    engine.runAndWait()
