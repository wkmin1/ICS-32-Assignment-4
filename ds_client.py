# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# William Min
# wkmin1@uci.edu
# 51528316

import socket
import ds_protocol
from time import time

def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
  '''
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''

  try: 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
      client.connect((server, port))

      send = client.makefile("w")
      recv = client.makefile("r")

      print("ICS32 client connected to "+ f"{server} on {port}")

      join_json = ds_protocol.dict_to_json({"join" : {"username" : username, "password" : password, "token" : ""}})
      send_json_to_server(send, join_json)
      response_info = get_response_from_server(recv)

      post_json = ds_protocol.dict_to_json({"token" : response_info.token, "post" : {"entry" : message, "timestamp" : time()}})
      send_json_to_server(send, post_json)

      if bio != None:
        bio_json = ds_protocol.dict_to_json({"token" : response_info.token, "bio" : {"entry" : bio, "timestamp" : time()}})
        send_json_to_server(send, bio_json)
 
    return True
    
  except:
     return False

# sends a json string to the remote server
def send_json_to_server(send, json_msg:str):
  send.write(json_msg + "\r\n")
  send.flush()

# retrieves response from server
def get_response_from_server(recv) -> ds_protocol.ResponseInfo:
  srv_msg = recv.readline()
  return ds_protocol.extract_json(srv_msg)