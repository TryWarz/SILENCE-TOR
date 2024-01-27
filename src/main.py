import src.core as core
import src.Interface as interface


class SILENCE_TOR:
    def __init__(self) -> None:
        self.host = core.request
        self.reload = core.tor_reload()
        self.start = core.tor_start()
        pass

    def main(self):
        self.reload

        interface.interface().home()
        
        
