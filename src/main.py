import src.core as core
import src.Interface as interface
import os

class SILENCE_TOR:
    """
    SILENCE_TOR class represents the main functionality of the SILENCE TOR application.
    It provides methods to initialize the application, start and stop the TOR service, and display the current IP address.

    Attributes:
        host (str): The current IP address.
        reload (function): Function to reload the TOR service.
        start (function): Function to start the TOR service.

    Methods:
        main(): The main method of the application that runs the TOR service and handles user input.
    """

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
        
