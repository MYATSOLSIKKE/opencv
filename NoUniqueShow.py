from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("QR Code Data From Scanners ")

        # Create a table widget to display the database contents
        self.table = QtWidgets.QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Data","TimeStamp"])
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.setCentralWidget(self.table)

        # Establish a connection to the SQLite database
        conn = sqlite3.connect("data.sqlite")
        cursor = conn.cursor()

        # Fetch all rows from the qr_codes table
        cursor.execute("SELECT * FROM qr_codes")
        rows = cursor.fetchall()

        # Display the data in the table
        self.table.setRowCount(len(rows))

        for idx, row in enumerate(rows):
            id_item = QtWidgets.QTableWidgetItem(str(row[0]))
            data_item = QtWidgets.QTableWidgetItem(row[1])
            timestamp_item = QtWidgets.QTableWidgetItem(row[2])
            self.table.setItem(idx, 0, id_item)
            self.table.setItem(idx, 1, data_item)
            self.table.setItem(idx, 2, timestamp_item)

        # Close the database connection
        conn.close()

        # Close the database connection when the application is closed
        self.destroyed.connect(self.close_db_connection)

    def close_db_connection(self):
        # Establish a connection to the SQLite database
        conn = sqlite3.connect("data.sqlite")
        conn.close()

# Create the application instance and main window
app = QtWidgets.QApplication([])

# Apply a style to the application
app.setStyle("Fusion")

# Set the palette colors for the Fusion style
palette = QtGui.QPalette()
palette.setColor(QtGui.QPalette.Window, QtGui.QColor("#F0F0F0"))
palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor("#333"))
palette.setColor(QtGui.QPalette.Base, QtGui.QColor("white"))
palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor("#F5F5F5"))
palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor("#66A3FF"))
app.setPalette(palette)

# Set the font for the application
font = QtGui.QFont("Arial", 14)  # Replace "Arial" with your desired font
app.setFont(font)

window = MainWindow()
window.show()

# Start the event loop
app.exec_()
