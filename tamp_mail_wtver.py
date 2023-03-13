import requests

# API endpoint for creating temporary email
url = 'https://privatix-temp-mail-v1.p.rapidapi.com/request/mail/id'

# Headers required for accessing the API
headers = {
    'X-RapidAPI-Host': 'privatix-temp-mail-v1.p.rapidapi.com',
    'X-RapidAPI-Key': 'YOUR_API_KEY',
}

# Send GET request to create temporary email
response = requests.get(url, headers=headers)

# Extract email from the response
email = response.json()['email']

# API endpoint for fetching verification code
url = f'https://privatix-temp-mail-v1.p.rapidapi.com/request/mail/message/{email}/'

# Send GET request to fetch verification code
response = requests.get(url, headers=headers)

# Extract verification code from the response
verification_code = response.json()[0]['mail_text']

print(f'Temporary email: {email}')
print(f'Verification code: {verification_code}')
