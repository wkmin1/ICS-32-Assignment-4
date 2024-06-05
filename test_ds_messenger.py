import ds_messenger

if __name__ == "__main__":
    server = ("168.235.86.101", 3021)
    username = "hjahbdgg1"
    password = "DrawinIsGr8"
    username_2 = "wkmin32"
    password_2 = "DrawinIsGr84"

    messenger = ds_messenger.DirectMessenger(server, username, password)
    print(messenger.send("Hello, friend!", username_2))

    messenger_2 = ds_messenger.DirectMessenger(server, username_2, password_2)

    new_dm = messenger_2.retrieve_new()
    for dm in new_dm:
        print(dm)

    all_dm = messenger_2.retrieve_all()
    for dm in all_dm:
        print(dm)