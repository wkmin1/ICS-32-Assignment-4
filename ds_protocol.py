# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# William Min
# wkmin1@uci.edu
# 51528316

import json
from collections import namedtuple
import socket

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
    json_obj = json_to_dict(json_msg)
    response_dict = json_obj[RESPONSE_KEY]
    message_type = response_dict[MESSAGE_KEY]
    token = response_dict[TOKEN_KEY]
  except json.JSONDecodeError:
    print("Json cannot be decoded.")

  return ResponseInfo(message_type, token)

def direct_message(send, recv, response_info, direct_message) -> ResponseInfo:
  json_msg = dict_to_json({"token" : response_info.token, "directmessage" : direct_message})
  send_json_to_server(send, json_msg)
  return recv.readline()

# turns a dictionary value into a json string
def dict_to_json(command_dict) -> str:
  return str(command_dict).replace("\'", "\"")

# turns a json string into a dictionary value
def json_to_dict(json_msg:str) -> dict:
  return json.loads(json_msg)

# sends a json string to the remote server
def send_json_to_server(send, json_msg:str):
  send.write(json_msg + "\r\n")
  send.flush()

# retrieves response from server
def get_response_from_server(recv) -> ResponseInfo:
  srv_msg = recv.readline()
  return extract_json(srv_msg)

def setup_connection(server:str, port:int, username:str, password:str):
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((server, port))

  send = client.makefile("w")
  recv = client.makefile("r")

  print("ICS32 client connected to "+ f"{server} on {port}")

  join_json = dict_to_json({"join" : {"username" : username, "password" : password, "token" : ""}})
  send_json_to_server(send, join_json)
  response_info = get_response_from_server(recv)

  return (send, recv, response_info)
  
