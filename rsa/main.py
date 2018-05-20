from rsa import get_private_key, hack, rsa, rsa_string


p = 67
q = 47

message = 19

message_string = 'привет андрей';

e = 5

public_key = (e, p*q)

if __name__ == '__main__':
  private_key = get_private_key(e, p, q)
  print(public_key, private_key)
  encoded_message = rsa(message, public_key)
  decoded_message = rsa(encoded_message, private_key)
  print('good!' if decoded_message is message else 'bad:(' )

  encoded_message = rsa_string(message_string, public_key)
  decoded_message = rsa_string(encoded_message, private_key, False)
  print(encoded_message, decoded_message)
  print('good!' if decoded_message == message_string else 'bad:(' )

  print('hacked key:', hack(public_key), private_key)
