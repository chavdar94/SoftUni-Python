def chat(msg, chat_list):
    chat_list.append(msg)
    return chat_list


def delete(msg, chat_list):
    if msg in chat_list:
        chat_list.remove(msg)
    return chat_list


def edit(msg, edit_msg, chat_list):
    if msg in chat_list:
        old_msg_index = chat_list.index(msg)
        chat_list.remove(msg)
        chat_list.insert(old_msg_index, edit_msg)
    return chat_list


def pin(msg, chat_list):
    if msg in chat_list:
        msg_index = chat_list.index(msg)
        chat_list.append(chat_list.pop(msg_index))


chats = []
while True:
    command = input().split()
    if 'end' in command:
        break
    message = command[1]
    if command[0] == 'Chat':
        chat(message, chats)
    elif command[0] == 'Delete':
        delete(message, chats)
    elif command[0] == 'Edit':
        edit_message = command[2]
        edit(message, edit_message, chats)
    elif command[0] == 'Pin':
        pin(message, chats)
    elif command[0] == 'Spam':
        for text in command[1:]:
            chats.append(text)

print('\n'.join(chats))