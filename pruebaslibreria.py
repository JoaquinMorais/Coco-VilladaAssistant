import keyboard
import speech_recognition as sr
import pyttsx3, pywhatkit


listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)





def escuchar():
    global estadoJarvis
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('You Pressed A Key!')
                return 'si' 
            voice = listener.listen(source)
            rec = listener.recognize_google(voice,language='es-ES',)
            print(rec)
    except:
        pass

def runJarvis():
    estadoJarvis = True
    while estadoJarvis:
        try:
            
            estadoJarvis = escuchar()
        except:
            break
        
    

runJarvis()