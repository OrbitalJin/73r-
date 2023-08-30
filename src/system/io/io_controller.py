# To prevent running into circular imports when annotating, we use the __future__ module
from __future__ import annotations
import system.system as sys

from system.io.display import Display
from system.io.collector import Collector

class IOController:
    def __init__(self, sys: sys.System):
        self._display = Display(sys)
        self._collector = Collector(sys)


    @property
    def display(self) -> Display: return self._display
    @property
    def collector(self) -> Collector: return self._collector


