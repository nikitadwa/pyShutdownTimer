import tkinter as tk
import os
import time

def shutdown():
    # Функция, вызываемая при нажатии кнопки "Shutdown"
    minutes = slider.get() # Получаем выбранное количество минут из слайдера
    seconds = minutes * 60 # Конвертируем минуты в секунды
    command = f"shutdown -s -t {seconds}" # Формируем команду shutdown
    os.system(command) # Вызываем команду shutdown

def sleep():
    # Функция, вызываемая при нажатии кнопки "Sleep"
    minutes = slider.get() # Получаем выбранное количество минут из слайдера
    seconds = minutes * 60 # Конвертируем минуты в секунды
    time.sleep(seconds)
    command = f"rundll32.exe powrprof.dll,SetSuspendState 0,1,0" # Формируем команду для перевода компьютера в режим сна с таймером
    os.system(command) # Вызываем команду


def cancel_shutdown():
    # Функция, вызываемая при нажатии кнопки "sd Cancel"
    os.system("shutdown -a") # Вызываем команду отмены shutdown

# Создание главного окна tkinter
window = tk.Tk()
window.geometry("300x250")

# Создание слайдера для выбора количества минут
slider = tk.Scale(window, from_=0, to=120, orient=tk.HORIZONTAL, length=200)
slider.pack()

# Создание кнопки "Shutdown"
shutdown_button = tk.Button(window, text="Shutdown", command=shutdown)
shutdown_button.pack()

# Создание кнопки "Sleep"
shutdown_button = tk.Button(window, text="Sleep", command=sleep)
shutdown_button.pack()

# Создание кнопки "sd Cancel"
cancel_button = tk.Button(window, text="Cancel", command=cancel_shutdown)
cancel_button.pack()

# Запуск основного цикла tkinter
window.mainloop()