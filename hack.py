import time
import random
import sys

def type_out(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar(task, duration=2):
    print(f"{task} [", end="")
    for _ in range(20):
        print("#", end="")
        sys.stdout.flush()
        time.sleep(duration / 20)
    print("] Done.")

def ip_scan():
    type_out("Initializing network scan on 192.168.0.0/24...")
    time.sleep(1)
    for i in range(5):
        ip = f"192.168.0.{random.randint(1, 254)}"
        type_out(f"Host found: {ip} | Status: ACTIVE | Open ports: 22, 80, 443")
        time.sleep(0.3)

def password_crack():
    passwords = ["123456", "password", "letmein", "admin", "hunter2"]
    type_out("Cracking password for target 'admin'...")
    for pwd in passwords:
        type_out(f"Trying password: {pwd}")
        time.sleep(0.5)
    type_out("Match found: 'admin123!'")

def override_firewall():
    type_out("Bypassing firewall...")
    for i in range(0, 101, 10):
        sys.stdout.write(f"\rProgress: {i}%")
        sys.stdout.flush()
        time.sleep(0.3)
    print("\nFirewall override complete.")

def deploy_payload():
    type_out("Deploying payload: /tmp/harmless_payload.exe")
    loading_bar("Uploading", 2)
    server.upload("RVCTF{RDev_H4s_b33n_compR0m153D}")
    loading_bar("Executing", 1)
    type_out("Payload executed. Target system compromised.\n")

def grant_access():
    type_out("Access Level: ROOT")
    type_out("Permissions escalated.")
    type_out("Welcome, Agent 47.")

def main():
    type_out("=== INITIATING CONNECTION TO TARGET SERVER ===", 0.03)
    time.sleep(1)
    fake_ip_scan()
    fake_password_crack()
    override_firewall()
    deploy_payload()
    grant_access()
    type_out("\n>>> Operation complete. Logging out...\n", 0.03)

if __name__ == "__main__":
    main()
