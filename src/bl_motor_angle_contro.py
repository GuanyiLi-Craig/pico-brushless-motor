# importing the required libraries
from machine import Pin, ADC
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

pot = ADC(Pin(28))

pwmOutput.freq(int(frequency))
duty_cycle = 4000

while True:
    duty = int(pot.read_u16() / 65535 * 3399) + duty_cycle_min    

    # duty cycle in integer
    # check user input for discrepancy
    if duty_cycle >= duty_cycle_min and duty_cycle <= duty_cycle_max and duty_cycle != duty:
        duty_cycle = duty
        print(duty)
        pwmOutput.duty_u16(duty_cycle)
    else:
        continue
