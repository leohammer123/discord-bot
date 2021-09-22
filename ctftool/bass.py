import base64


def bass64(txt):
  return base64.b64decode(txt).decode()

def bass32(txt):
  return base64.b32decode(txt).decode()