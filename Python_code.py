import asyncio
import cv2
from bleak import BleakClient

# ============================================================
# CONFIGURATION - CONFIRMED BY YOUR SCAN
# ============================================================
DEVICE_ADDRESS = "01:34:34:B8:80:4D" 
CHARACTERISTIC_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

# Load the face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

async def run_robot():
    print(f"Connecting to Robot at {DEVICE_ADDRESS}...")
    
    try:
        async with BleakClient(DEVICE_ADDRESS) as client:
            print("Connected successfully! Starting Camera...")
            
            cap = cv2.VideoCapture(0)
            
            # To avoid flooding the Bluetooth with too many commands
            last_command = ""

            while True:
                ret, frame = cap.read()
                if not ret: break

                # Flip frame for natural mirror view
                frame = cv2.flip(frame, 1)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.1, 6)

                current_command = 'S' # Default to Stop

                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    
                    center_x = x + (w // 2)
                    screen_width = frame.shape[1]
                    
                    # Logic: 
                    # If center of face is in the left 35% of screen -> Turn Left
                    # If center of face is in the right 35% of screen -> Turn Right
                    # Otherwise -> Move Forward
                    if center_x < screen_width * 0.35:
                        current_command = 'L'
                    elif center_x > screen_width * 0.65:
                        current_command = 'R'
                    else:
                        current_command = 'F'
                    break 

                # Only send if the command has changed (to keep connection stable)
                if current_command != last_command:
                    await client.write_gatt_char(CHARACTERISTIC_UUID, current_command.encode())
                    last_command = current_command
                    print(f"Robot Action: {current_command}")

                # Display the vision
                cv2.putText(frame, f"Cmd: {current_command}", (10, 30), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("AI Robot Vision", frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    await client.write_gatt_char(CHARACTERISTIC_UUID, 'S'.encode())
                    break

            cap.release()
            cv2.destroyAllWindows()
            
    except Exception as e:
        print(f"Connection Error: {e}")

# Start the AI
if __name__ == "__main__":
    asyncio.run(run_robot())
