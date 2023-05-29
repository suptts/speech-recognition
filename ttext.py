#!/usr/bin/env python3

import goslate

text = "Hello World"
#text = input("Please enter a string:\n")

gs = goslate.Goslate()
translatedText = gs.translate(text, "fr")
# translatedText = gs.translate(text, "ja")

print(translatedText)
#print(f'You entered {text} and in French  is {gs.translate(text, "fr")}')
