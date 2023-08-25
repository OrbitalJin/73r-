from engine.system import System
import readline
import rich


# Entry point
if __name__ == "__main__":
    system: System = System(name = "termOS")
    system.boot("./data/termOS.state")
    system.loop()