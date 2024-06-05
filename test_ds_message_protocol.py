import ds_protocol
from time import time

if __name__ == "__main__":
    server = "168.235.86.101" 
    port = 3021

    username = "hjahbdgg1"
    password = "DrawinIsGr8"
    username_2 = "wkmin32"
    password_2 = "DrawinIsGr84"

    connect_parts = ds_protocol.setup_connection(server, port, username_2, password_2)
    send = connect_parts[0]
    recv = connect_parts[1]
    response_info = connect_parts[2]

    #print(ds_protocol.direct_message(send, recv, response_info, {"entry": "Hello World!", "recipient":username_2, "timestamp": time()}))
    #print(ds_protocol.direct_message(send, recv, response_info, {"entry": "Mr Beast", "recipient":username_2, "timestamp": time()}))
    #print(ds_protocol.direct_message(send, recv, response_info, {"entry": "We must take off from the internet!", "recipient":username_2, "timestamp": time()}))
    print(ds_protocol.direct_message(send, recv, response_info, "new"))
    print(ds_protocol.direct_message(send, recv, response_info, "all"))