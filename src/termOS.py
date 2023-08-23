from core.system import System
from core.disk import Disk
import time

# Entry point
if __name__ == "__main__":
    system: System = System(name = "termOS")
    system.boot("./data/termOS.state")
    system.loop()