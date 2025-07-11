import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

#delete in production
# from dotenv import load_dotenv
# load_dotenv()

# key_vault_uri=os.getenv("KEYVAULT_URI", "https://keyvaultpython.vault.azure.net/")

key_vault_uri=os.getenv("KEYVAULT_URI")

#auth

credential = DefaultAzureCredential()

# Create a SecretClient to interact with the Key Vault
client = SecretClient(vault_url=key_vault_uri, credential=credential)

def get_secret(name_secret):
    try:
        return client.get_secret(name=name_secret).value
    except Exception as e:
        print(f"Error get secret {name_secret}: {e}")


