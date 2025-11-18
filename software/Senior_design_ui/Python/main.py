import sys

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from backend import Backend
#import PyQt6.QtCore
from autogen.settings import setup_qt_environment

# Import here the Python files that define QML elements


def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    backend = Backend()
    engine.rootContext().setContextProperty("backend", backend)

    setup_qt_environment(engine)

    engine.load("main.qml")
    if not engine.rootObjects():
        sys.exit(-1)

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
