import speech_recognition as sr
import pyttsx3, pywhatkit
import random
import pyautogui as pg
import time


from vocabulario import *



listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

name = ['coco','coro','x']
estadoJarvis = True
rec = ''


##########   PyAutoGui   ##########

def escribir(texto):
    pg.typewrite(f'{texto}')

def abrirPc(texto,tiempo = 1):
    pg.hotkey('win')
    pg.typewrite(f'{texto}')
    time.sleep(tiempo/2)
    pg.hotkey('enter')
    time.sleep(tiempo*3)

def clickOn(ub , min = False):
    pg.moveTo(ubicacion[ub])
    pg.click()
    if min:
        pg.moveTo(ubicacion['minimizar'])
        pg.click()


##########   Func Especiales   ##########

def cleanMensaje(s):
    s = s.lower()
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ü", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def ifIn(lista, valor,borrar = False):
    global rec

    for i in lista:
        if i in valor:
            if borrar:
                rec = rec.replace(i, '')
            return True
    return False


##########   VOZ   ##########

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()


def escuchar():
    global estadoJarvis,name,rec

    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("Escuchando...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice,language='es-ES',)

            rec = cleanMensaje(rec)
            print(rec)
            
            if ifIn(name,rec,True):
                estadoJarvis = comandos()
                 
    except:
        pass
    return estadoJarvis

def modoEscribir():
    global estadoJarvis,name,rec

    rec = input('>> ')

    if ifIn(name,rec,True):
        estadoJarvis = comandos()
    
    return estadoJarvis


def comandos():
    global rec,voz

    

    notEncontrarPalabra = True
    for i in range(int(len(palabras)/2)):
        pos = i*2
        if ifIn(palabras[pos], rec):
            hablar(random.choice(palabras[pos+1]))
            notEncontrarPalabra = False
            break    
    if notEncontrarPalabra:
        hablar("Vuelve a intentarlo, no reconozco: " + rec)
        return True

    if ifIn(palabras[0], rec,True):
        music = rec
        hablar(random.choice(palabras[1]) + music)
        print(random.choice(palabras[1]) + music)
        pywhatkit.playonyt(music)

    elif ifIn(palabras[2], rec):
        return False
    
    elif ifIn(palabras[4], rec):
        voz = not voz

    elif ifIn(palabras[6],rec):
        abrirPc('spotify')
        clickOn('lupitaCancionSpotify')
        time.sleep(2)
        clickOn('buscarCancionSpotify')
        clickOn('buscarCancionSpotify')
        clickOn('buscarCancionSpotify')
        time.sleep(2)
        escribir('top 50 global')
        time.sleep(4)
        clickOn('reproducirBusquedaDeCancionSpotify',min=True)

    elif ifIn(palabras[8],rec):
        abrirPc('spotify')
        clickOn('siguienteCancionSpotify')
    elif ifIn(palabras[10],rec):
        abrirPc('spotify')
        clickOn('anteriorCancionSpotify')

    if ifIn(palabras[12], rec,True):
        hablar(random.choice(canciones))
        



    elif ifIn(palabras[14],rec):
        for i in range(20):
            pg.hotkey('volumedown')
    
    elif ifIn(palabras[16],rec):
        for i in range(20):
            pg.hotkey('volumeup')
    elif ifIn(palabras[22],rec):
        pg.hotkey('space')
    
    return True






def runJarvis():
    global estadoJarvis,voz
    while estadoJarvis:
        if voz:
            #input('Toca cualquier letra para continuar')
            estadoJarvis = escuchar()
        else:
            estadoJarvis = modoEscribir()


voz = False
runJarvis()

