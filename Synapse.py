import json
from matrix_client.client import MatrixClient


credentials = open("synapse-credentials/credentials.json", mode = "r")
credentials = json.load(credentials)


class Synapse:

    def __init__(self):
        print("Initializing client...")
        client =  MatrixClient(
            "https://matrix.org"
        )
        print("Loggin in...")
        token = client.login(
            credentials["login"],
            credentials["password"]
        )
        print("Reinitializing client")
        self.client =  MatrixClient(
            "https://matrix.org",
            token = token,
            user_id = "@isbur:matrix.org"
        )
        print("Entering the room...")
        self.room = client.join_room("!BeLEKkRmKBJzNOdqxB:matrix.org")
    
    def post(self, msg):
        print("Sending message: ", msg)
        self.room.send_text(str(msg))


Synapse = Synapse()