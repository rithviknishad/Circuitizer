#!/usr/bin/python3
# Circuitizer Cross Global Definitions


class DynamicCrossGlobalVariable(object):
    def __init__(self):
        self.value = None

    def reset(self):
        self.value = None


# Store the current tab name here
CurrentTab = DynamicCrossGlobalVariable()
# Used to decide if the scrollbar should be visible for not
TabPanelWidth = DynamicCrossGlobalVariable()
