from PySide6.QtCore import QObject, Slot
import meshtastic
import meshtastic.serial_interface

class Backend(QObject):

    def __init__(self):
        super().__init__()
        # connect to your meshtastic device
        self.interface = meshtastic.serial_interface.SerialInterface()

    @Slot()
    def sendTestMessage(self):
        print("Sending test message...")
        self.interface.sendText("Hello from Qt!")
        print("Message sent!")
