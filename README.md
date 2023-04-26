# Senior-Design

Hello, welcome to Team 11 - Trash Boss' Senior Capstone project from 2022-23

The two separate codes within this project include:
  1. Bluetooth Main PWM App 4-19-23
  2. Trash_Boss_Android.aia

The first is the code written in micro python used to flash the raspberry pi pico w. The code includes initializing all of the pins on the microcontroller and setting them up with Pulse Width Modulation (PWM). The variables used in the code are then established, and then it starts the while loop. If the connection is established on any UART port, it enters the loop. It then constantly searches for UART strings as established in the code, each singifying a different command on the robot. 

The second is a code that can be imported into MIT App Inventor that will create the app UI for the tablet. At the moment the app will only work on Android devices for two reasons. The first is because the HC-05 module currently implemented with the device is a serial bluetooth connection, which IOS devices can not find. The second reason is that when an AT-09 module was tried, to broadcast a Bluetooth Low Energy (BLE) signal, but the MIT App companion base app doesn't support BLE connections. Nor does the IOS companion app support the extensons needed to connect to BLE devices.
