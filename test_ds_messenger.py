import ds_messenger

if __name__ == "__main__":
    server = "168.235.86.101"
    username = "hjahbdgg1"
    password = "DrawinIsGr8"
    username_2 = "wkmin32"
    password_2 = "DrawinIsGr84"
    username_3 = "will316min"
    password_3 = "witherwarrior819"
    username_4 = "wihazbakjbajh"
    password_4 = "whaakfab"

    messenger = ds_messenger.DirectMessenger(server, username, password)
    assert messenger.send(f"Hello, {username_2}!", username_2), "This message should have been sent."

    messenger_2 = ds_messenger.DirectMessenger(server, username_2, password_2)
    assert messenger_2.send(f"Hello, {username}!", username), "This message should have been sent."

    messenger_3 = ds_messenger.DirectMessenger(server, username_3, password_3)
    assert messenger.send(f"Hello, {username_3}!", username_3), "This message should have been sent."
    assert messenger_2.send(f"Hello, {username_3}!", username_3), "This message should have been sent."

    assert len(messenger.retrieve_new()) > 0, "There should be new messages on messenger 1."
    assert messenger.retrieve_new() is None, "There should be no new messages on messenger 1."
    assert len(messenger.retrieve_all()) > 0, "This should give all messages on messenger 1."

    assert len(messenger_2.retrieve_new()) > 0, "There should be new messages on messenger 2."
    assert messenger_2.retrieve_new() is None, "There should be no new messages on messenger 2."
    assert len(messenger_2.retrieve_all()) > 0, "This should give all messages on messenger 2."

    assert len(messenger_3.retrieve_new()) > 0, "There should be new messages on messenger 3."
    assert messenger_3.retrieve_new() is None, "There should be no new messages on messenger 3."
    assert len(messenger_3.retrieve_all()) > 0, "This should give all messages on messenger 3."