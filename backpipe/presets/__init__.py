from backpipe.presets.file import file_hoster
from backpipe.presets.ipaddr import ipaddr_hoster
from backpipe.presets.redirect import redirect_hoster

class PresetManager():
    def __init__(self) -> None:
        self.presets = {}
    def addPreset(self, name, func):
        self.presets[name] = func
    def execPreset(self, name, addr, port):
        self.presets[name](addr, port)
    def listPresets(self):
        return tuple(self.presets.keys())

PRESET_MNGR = PresetManager()

PRESET_MNGR.addPreset("file", file_hoster)
PRESET_MNGR.addPreset("ipaddr", ipaddr_hoster)
PRESET_MNGR.addPreset("redirect", redirect_hoster)