from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import base64
import requests
import re
import json

# Constant
login_url = 'https://my.its.ac.id'
signin_endpoint = 'https://my.its.ac.id/signin'
username = "5024xxxxxx"
password = "password"

# Start a session to persist cookies
print("Start a session")
session = requests.Session()
response = session.get(login_url)
html_content = response.text

# Use regular expressions to extract dynamic fields
client_id = re.search(r'name="client_id" value="(.*?)"', html_content).group(1)
state = re.search(r'name="state" value="(.*?)"', html_content).group(1)
nonce = re.search(r'name="nonce" value="(.*?)"', html_content).group(1)
redirect_uri = re.search(r'name="redirect_uri" value="(.*?)"', html_content).group(1)
pubkey_pem = re.search(r'id="pubkey" value="(.*?)"', html_content, re.DOTALL).group(1)
pubkey_pem = '\n'.join([s.replace('\t', '') for s in pubkey_pem.splitlines()])

# Prepare the credentials to encrypt
credentials = json.dumps({
    'u': username,  # Replace with your actual username
    'p': password,   # Replace with your actual password
    'dm': '',  # Assuming empty
    'ps': 'true',
})

# Encrypt the credentials using the public key
public_key = serialization.load_pem_public_key(
    pubkey_pem.encode(),
    backend=default_backend()
)
encrypted_content = public_key.encrypt(
    credentials.encode(),
    padding.PKCS1v15()
)
encrypted_base64 = base64.b64encode(encrypted_content).decode()

# Prepare the payload with dynamic fields
payload = {
    'client_id': client_id,
    'response_type': 'code',
    'scope': 'group resource role openid',
    'state': state,
    'prompt': '',
    'redirect_uri': redirect_uri,
    'nonce': nonce,
    'content': encrypted_base64,
    'password_state': 'true',
    'device_method': '',
}

# Submit the login form
login_response = session.post(signin_endpoint, data=payload)

# Check the response to see if login was successful
if "incorrect" in login_response.text:
    print("Incorrect credential!")
else:
    print("Login successful")