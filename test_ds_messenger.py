import ds_messenger

if __name__ == "__main__":
    server = "168.235.86.101"
    username = "hjahbdgg1"
    password = "DrawinIsGr8"
    username_2 = "wkmin32"
    password_2 = "DrawinIsGr84"
    username_3 = "will316min"
    password_3 = "witherwarrior819"

    messenger = ds_messenger.DirectMessenger(server, username, password)
    print(messenger.send(f"Hello, {username_2}!", username_2))

    messenger_2 = ds_messenger.DirectMessenger(server, username_2, password_2)
    print(messenger_2.send(f"Hello, {username}!", username))

    messenger_3 = ds_messenger.DirectMessenger(server, username_3, password_3)
    print(messenger.send(f"Hello, {username_3}!", username_3))
    print(messenger_2.send(f"Hello, {username_3}!", username_3))

    messenger.retrieve_new()
    messenger.retrieve_all()

    messenger_2.retrieve_new()
    messenger_2.retrieve_all()

    messenger_3.retrieve_new()
    messenger_3.retrieve_all()

    print(messenger.retrieve_new())
    print(messenger.retrieve_all())

    print(messenger_2.retrieve_new())
    print(messenger_2.retrieve_all())

    print(messenger_3.retrieve_new())
    print(messenger_3.retrieve_all())