import json, os, base64
from cryptography.fernet import Fernet
from getpass import getpass
import hashlib
import argparse

VAULT_FILE = "vault.json"

def derive_key(master_pwd):
    hash_digest = hashlib.sha256(master_pwd.encode()).digest()
    return base64.urlsafe_b64encode(hash_digest)

def load_vault():
    if not os.path.exists(VAULT_FILE):
        return {}
    with open(VAULT_FILE, 'r') as f:
        return json.load(f)

def save_vault(data):
    with open(VAULT_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_password(service, password, fernet):
    vault = load_vault()
    vault[service] = fernet.encrypt(password.encode()).decode()
    save_vault(vault)
    print(f"🔐 Password added for '{service}'.")

def get_password(service, fernet):
    vault = load_vault()
    if service in vault:
        decrypted = fernet.decrypt(vault[service].encode()).decode()
        print(f"🔓 Password for '{service}': {decrypted}")
    else:
        print("❌ Service not found.")

def delete_password(service):
    vault = load_vault()
    if service in vault:
        del vault[service]
        save_vault(vault)
        print(f"🗑️ Deleted password for '{service}'.")
    else:
        print("❌ Service not found.")

def main():
    parser = argparse.ArgumentParser(description="Password Manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    add = subparsers.add_parser("add")
    add.add_argument("service")
    
    get = subparsers.add_parser("get")
    get.add_argument("service")

    delete = subparsers.add_parser("delete")
    delete.add_argument("service")

    args = parser.parse_args()
    master_pwd = getpass("🔑 Enter master password: ")
    fernet = Fernet(derive_key(master_pwd))

    if args.command == "add":
        pw = getpass("🔐 Enter password to store: ")
        add_password(args.service, pw, fernet)
    elif args.command == "get":
        get_password(args.service, fernet)
    elif args.command == "delete":
        delete_password(args.service)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
