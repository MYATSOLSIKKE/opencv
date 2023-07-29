import cv2
import pyzbar.pyzbar as pyzbar
import sqlite3
import datetime

# Create a flag to control the QR code scanning loop
scanning = False

# Function to handle the QR code scanning
def scan_qr_code():
    global scanning
    scanning = True
    # Create a VideoCapture object to capture video from the camera
    cap = cv2.VideoCapture(0)

    try:
        while scanning:
            # Create a new connection and cursor within the scanning loop
            with sqlite3.connect("data.sqlite") as conn:
                cursor = conn.cursor()

                # Read the current frame from the camera
                ret, frame = cap.read()

                # Find and decode QR codes in the frame
                decoded_objects = pyzbar.decode(frame)

                for obj in decoded_objects:
                    # Get the current date and time
                    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    # Extract the data from the QR code
                    qr_data = obj.data.decode("utf-8")

                    # Display the QR code data
                    print("QR Code Data:", qr_data)

                    # Create the "qr_codes" table if it doesn't exist
                    cursor.execute("CREATE TABLE IF NOT EXISTS qr_codes (id INTEGER PRIMARY KEY, data TEXT, timestamp TEXT)")

                    # Check if the "timestamp" column exists
                    cursor.execute("PRAGMA table_info(qr_codes)")
                    columns = cursor.fetchall()
                    has_timestamp_column = any(col[1] == 'timestamp' for col in columns)

                    # If the "timestamp" column doesn't exist, add it to the table
                    if not has_timestamp_column:
                        cursor.execute("ALTER TABLE qr_codes ADD COLUMN timestamp TEXT")

                    # Store the QR code data and timestamp in the database
                    cursor.execute("INSERT INTO qr_codes (data, timestamp) VALUES (?, ?)", (qr_data, current_datetime))
                    conn.commit()

                # Check for key press events
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    except KeyboardInterrupt:
        # Handle the Keyboard Interrupt gracefully
        print("QR code scanning interrupted")

    finally:
        # Release the VideoCapture
        cap.release()

if __name__ == "__main__":
    scan_qr_code()
