from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("QR Code Data")

        # Create a table widget to display the database contents
        self.table = QtWidgets.QTableWidget(self)
        self.table.setColumnCount(2)  # Two columns: Data and Timestamp
        self.table.setHorizontalHeaderLabels(["Data", "Timestamp"])
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.setCentralWidget(self.table)

        # Fetch and display the data and timestamp from the database
        conn = sqlite3.connect("data.sqlite")
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT data, timestamp FROM qr_codes")
        rows = cursor.fetchall()
        self.table.setRowCount(len(rows))

        for idx, row in enumerate(rows):
            data_item = QtWidgets.QTableWidgetItem(row[0])
            self.table.setItem(idx, 0, data_item)

            # Check if the row has a timestamp (index 1 in the tuple)
            if len(row) >= 2:
                timestamp_item = QtWidgets.QTableWidgetItem(row[1])
                self.table.setItem(idx, 1, timestamp_item)
            else:
                # If there is no timestamp in the row, set a default value or handle it as needed
                timestamp_item = QtWidgets.QTableWidgetItem("N/A")
                self.table.setItem(idx, 1, timestamp_item)

        # Close the database connection
        conn.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle("Fusion")  # Apply the Fusion style

    # Set the font for the application
    font = QtGui.QFont("Arial", 14)  # Replace "Arial" with your desired font
    app.setFont(font)

    window = MainWindow()
    window.show()
    app.exec_()
