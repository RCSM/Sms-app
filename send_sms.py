from twilio.rest import Client

from credentials import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)

str = """
txt msg ::: Oi Humano! Eu sou um bot do twilio, pode confiar em mim ;)
"""

message = client.messages.create(to=my_cell, from_=my_twilio, body=str)
