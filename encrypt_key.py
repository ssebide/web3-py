import getpass
from eth_account import Account
from pathlib import Path
import json

KEYSTORE_PATH = Path(".keystore.json")

def main():
    private_key = getpass.getpass("Enter your private key: ") #similar to input command
    my_account = Account.from_key(private_key)
    
    password = getpass.getpass("Enter your password:\n")
    encrypted_account = my_account.encrypt(password)
    print(f"Savin to {KEYSTORE_PATH}...")
    with KEYSTORE_PATH.open("w") as fp:
        json.dump(encrypted_account, fp)

if __name__ == "__main__":
    main()
    