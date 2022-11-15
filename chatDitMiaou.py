from animaux import Animal

class Chat(Animal):
    def parler(self):
        print("Miaouu")

chat = Chat()
chat.parler()
