from PyQt5.QtCore import pyqtSignal, QObject, pyqtSlot


class WidgetA(QObject):
    procStart = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def some_function(self):
        # Do something
        self.procStart.emit("Hello from WidgetA")


class WidgetB(QObject):
    def __init__(self):
        super().__init__()

    @pyqtSlot(str)
    def on_proc_start(self, message):
        # Do something with the message
        print(message)


widgetA = WidgetA()
widgetB = WidgetB()

widgetA.procStart.connect(widgetB.on_proc_start)

widgetA.some_function()
