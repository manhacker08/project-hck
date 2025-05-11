from utils import *

import time
import random

def decode_matrix():
    print("Decoding the encrypted flux capacitor matrix...")
    time.sleep(1)
    for _ in range(5):
        print("".join(random.choice("01") for _ in range(32)))
        time.sleep(0.3)
    print("Error: Flux density is over 9000.")
    time.sleep(0.5)
    print("Attempting reverse polarity of the neutron flow...")
    time.sleep(1)
    print("Abort. Reticulating splines instead.")

def reticulate_splines():
    print("Reticulating splines...")
    for i in range(101):
        time.sleep(0.01)
        print(f"Spline reticulation progress: {i}%", end="\r")
    print("Splines reticulated. Absolutely nothing changed.")

def main():
    decode_matrix()
    reticulate_splines()
    print("\nAll tasks complete. You have achieved nothing.")

if __name__ == "__main__":
    main()
