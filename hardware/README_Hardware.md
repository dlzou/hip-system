# **hip-system**
Hot Interior Protection System, a project for Hack Month 2020

## **Hardware Portion**
The hardware portion of the system is mainly divided into 6 different modules: CAN Communication Module, Power Regulation, Environmental Sensor, Image Processing, Wireless Communication and Warning module. The Wireless Communication module is responsible for relaying important information such as temperature, passenger status etc. to the mobile interface.

### *CAN Communication*
The system mainly interacts with the vehicle via the CAN network. The CAN Communication module is responsible for communicating with the CAN network in the car to gather important information regarding to vehicle status and to control certain components onboard the vehicle such as turning off air conditioning or honk horns. In our prototype, this is achieved by using a Arduino CAN shield, in our case, an OBD-II UART Arduino module.
### *Power Regulation*
The Power Regulation module helps provide a stable power supply for all the modules. In our prototype, it steps down the 12V supply provided by the car battery to a 5V supply suitable for the components used in other modules such as the Raspberry Pi and the Arduino used for the Environmental Sensor module and Image Processing module. This is achieved by using a L7805 5V regulator.
### *Environmental Sensor*
The Environmental Sensor module senses environmental data such as the temperature within the vehicle and whether there are object within the vehicle. This includes a pressure sensor pad on the passenger seats and a temperature sensor. For our prototype, we used an analog textile sensor PW073 for detecting whether an object in on a seat by sensing pressure and an analog low voltage temperature sensor TMP36 for gathering interior temperature data. The data is then sent to a microcontroller, in our case an Arduino. The microcontroller then checks if the temperature is above a certain threshold such as 38&deg;C or 100&deg;F and if an object is occupying the passenger seat. If both clause is true, a signal is then sent to the Image Processing module in attempt to recognize the object.
### *Image Processing*
The Image Processing module determines whether the object detected by the Environment Sensors are living beings through advanced computer vision techniques, which would be elaborated upon on the Software Portion of this documentation. In the prototype, this is achieved using a USB webcam connected to a Raspberry Pi that is pointed at the passenger seat to check whether the object is a baby or a pet. If it is, it sends a signal to the Warning module to warn the user about the passenger or pet and the Wireless Communication module to relay this information to the mobile interface.
### *Wireless Communication*
The Wireless Communication module is responsible for relaying important informations such as temperature, passenger status etc. to the mobile interface. In our prototype, the mobile interface is connected to the system via Bluetooth, which is done using a BLE module connected to the Raspberry Pi.
### *Warning Module*
This the module that provides onboard warning to the user if a baby or pet is detected in a passenger seat. When an appropriate signal is received from the image processing module, this module's microcontroller, in our case the Arduino, would notify the CAN Communication module to turn on the air conditioning, roll down the car window, and honk the horns. In addition, the alarm, in our prototype, the ultra bright LED and buzzer will go off, flashing and buzzing in quick successions.

![HIP Schematic](HIP_Schematic_schem.png)
