import ds_protocol
from Profile import Profile, Post, DirectMessage
from time import time

RESPONSE_KEY = 'response'
MESSAGE_LIST_KEY = 'messages'
MESSAGE_KEY = 'message'
RECIPIENT_KEY = 'from'
TIME_STAMP_KEY = 'timestamp'

def get_dm_list(response_info:ds_protocol.ResponseInfo) -> list[DirectMessage]:
  dm_list = list()

  if response_info is None:
    return None
  
  else: 
    message_list = response_info.token

    for response in message_list:
      dm = DirectMessage(response[RECIPIENT_KEY], response[MESSAGE_KEY], float(response[TIME_STAMP_KEY]))
      dm_list.append(dm)

    if len(dm_list) <= 0:
      return None
    else:
      return dm_list

def get_dm_response_info(profile:Profile, direct_message) -> ds_protocol.ResponseInfo:
  port = 3021
  try:
    connect_parts = ds_protocol.setup_connection(profile.dsuserver, port, profile.username, profile.password)
    send = connect_parts[0]
    recv = connect_parts[1]
    response_info = connect_parts[2]

    return ds_protocol.direct_message(send, recv, response_info, direct_message)
  except:
    return None
  
def get_dms(dm_collection:list[DirectMessage], contact:str):
  dm_list = list()

  for dm in dm_collection:
    if dm.get_recipient() == contact:
      dm_list.append(dm)

  dm_list.sort(reverse = True, key = sort_by_time)
  return dm_list

def sort_by_time(dm:DirectMessage):
  return dm.get_time()

class DirectMessenger:
  def __init__(self, dsuserver=None, username=None, password=None):
    self.token = None
    self.profile = Profile(dsuserver, username, password)
    self.profile_path = None
    
    if username is not None:
      self.profile_path = username + "_profile.dsu"

      try:
        self.profile.load_profile(self.profile_path)
      except Exception:
        self.retrieve_all()
		
  def send(self, message:str, recipient:str) -> bool:
    try: 
      msg_time = time()
      get_dm_response_info(self.profile, {"entry": message, "recipient":recipient, "timestamp": msg_time})
      self.profile.add_post(DirectMessage(recipient, message, msg_time))

      self.save_messenger()
      return True
    
    except:
      return False
		
  def retrieve_new(self) -> list:
    dm_list = get_dm_list(get_dm_response_info(self.profile, "new"))

    if dm_list is not None:
      for dm in dm_list:
        self.profile.add_other_post(dm)

    self.save_messenger()

    return dm_list
 
  def retrieve_all(self) -> list:
    dm_list = get_dm_list(get_dm_response_info(self.profile, "all"))

    if dm_list is not None:
      self.profile._other_dms = dm_list

    self.save_messenger()
    
    return self.profile._other_dms
  
  def save_messenger(self):
    if self.profile_path is not None:
      self.profile.save_profile(self.profile_path)

  def sent_dms(self, recipient:str):
    return get_dms(self.profile._dms, recipient)

  def received_dms(self, sender:str):
    return get_dms(self.profile._other_dms, sender)
