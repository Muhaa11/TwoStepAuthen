# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACd401a13223aaf530d23193ba8899a221'
auth_token = 'c6793c0ad4893f532276baa77af98f64'
client = Client(account_sid, auth_token)

def send_msg(user_code, phone_number):
    message = client.messages.create(
        body=f'Hi there, Your verification code is {user_code}',
        from_='+12548480216',
        to=f'{phone_number}'
                          )

    print(message.sid)