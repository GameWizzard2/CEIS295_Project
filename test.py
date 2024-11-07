import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

# Step 1: Define the application
app = QApplication(sys.argv)

# Step 2: Set up the main window
main_window = QWidget()
main_window.setWindowTitle("PySide6 Starter")

# Step 3: Create a layout and widgets
layout = QVBoxLayout()
label = QLabel("Welcome to PySide6!")
button = QPushButton("Click Me")

# Step 4: Define what happens when the button is clicked
def on_button_clicked():
    label.setText("Hello, PySide6!")

button.clicked.connect(on_button_clicked)

# Step 5: Add widgets to the layout and set the layout to the main window
layout.addWidget(label)
layout.addWidget(button)
main_window.setLayout(layout)

# Step 6: Display the main window
main_window.show()

# Step 7: Execute the application
sys.exit(app.exec())
