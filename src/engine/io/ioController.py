# To prevent running into circular imports when annotating, we use the __future__ module
from __future__ import annotations
import engine.system as sys

from engine.io.display import Display
from engine.io.collector import Collector

class IOController:
    def __init__(self, sys: sys.System):
        self._display = Display(sys)
        self._collector = Collector(sys)

    @property
    def display(self) -> Display: return self._display
    @property
    def collector(self) -> Collector: return self._collector


