import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

# import UI from the ui folder
from ui.ui_untitled import Ui_MainWindow

import meshtastic.serial_interface


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect to Meshtastic device
        try:
            self.interface = meshtastic.serial_interface.SerialInterface()
        except Exception as e:
            QMessageBox.critical(
                self,
                "Meshtastic Error",
                f"Failed to connect to device:\n{e}"
            )
            sys.exit(1)

        # Connect button with Qt6 signal syntax
        self.ui.pushButton.clicked.connect(self.send_pit_messages)

    def send_pit_messages(self):
        # Get numbers from combo boxes
        team_a = self.ui.TeamA_Number.currentText()
        team_b = self.ui.TeamB_Number.currentText()

        # Build messages
        msg_a = f"#{team_a} | team go to pit"
        msg_b = f"#{team_b} | team go to pit"

        try:
            # Send Team A message
            self.interface.sendText(msg_a)

            # Send Team B message
            self.interface.sendText(msg_b)

            QMessageBox.information(
                self,
                "Messages Sent",
                f"Sent:\n{msg_a}\n{msg_b}"
            )

        except Exception as e:
            QMessageBox.critical(
                self,
                "Send Error",
                f"Failed to send messages:\n{e}"
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())