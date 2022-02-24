import speech_recognition as sr
import pyttsx3
import pyautogui
import time 
pyautogui.PAUSE = 1
reconhecedor_supremo = sr.Recognizer()
nao_estou_rouco = True

with sr.Microphone() as microfone:
    engine = pyttsx3.init()
    while nao_estou_rouco:
        reconhecedor_supremo.adjust_for_ambient_noise(microfone)
        print('Say something:')
        try:
            audio_raptado = reconhecedor_supremo.listen(microfone)
            texto = reconhecedor_supremo.recognize_google(audio_raptado, language='pt-BR')
            print(texto)
        except:
            print('erro')
            engine.say('Desculpe, não entendi.')
            engine.runAndWait()
            audio_raptado = reconhecedor_supremo.listen(microfone)
            texto = reconhecedor_supremo.recognize_google(audio_raptado, language='pt-BR')
            print(texto)

        
        
        if texto == 'oi' or texto == 'Oi':
            engine.say('Oi, tudo bem?')
            engine.runAndWait()
            try:
                b = reconhecedor_supremo.listen(microfone)
                b_texto = reconhecedor_supremo.recognize_google(b, language='pt-BR')
                print(b_texto)
            except:
                engine.say('Desculpe nao entendi')
                b = reconhecedor_supremo.listen(microfone)
                b_texto = reconhecedor_supremo.recognize_google(b, language='pt-BR')
                print(b_texto)
            if b_texto == 'tudo' or b_texto == "Texto":
                engine.say('Que ótimo')
                engine.runAndWait()


        if texto == 'sair' or texto == 'Sair':
            engine.say('Saindo!')
            engine.runAndWait()
            nao_estou_rouco = False
        if texto == 'faça uma anotação' or texto == 'Faça uma anotação':
            pyautogui.press('win')
            pyautogui.write('bloco de notas')
            pyautogui.press('enter')
            time.sleep(4)
            
            c = reconhecedor_supremo.listen(microfone)
            c_texto = reconhecedor_supremo.recognize_google(c, language='pt-BR')
            pyautogui.write(c_texto)
            pyautogui.hotkey('ctrl','s')
            pyautogui.write('Arquivo2024')
            pyautogui.press('enter')

