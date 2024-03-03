# Brushless Motor Controller with Raspberry Pi Pico

The Brushless Motor Controller project aims to create a versatile and user-friendly solution for controlling brushless motors A2212/15T 930KV using the Raspberry Pi Pico microcontroller, Hobbywing Skywalker 30A ESC and inputs. By leveraging the power and flexibility of the Raspberry Pi Pico, combined with simple input mechanisms, this project offers an accessible and customizable motor control solution for various applications.

## Key Features:

* Brushless Motor Control: The heart of the project lies in its ability to control brushless motors, offering precise speed and direction control for a wide range of applications, including robotics, drones, and electric vehicles.
* Raspberry Pi Pico Integration: The Raspberry Pi Pico serves as the central processing unit, providing the necessary computational power and GPIO pins for interfacing with the brushless motor driver signal output and user input.


## Inputs

Here we explored several input method.

### Two Buttons

User Input with two buttons which are incorporated into the design to enable user interaction. These buttons can be used to adjust motor speed. 

Assambling:

* GPIO 13 - Button 1, speed up
* GPIO 14 - Button 2, speed down
* GPIO 15 - PWM, motor control

Power supply: Here I used 12v 12.5A 150W PSU. Lipo 3S is recommended. 

Wire:

![Button Control Wire](https://github.com/GuanyiLi-Craig/pico-brushless-motor/blob/main/static/button_control_wire.png?raw=true)

Assembled: 

![Button Control Assembled](https://github.com/GuanyiLi-Craig/pico-brushless-motor/blob/main/static/button_control_photo.jpg?raw=true)


Left button to increase the speed while right button to decrease the speed. 

### Rotary Angle Sensor

Here we used the [rotary angle sensor](https://thepihut.com/products/grove-rotary-angle-sensor) from grove. And use PIN 28 as the ADC input pin connect to sensor's signal pin. 


Assambling:

* GPIO 15 - PWM, motor control
* GPIO 28 - ADC, adc input

Wire:

![Angle Control Wire](https://github.com/GuanyiLi-Craig/pico-brushless-motor/blob/main/static/angle_control_wire.png?raw=true)

Assembled:

![Angle Control Assembled](https://github.com/GuanyiLi-Craig/pico-brushless-motor/blob/main/static/angle_control_photo.png?raw=true)


## Summary
Overall, the Brushless Motor Controller project combines the power of the Raspberry Pi Pico microcontroller with the simplicity of inputs to create a versatile and customizable motor control solution. Whether used for hobby projects, educational purposes, or prototyping applications, this project offers an exciting opportunity to explore the world of brushless motor control with ease and flexibility.
