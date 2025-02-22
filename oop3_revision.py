class Server:
    def __init__(self, members, meeting): ##constructor
        self.mem = members
        self.meet = meeting #instance variable

    def view(self):
        print("Our meeting is on", self.meet)

        



server_tahiya = Server(10, "wednesday")
server_arman = Server(15, "friday")
server_hasan = Server(9, "sunday")

# print(server_arman.meet)

# server_arman.meet = "sat"

# print(server_arman.meet)
# print(server_tahiya)
# print(server_arman)

server_tahiya.view()
