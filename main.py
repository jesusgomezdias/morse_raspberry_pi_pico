# -*- coding: utf-8 -*-
import machine
import time

MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "CH": "----",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
    "/": "-..-.",
    "\"": ".-..-.",
    "@": ".--.-.",
    "=": "-...-",
    "!": "−.−.−−",
}

texto = ""
palabra = input("Ingrese una palabra o texto a codificar: ")
for caracter in palabra:
    if caracter != " " and caracter in MORSE:
        texto += MORSE[caracter]
    else:
        texto += caracter
    texto += " "
tiempo_base = 0.1
led_onboard = machine.Pin(15, machine.Pin.OUT)
for letra in texto:
    if letra == ".":
        led_onboard.on()
        time.sleep(tiempo_base * 1)
        led_onboard.off()
    elif letra == "-":
        led_onboard.on()
        time.sleep(tiempo_base * 2)
        led_onboard.off()
    else:
        led_onboard.off()
        time.sleep(tiempo_base * 3)
    time.sleep(tiempo_base)


print("Texto codificado: {}".format(texto))

    
