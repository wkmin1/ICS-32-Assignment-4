import ds_protocol
from time import time

if __name__ == "__main__":
    server = "168.235.86.101" 
    port = 3021

    username = "hjahbdgg1"
    password = "DrawinIsGr8"
    username_2 = "wkmin32"
    password_2 = "DrawinIsGr84"

    connect_parts = ds_protocol.setup_connection(server, port, username, password)
    send = connect_parts[0]
    recv = connect_parts[1]
    response_info = connect_parts[2]

    assert ds_protocol.direct_message(send, recv, response_info, {"entry": "Hello World!", "recipient":username_2, "timestamp": time()}).type == "ok", F"This message should send, but it shows {ds_protocol.direct_message(send, recv, response_info, {"entry": "Hello World!", "recipient":username_2, "timestamp": time()}).type}"
    assert ds_protocol.direct_message(send, recv, response_info, {"text": "Hello World!", "recipient":username_2, "timestamp": time()}).type == "error", "This message should not send"

    connect_parts_2 = ds_protocol.setup_connection(server, port, username_2, password_2)
    send_2 = connect_parts_2[0]
    recv_2 = connect_parts_2[1]
    response_info_2 = connect_parts_2[2]

    assert ds_protocol.direct_message(send_2, recv_2, response_info_2, {"entry": "Hello To You too!", "recipient":username, "timestamp": time()}).type == "ok", "This message should send"
    assert ds_protocol.direct_message(send_2, recv_2, response_info_2, {"text": "Hello To You too!", "recipient":username, "timestamp": time()}).type == "error", "This message should not send"

    #print(ds_protocol.direct_message(send, recv, response_info, {"entry": "Hello World!", "recipient":username_2, "timestamp": time()}))
    #print(ds_protocol.direct_message(send, recv, response_info, {"entry": "Mr Beast", "recipient":username_2, "timestamp": time()}))
    #print(ds_protocol.direct_message(send, recv, response_info, {"entry": "We must take off from the internet!", "recipient":username_2, "timestamp": time()}))
    assert ds_protocol.direct_message(send, recv, response_info, "new").type == "ok", "The new messages should come out"
    assert ds_protocol.direct_message(send, recv, response_info, "all").type == "ok", "All messages should come out"
    assert ds_protocol.direct_message(send, recv, response_info, "nw").type == "error", "The new messages should not come out"
    assert ds_protocol.direct_message(send, recv, response_info, "al=l").type == "error", "All messages should not come out"

    assert ds_protocol.direct_message(send_2, recv_2, response_info_2, "new").type == "ok", "The new messages should come out"
    assert ds_protocol.direct_message(send_2, recv_2, response_info_2, "all").type == "ok", "All messages should come out"
    assert ds_protocol.direct_message(send_2, recv_2, response_info_2, "nw").type == "error", "The new messages should not come out"
    assert ds_protocol.direct_message(send_2, recv_2, response_info_2, "al=l").type == "error", "All messages should not come out"