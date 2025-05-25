import os
import eel

eel.init('www')

os.system('start chrome.exe --app="https://localhost:8000/index.html"')

eel.start('index.html', mode='chrome', host='localhost', block=True)
