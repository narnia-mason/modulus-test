import subprocess
import sys

def main():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "nvidia-modulus"])