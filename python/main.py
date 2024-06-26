import time
import customtkinter as ctk
from audio import Audio
from uart import Uart
from loop import MixerLoop
uart = None
program_on = False
chosen_game = None
process_names = ['']

ctk.set_default_color_theme('S:\\Python\\PythonWorkspace\\mixer07\\theme.json')
window = ctk.CTk()
font = ctk.CTkFont('Fixedsys', 12)
window.title('Mikser06')


colors = {"BACKGROUND": "#041f2b",
          "BUTOON": "#468B97'",
          "BUTTON_HOOVER": '#1D5B79',
          "START": '#B0D9B1',
          "START_HOOVER": '#79AC78'}

BACKGROUND = "#041f2b"
BUTTON = '#468B97'
BUTTON_HOOVER = '#1D5B79'
START = '#B0D9B1'
START_HOOVER = '#79AC78'


def loop():
    mixer_loop.loop(str(uart.readline()), audio)
    state_label.configure(text='Status:Running', text_color=colors['START'])
    window.after(10, loop)


def turn_off():
    mixer_loop.program_on_set_false()
    print("serial closed")
    uart.close()
    state_label.configure(text='Status:Press Start', text_color='#FFF5E0')


def uart_setup():
    global uart
    if com_entry.get() == '':
        com = 'COM4'
    else:
        com = 'COM' + str(com_entry.get())
    time.sleep(0.2)
    uart = Uart(com, 9600)
    window.after(0, audio_setup)


def choose_game():
    global chosen_game
    chosen_game = value_inside.get()
    print(chosen_game)


def get_sessions():
    audio.get_sessions()
    game_dropbox.configure(values=audio.process_names)


def audio_setup():
    audio.audio_setup(chosen_game)
    global program_on
    mixer_loop.program_on_set_true()
    window.after(0, loop)
    #


audio = Audio()
mixer_loop = MixerLoop()
# uart = Uart(port='')


stop_button = ctk.CTkButton(window, text='Stop', command=turn_off, width=265, fg_color=BUTTON, hover_color=BUTTON_HOOVER, font=font)
start_button = ctk.CTkButton(window, text='Start', command=uart_setup, width=265, fg_color='#79AC78', hover_color='#618264', font=font)
state_label = ctk.CTkLabel(window, text='Status:Press Start', font=font)
com_label = ctk.CTkLabel(window, text='COM', font=font)
com_entry = ctk.CTkEntry(window, placeholder_text="4", width=40, font=font)
value_inside = ctk.StringVar(window,'Select process')
game_dropbox = ctk.CTkOptionMenu(window,
                                 values=process_names,
                                 variable=value_inside,
                                 font=font,
                                 dropdown_font=font,
                                 width=160,
                                 anchor='w')
game_dropbox.configure(font=font, dropdown_font=font, width=160, anchor='w')
set_button = ctk.CTkButton(window, text='Set', command=choose_game, width=265,fg_color=BUTTON, hover_color=BUTTON_HOOVER, font=font)
refresh_button = ctk.CTkButton(window, text='Refresh', command=get_sessions, width=98,fg_color=BUTTON, hover_color=BUTTON_HOOVER, font=font)
specify_com_label = ctk.CTkLabel(window, text='Specify COM Port:', font=font)
game_choose_label = ctk.CTkLabel(window, text='Select main process:', font=font)
specify_com_label.grid(row=0, column=0, padx=20, pady=10)
com_label.grid(row=0, column=1, padx=(20,5), pady=10)
com_entry.grid(row=0, column=2, padx=(0,20), pady=10)
game_choose_label.grid(row=1, column=0, columnspan=2, sticky='w', padx=20, pady=(10,0))
game_dropbox.grid(row=2, column=0, columnspan=1, sticky='w', padx=(18,0), pady=(0,10))
refresh_button.grid(row=2, column=1, columnspan=2, padx=(5,20), pady=(0,10), sticky='w')
set_button.grid(row=3, columnspan=3, column=0, padx=10, pady=(0,10))
start_button.grid(row=4, columnspan=3, column=0, padx=10, pady=(0,10))
stop_button.grid(row=5, columnspan=3, column=0, padx=10, pady=(0,10))
state_label.grid(row=6, columnspan=3, column=0)

get_sessions()
time.sleep(3)
window.mainloop()





