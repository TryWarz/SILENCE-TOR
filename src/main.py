import src.core as core
import src.Interface as interface
import os

class SILENCE_TOR:
    def __init__(self) -> None:
        self.host = core.request().host
        self.reload = core.tor_reload()
        self.start = core.tor_start()
        pass

    def main(self):
        os.system("clear")
        self.reload

        interface.interface().home()
        
        print("[!] SILENCE TOR is running...")
        print("[!] Press CTRL+C to stop.")
        self.start
        print("[+] New IP: " + str(self.host))
        try:
            while True:
                pass
        except KeyboardInterrupt:
            print(" [!] Stopping SILENCE TOR...")
            self.start
            print(" [!] SILENCE TOR stopped.")
            exit(0)
        
