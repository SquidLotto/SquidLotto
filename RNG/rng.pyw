#imports
import PySimpleGUI as sg
import secrets

#themebuilder
squidlotto   = {'BACKGROUND': '#16171B',
                'TEXT': '#EA325E',
                'INPUT': '#191A1E',
                'TEXT_INPUT': '#36C688',
                'SCROLL': '#191A1E',
                'BUTTON': ('white', '#EA325E'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}
sg.theme_add_new('SquidTheme', squidlotto)
sg.theme('SquidTheme')

#GUI
layout = [  [sg.Image(r"logo.png", s=(None, 50))],
            [sg.Text('SQTTO Random Number Gen', font=("",16))],
            [sg.Text('Start', size=(5, 1), text_color='white'),sg.InputText(key="start",default_text="1")],
            [sg.Text('End', size=(5, 1), text_color='white'),sg.InputText(key="end",default_text="45000")],
            [sg.Text('')],
            [sg.Button('Draw Winning Token', font=("",16))],
            [sg.Text('WINNING TOKEN', text_color='#36C688', font=("",16)),sg.Text('00000', key="Number" , size=(0,1), font=("",36))]]

window = sg.Window('Squid Lotto Randomizer', layout, no_titlebar=True, grab_anywhere=True, element_justification='c',)

#Functions
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == "Draw Winning Token":
        rng = secrets.SystemRandom()
        window["Number"].update(rng.randrange(int(values["start"]), int(values["end"]) + 1))

window.close()
