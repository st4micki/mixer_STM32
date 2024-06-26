This project lets user control windows audio mixer through physical knobs. Desktop application is written in python.
Python code uses comtypes, pycaw, pyserial and customtkinter packages.
Hardware part of the projest is based on STM32F3R8 microcontroller and features 4 linear poteniometers.

Desktop app features:
- User can choose COM port to which STM32 is plugged in.
- Potentiometers 2-4 control volumes of Spotify desktop app, Discord and Google Chrome
- User can choose which app's volume is controlled by Potentiometer1

Microcontroller software features:
- Serial communication with python desktop app through UART and built in USB connector
- Knob position reading using 4 ADC channels and DMA
- Signal filtering by a software low-pass filter

STM32R8 pinout:
Potentiometer 1 - PB0
Potentiometer 2 - PB1
Potentiometer 3 - PB13
Potentiometer 4 - PB11
