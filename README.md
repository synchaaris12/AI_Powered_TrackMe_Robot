# AI-Powered TrackMe Robot 🤖

An autonomous 4WD robot that uses computer vision to track objects in real-time. This project combines Python-based AI with Arduino hardware control.

## 🚀 Features
* **Real-time Tracking:** Uses OpenCV for high-speed face or object detection.
* **Wireless Control:** Communicates via HC-05 Bluetooth module.
* **4-Wheel Drive:** High torque movement using the L293D Motor Shield.
* **Cross-Platform:** Python logic runs on a PC/Laptop, controlling the Arduino hardware remotely.

## 🛠️ Hardware Requirements
* Arduino Uno
* L293D Motor Shield
* HC-05 Bluetooth Module
* 4x DC Motors & Chassis
* 7.4V - 12V Li-ion Battery pack
* USB Camera (or ESP32-CAM)

## 💻 Software Stack
* **Python 3.x:** (OpenCV, PySerial)
* **Arduino IDE:** (AFMotor library)

## 📂 Project Structure
* `/Arduino`: Contains `.ino` sketches for motor control and Bluetooth handling.
* `/Python`: Contains `.py` scripts for OpenCV detection and serial command transmission.

## 🔧 Installation & Usage
1.  Upload the code in the `/Arduino` folder to your Uno.
2.  Pair your PC with the **HC-05 Bluetooth** module.
3.  Install dependencies: `pip install opencv-python pyserial`.
4.  Update the COM port in the Python script to match your Bluetooth port.
5.  Run the Python script: `python track_me.py`.
