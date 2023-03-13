import requests

def generate_temp_email():
    domain = '1secmail.com'
    url = f'https://www.{domain}/api/v1/?action=genRandomMailbox&count=1'
    response = requests.get(url).json()
    return response[0]

if __name__ == '__main__':
    temp_email = generate_temp_email()
    print(f'Temporary email address: {temp_email}')
