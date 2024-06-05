import ds_protocol
from Profile import Profile
from time import time

RESPONSE_KEY = 'response'
MESSAGE_LIST_KEY = 'messages'
MESSAGE_KEY = 'message'
RECIPIENT_KEY = 'from'
TIME_STAMP_KEY = 'timestamp'

class DirectMessage:
  def __init__(self):
    self.recipient = None
    self.message = None
    self.timestamp = None

  def __str__(self):
    return "message: " + self.message + "\n\trecipient: " + self.recipient + "\n\ttimestamp: " + self.timestamp

def get_dm_list(response_info:ds_protocol.ResponseInfo) -> list[DirectMessage]:
  message_list = ds_protocol.json_to_dict(response_info)[RESPONSE_KEY][MESSAGE_LIST_KEY]
  dm_list = list()

  for response in message_list:
    dm = DirectMessage()
    dm.message = response[MESSAGE_KEY]
    dm.recipient = response[RECIPIENT_KEY]
    dm.timestamp = response[TIME_STAMP_KEY]
    dm_list.append(dm)

  return dm_list

def get_dm_response_info(profile:Profile, direct_message) -> ds_protocol.ResponseInfo:
  connect_parts = ds_protocol.setup_connection(profile.dsuserver[0], profile.dsuserver[1], profile.username, profile.password)
  send = connect_parts[0]
  recv = connect_parts[1]
  response_info = connect_parts[2]

  return ds_protocol.direct_message(send, recv, response_info, direct_message)

class DirectMessenger:
  def __init__(self, dsuserver=None, username=None, password=None):
    self.token = None
    self.profile = Profile(dsuserver, username, password)
		
  def send(self, message:str, recipient:str) -> bool:
    try: 
      msg_time = time()
      get_dm_response_info(self.profile, {"entry": message, "recipient":recipient, "timestamp": msg_time})

      return True
    
    except:
      return False
		
  def retrieve_new(self) -> list:
    return get_dm_list(get_dm_response_info(self.profile, "new"))
 
  def retrieve_all(self) -> list:
    return get_dm_list(get_dm_response_info(self.profile, "all"))