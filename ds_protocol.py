# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# William Min
# wkmin1@uci.edu
# 51528316

import json
from collections import namedtuple

# Namedtuple to hold the values retrieved from json messages.
MESSAGE_KEY = 'type'
TOKEN_KEY = 'token'
RESPONSE_KEY = 'response'
ResponseInfo = namedtuple('ResponseInfo', [MESSAGE_KEY, TOKEN_KEY])

def extract_json(json_msg:str) -> ResponseInfo:
  '''
  Call the json.loads function on a json string and convert it to a DataTuple object
  '''
  try:
    json_obj = json.loads(json_msg)
    response_dict = json_obj[RESPONSE_KEY]
    message_type = response_dict[MESSAGE_KEY]
    token = response_dict[TOKEN_KEY]
  except json.JSONDecodeError:
    print("Json cannot be decoded.")

  return ResponseInfo(message_type, token)
