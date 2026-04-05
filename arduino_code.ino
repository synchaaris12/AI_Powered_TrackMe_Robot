#include <AFMotor.h>
#include <SoftwareSerial.h>

// Setup Bluetooth on Analog Pins A0 and A1
// HC-05 TX -> A0, HC-05 RX -> A1
SoftwareSerial bluetooth(A0, A1); 

// Define all 4 DC Motors
AF_DCMotor m1(1); 
AF_DCMotor m2(2);
AF_DCMotor m3(3); 
AF_DCMotor m4(4);

void setup() {
  // Start Bluetooth communication at 9600 baud
  bluetooth.begin(9600); 
  
  // Set maximum speed for all motors (0-255)
  // High speed is better for 4-wheel torque
  m1.setSpeed(255); 
  m2.setSpeed(255);
  m3.setSpeed(255); 
  m4.setSpeed(255);
}

void loop() {
  // Check if data is coming from the Laptop via Bluetooth
  if (bluetooth.available() > 0) {
    char cmd = bluetooth.read(); // Read the command (F, B, L, R, or S)
    
    if (cmd == 'F') { // MOVE FORWARD
      m1.run(FORWARD);  m2.run(FORWARD);
      m3.run(FORWARD);  m4.run(FORWARD);
    } 
    else if (cmd == 'B') { // MOVE BACKWARD (When you get too close)
      m1.run(BACKWARD); m2.run(BACKWARD);
      m3.run(BACKWARD); m4.run(BACKWARD);
    }
    else if (cmd == 'L') { // SPIN LEFT
      m1.run(BACKWARD); m3.run(BACKWARD); // Left side back
      m2.run(FORWARD);  m4.run(FORWARD);  // Right side forward
    }
    else if (cmd == 'R') { // SPIN RIGHT
      m1.run(FORWARD);  m3.run(FORWARD);  // Left side forward
      m2.run(BACKWARD); m4.run(BACKWARD); // Right side back
    }
    else if (cmd == 'S') { // STOP
      m1.run(RELEASE);  m2.run(RELEASE);
      m3.run(RELEASE);  m4.run(RELEASE);
    }
  }
}
