import AminoLab
import pyfiglet
import concurrent.futures
from colored import fore, back, style, attr
attr(0)
print(fore.INDIAN_RED_1A + style.BOLD)
print("""Script by Lil Zevi
Github : https://github.com/LilZevi""")
print(pyfiglet.figlet_format("aminomssbov2", font="rectangles"))
client = AminoLab.Client()
email = input("Email >> ")
password = input("Password >> ")
client.auth(email=email, password=password)
message = input("Message >> ")
clients = client.my_communities()
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
ndcId = clients.ndcId[int(input("Select the community >> ")) - 1]

def chats_spam():
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        try:
            chats = client.get_public_chat_threads(ndcId=ndcId, size=100)
            for chatId, title in zip(chats.threadId, chats.title):
                print(f"Joined To Chat {title}")
                _ = [executor.submit(client.join_thread, ndcId, chatId) for _ in range(2)]
                _ = [
                    executor.submit(
                        client.send_message,
                        ndcId,
                        chatId,
                        message) for _ in range(12)]
                print(f"Spammed Chat {title}")
            print("All Chats Spammed")
        except Exception as e:
            print(e)

chats_spam()
