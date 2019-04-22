API = {}
with open('api_key.secret') as f:
    secrets = f.read().splitlines()

for secret in secrets:
    key, value = secret.split(':')
    API[key] = value.strip()
