import os
import subprocess
import time


class Tools:
    @staticmethod
    def clear():
        subprocess.run("cls" if os.name == "nt" else "clear", check=False, shell=True)

    @staticmethod
    def wait(cooldown):
        time.sleep(cooldown)
