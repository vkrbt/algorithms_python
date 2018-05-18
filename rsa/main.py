from rsa import get_private_key, get_public_key, encode, decode


p = 19
q = 23

message = 15

e = 43

public_key = (e, 19*23)


if __name__ == '__init__':
  private_key = get_private_key(public_key)
  encoded_message = encode(message, public_key)
  decoded_message = decode(encoded_message, private_key)

  print('good!' if decoded_message is message else 'bad:(' )
