from mcsm.server.server import Server
from queue import Queue

class SimpleCLI:
    def setServer(self, server):
        self.server = server

    def getServerInput(self):
        while True:
            user_in = input()

            # handles all 
            if self.checkMCSM(user_in):
                pass
            else:
                self.server.in_queue.put(user_in)

    def getServerOutput(self):
        while True:
            try:
                out = self.server.out_queue.get_nowait()
                print(out)
            except:
                pass

    def checkMCSM(self, msg):
        return msg.split()[0] == 'mcsm'