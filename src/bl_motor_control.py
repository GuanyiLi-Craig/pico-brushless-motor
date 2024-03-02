# importing the required libraries
from machine import Pin
from machine import PWM
import time



# initial varibale declaratins
frequency = 50
# min and max is the ~5% and ~10% of the maximum duty cycle value 65025
duty_cycle_min = 3200
duty_cycle_max = 6600



# pin declarations
pwmPin = Pin(15) # declare the pin for PWM output
pwmOutput = PWM(pwmPin) # define a PWM object

button_1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button_2 = Pin(14, Pin.IN, Pin.PULL_DOWN)

pwmOutput.freq(int(frequency))
    
# Set initial duty 
duty = 4000

# define function for PWM generation
def pwmGenerate(duty_cycle):
    duty_cycle = duty_cycle
    pwmOutput.duty_u16(duty_cycle)
 
duty_cycle = duty_cycle_min
# generate the PWM signal with variable duty cycle 
while True:
    if button_1.value():
        duty = duty + 50
        time.sleep(0.5)


    if button_2.value():
        duty = duty - 50
        time.sleep(0.5)
        

    # duty cycle in integer
    # check user input for discrepancy
    if duty_cycle >= duty_cycle_min and duty_cycle <= duty_cycle_max and duty_cycle != duty:
        duty_cycle = duty
        print(duty)
        pwmGenerate(duty_cycle)
    elif duty < duty_cycle_min:
        duty = duty_cycle_min
    elif duty > duty_cycle_max:
        duty = duty_cycle_max
    else:
        continue
