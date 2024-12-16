from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

VAULT_URL = "https://<your-key-vault-name>.vault.azure.net"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=VAULT_URL, credential=credential)

# Set a secret
client.set_secret("mySecretName", "mySecretValue")

# Get a secret
retrieved_secret = client.get_secret("mySecretName")
print(f"Secret Name: {retrieved_secret.name}")
print(f"Secret Value: {retrieved_secret.value}")
