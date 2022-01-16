class TV:
    def __init__(self):
        self.channel = 45
        self.volumeLevel = 5
        self.on = False

    def getChannel(self):
        return self.channel

    def turnon(self):
        print("TV turned on")
        self.on = True

    def turnoff(self):
        print("TV turned off")
        self.on = False

    def setChannel(self, channel):
        if 1 < channel < 120:
            self.channel = channel
        else:
            print("There are only 120 channel. Please, select between 1 to 120 .\n")


    def getVolume(self):
        return self.volumeLevel

    def setVolume(self, volumeLevel):
        if 1 < volumeLevel < 7:
            self.volumeLevel = volumeLevel
        else:
            print("There are only 7 levels. Please select Between 1 to 7. \n")

    def channelUp(self):
        if self.channel != 120:
            self.channel += 1
        else:
            self.channel = 1
            print("There are only 120 channels. Our channel has been set to 1 .\n")

    def channelDown(self):
        if self.channel != 1:
            self.channel -= 1
        else:
            self.channel = 120
            print(" Channel has been changed to 120\n")

    def volumeUp(self):
        if self.volumeLevel != 7:
            self.volumeLevel += 1
        else:
            print("You already have maximum volume\n")

    def volumeDown(self):
        if self.volumeLevel != 1:
            self.volumeLevel -= 1
        else:
            print("You already have min volume\n")


tv = TV()
tv.turnon()
tv.setChannel(120)
print("Current channel: ", tv.getChannel())
tv.setVolume(7)
print("Current volume: ", tv.getVolume())