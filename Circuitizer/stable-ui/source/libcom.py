import threading


class DynamicCrossGlobalVariable(object):
    def __init__(self):
        self.value = None
        threading.Timer(1, self.go_back, ()).start()

    def go_back(self):
        self.value = None


CurrentTab = DynamicCrossGlobalVariable()
CurrentTab.value = str()
