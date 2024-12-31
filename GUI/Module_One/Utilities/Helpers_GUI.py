from PySide6.QtWidgets import QMessageBox

def show_message_box(title: str, message: str, icon: QMessageBox.Icon = QMessageBox.Information):
        """
        Displays a message box with the given title, message, and icon.

        Args:
            title (str): The title of the message box.
            message (str): The content of the message box.
            icon (QMessageBox.Icon): The icon to display (default is QMessageBox.Information).
        """
        messageBox = QMessageBox()
        messageBox.setWindowTitle(title)
        messageBox.setText(message)
        messageBox.setIcon(icon)
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()