from os import environ

def get_value_for_key(key: str):
  """
    This may be used to get secrets from environ or remote key repository
  """
  return environ.get(key)
