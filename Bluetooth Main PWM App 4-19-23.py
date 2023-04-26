from machine import Pin, UART, PWM
import time

# Configure pins
led_pin = machine.Pin(15, machine.Pin.OUT)
PWMO = machine.Pin(20, machine.Pin.OUT) #Actuator push out
PWMI = machine.Pin(21, machine.Pin.OUT) #Actuator pull in
PWMLF = machine.Pin(14, machine.Pin.OUT) #Left DC Forward
PWMLB = machine.Pin(15, machine.Pin.OUT) #Left DC Back
PWMRF = machine.Pin(3, machine.Pin.OUT) #Right DC Forward
PWMRB = machine.Pin(2, machine.Pin.OUT) #Right DC Back
PWMBF = machine.Pin(16, machine.Pin.OUT) #DC Magnet On
PWMBB = machine.Pin(17, machine.Pin.OUT) #DC Magnet Off

# Create a PWM object with a frequency of 1000 Hz
pwmLED = machine.PWM(led_pin)
pwmLED.freq(1000)
pwmOUT = machine.PWM(PWMO)
pwmOUT.freq(1000)
pwmIN = machine.PWM(PWMI)
pwmIN.freq(1000)
pwmDCRF = machine.PWM(PWMRF)
pwmDCRF.freq(1000)
pwmDCRB = machine.PWM(PWMRB)
pwmDCRB.freq(1000)
pwmDCLF = machine.PWM(PWMLF)
pwmDCLF.freq(1000)
pwmDCLB = machine.PWM(PWMLB)
pwmDCLB.freq(1000)
pwmDCBF = machine.PWM(PWMBF)
pwmDCBF.freq(1000)
pwmDCBB = machine.PWM(PWMBB)
pwmDCBB.freq(1000)

led_pin.value(0)
PWMO.value(0)
PWMI.value(0)

uart = UART(0, 9600)
led = Pin(13, Pin.OUT)
#PWML = Pin(2, Pin.OUT)
#PWMR = Pin(6, Pin.OUT)

MAX = 65535
TOP = 32767
SLOW = 16384
STOP = 0
SPEED = 0

while True:
    if uart.any() > 0:
        data = uart.read()
        data=str(data)
        print(data)
        #led.value(1)
        #time.sleep(.5)
        #led.value(0)
        #time.sleep(.5)
        if "on" in data:
            led.value(1)
            print('LED on \n')
            uart.write('LED on \n')
        elif "off" in data:
            led.value(0)
            print('LED off \n')
            uart.write('LED off \n')
        elif "out" in data:
            pwmOUT.duty_u16(MAX)
            pwmIN.duty_u16(STOP)
            print('Actuator moving out \n')
            uart.write('Actuator moving out \n')
        elif "in" in data:
            pwmOUT.duty_u16(STOP)
            pwmIN.duty_u16(MAX)
            print('Actuator moving in \n')
            uart.write('Actuator moving in \n')
        elif "forward" in data:
            pwmDCBF.duty_u16(STOP)
            pwmDCBB.duty_u16(STOP)
            pwmDCLB.duty_u16(STOP)
            pwmDCRB.duty_u16(STOP)
            pwmDCLF.duty_u16(SPEED)
            pwmDCRF.duty_u16(SPEED)
            print(SPEED)
            print('Set DC Speed \n')
            uart.write('Top DC Speed \n')
        elif "fast" in data:
            pwmDCBF.duty_u16(STOP)
            pwmDCBB.duty_u16(STOP)
            pwmDCLB.duty_u16(STOP)
            pwmDCRB.duty_u16(STOP)
            pwmDCLF.duty_u16(MAX)
            pwmDCRF.duty_u16(MAX)
            print('Mid DC Speed \n')
            uart.write('Mid DC Speed \n')
        elif "reverse" in data:
            pwmDCBF.duty_u16(STOP)
            pwmDCBB.duty_u16(STOP)
            pwmDCLF.duty_u16(STOP)
            pwmDCRF.duty_u16(STOP)
            pwmDCLB.duty_u16(SPEED)
            pwmDCRB.duty_u16(SPEED)
            print('Motors in Reverse \n')
            uart.write('Motors in Reverse \n')
        elif "left" in data:
            pwmDCBF.duty_u16(STOP)
            pwmDCBB.duty_u16(STOP)
            pwmDCLF.duty_u16(STOP)
            pwmDCRB.duty_u16(STOP)
            pwmDCLB.duty_u16(SPEED)
            pwmDCRF.duty_u16(SPEED)
            print('Turning Left \n')
            uart.write('Turning Left \n')
        elif "right" in data:
            pwmDCBF.duty_u16(STOP)
            pwmDCBB.duty_u16(STOP)
            pwmDCLB.duty_u16(STOP)
            pwmDCRF.duty_u16(STOP)
            pwmDCLF.duty_u16(SPEED)
            pwmDCRB.duty_u16(SPEED)
            print('Turning Right \n')
            uart.write('Turning Right \n')
        elif "brake" in data:
            pwmDCLF.duty_u16(STOP)
            pwmDCRF.duty_u16(STOP)
            pwmDCLB.duty_u16(STOP)
            pwmDCRB.duty_u16(STOP)
            print('Motors Stopped \n')
            uart.write('Motors stopped \n')
        elif "magnet" in data:
            pwmDCBB.duty_u16(STOP)
            pwmDCBF.duty_u16(MAX)
            print('Brake is on \n')
            uart.write('Brake is on \n')
        elif "maybe" in data: #Negative Output
            pwmDCBB.duty_u16(STOP)
            pwmDCBF.duty_u16(MAX)
            print('Brake is on \n')
            uart.write('Brake is on \n')
        elif "quit" in data:
            pwmDCBF.duty_u16(STOP)
            pwmDCBB.duty_u16(STOP)
            print('Brake is off \n')
            uart.write('Brake is off \n')
        elif "speed" in data:   
            set_speed=data.split("|")
            print(set_speed[1])
            if "100" in set_speed[1]:
                set_string = set_speed[1]
                sub = set_string[:3]
                print(sub)
            else:
                set_string = set_speed[1]
                sub = set_string[:2]
                print(sub)
            s = int(sub)
            s = float(s)/100 * MAX
            SPEED = int(s)
        elif "stop" in data:
            pwmOUT.duty_u16(STOP)
            pwmIN.duty_u16(STOP)
            pwmDCLF.duty_u16(STOP)
            pwmDCRF.duty_u16(STOP)
            pwmDCLB.duty_u16(STOP)
            pwmDCRB.duty_u16(STOP)
        
