

class kumanda():
    def __init__ (self,tv_durum = "kapalı",tv_ses = 0, kanal_listesi = ["Trt"], kanal = "Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    def open_tv(self):
        self.tv_durum = "açık"
    def close_tv(self):
        self.tv_durum = "kapalı"
    
    def tv_volume(self):
        a = int(input("To Volume Up Press 1, To Volume down press 0: "))
        if a == 1:
            if self.tv_ses == 5:
                print("you can't up the volume")
            else:
                self.tv_ses+= 1
        else:
            if self.tv_ses == 0:
                print("you can't down the volume")
            else :
                self.tv_ses -= 1
        print(f"New volume: {self.tv_ses}")
    
    def tv_channel_list(self):
        a = int(input("To append press '1', To delist press '0'"))
        if a == 0:
            if len(self.kanal_listesi) == 0:
                print("you can't delist anymore")
            else:
                b = input("Channel name: ")
                for i in self.kanal_listesi:
                    if b == i:
                        self.kanal_listesi.remove(i)

        if a == 1:
            b = input("Channel name: ")
            self.kanal_listesi.append(b)
        print(f"Channel List: {self.kanal_listesi}")
    
    def choose_channel(self):
        j = 0
        for i in self.kanal_listesi:
            j+=1
            print(f"To {i} press {j}")
        a = int(input("Channel: "))
        print(f"Now the channel is {self.kanal_listesi[a-1]}")
        self.kanal = self.kanal_listesi[a-1]
    
    def bilgieri_goster(self):
        print(self.tv_durum)
        print(self.tv_ses)
        print(self.kanal_listesi)
        print(self.kanal)
kumanda1 = kumanda()
while True:
    a = int(input("To open TV '1' / To close TV '2' / To Change Volume '3' / To add or remove channel '4'\nTo choose channel '5' / To all informations '6' / To Leave '7'"))
    if a == 1:
        kumanda1.open_tv()
    if a == 2:
        kumanda1.close_tv()
    if a == 3:
        kumanda1.tv_volume()
    if a == 4:
        kumanda1.tv_channel_list()
    if a == 5:
        kumanda1.choose_channel()
    if a == 6:
        kumanda1.bilgieri_goster()
    if a == 7:
        print("leaving the program")
        break



                


