class Protocol(object):
    def __init__(self, name, number, description):

        self.name = name
        self.number = number
        self.description = description

    def getProtocolInfo(self):

        return self.name + " " + str(self.number) + " " + self.description
