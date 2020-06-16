
#import cv2
import kivy
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.image import Image

from kivy.uix.popup import Popup
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#import imageio



'''class ImageRead(Image):
    def imageread():
        image = Image(source="Lenna_(test_image).png")
        return image'''
class methods():
    def __init__(self):
        self.List1 = []
        self.decimal = 0

    def convertToBinary(self, n):
        # List1=[]
        while n != 0:
            r = n % 2
            n = n // 2
            self.List1.append(r)
        answer = self.List1[::-1]
        l = len(answer)
        if l < 8:
            z = 8 - l
            for i in range(0, z):
                answer.insert(0, 0)
        return answer

    def convertToDecimal(self, res):
        self.decimal = 0
        rev = res[::-1]
        for i in range(0, len(res)):
            if rev[i] == 1:
                self.decimal += 2 ** i
            else:
                self.decimal += 0
        return self.decimal




def rgb_to_gray(image):
    ans = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    ans1 = ans * 255
    # print(ans1)
    for i in range(0, 512):
        for j in range(0, 512):
            ans1[i][j] = round(ans1[i][j])
    # print(ans1)
    return ans1


class myGrid(GridLayout):
    def __init__(self):
        #self.image = cv2.imread("Lenna_(test_image).png")
        #self.img = self.image.convert('L')
        #self.img = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)

        self.image = mpimg.imread("Lenna_(test_image).png")
        self.img = rgb_to_gray(self.image)
        #plt.imshow(gray, cmap=plt.get_cmap('gray'))
        #plt.savefig('Lenna_gray_scale.png')
        #plt.show()
        print(self.img)



        super(myGrid, self).__init__()
        self.lb1 = Label(text = "ENCRYPTION DECRYPTION APP", color=(1,1,1,1),font_size="20sp")

        self.btn1 = Button(text="INSTRUCTIONS", color=(1, 1, 1, 1), font_size="15sp")
        self.btn1.bind(on_press=self.instructionsClicked)
        
        self.btn2 = Button(text="ENCRYPT", color=(1, 1, 1, 1), font_size="15sp")
        self.btn2.bind(on_press=self.encryptClicked)


        self.btn3 = Button(text="DECRYPT", color=(1, 1, 1, 1), font_size="15sp")
        self.btn3.bind(on_press=self.decryptClicked)

        self.btn4 = Button(text="SEND")
        self.btn4.bind(on_press=self.sendClicked)

        self.btn5 = Button(text="RECEIVE")
        self.btn5.bind(on_press=self.receivedClicked)

        self.btn6 = Button(text="ABOUT US")
        self.btn6.bind(on_press=self.dispInfo)

        self.rows = 7

        self.add_widget(self.lb1)
        self.add_widget(self.btn1)
        self.add_widget(self.btn2)
        self.add_widget(self.btn3)
        self.add_widget(self.btn4)
        self.add_widget(self.btn5)
        self.add_widget(self.btn6)

    def sendClicked(self,instance):
        #image = Image(source="Lenna_(test_image).png")
        sendImage = Popup(title="Notification", content=Label(text="Image sent"), size_hint=(None, None), size=(600, 400))
        sendImage.open()

    def receivedClicked(self,instance):
        receivedImage = Popup(title="Notification", content=Label(text="Image Received"), size_hint=(None, None), size=(600, 400))
        receivedImage.open()

    def instructionsClicked(self,instance):
        showInstructions = Popup(title="Instructions", content=Label(text="Functionality of Buttons:\n\n1.ENCRYPT button :\nencrypts image,security to sensitive data.\n\n2. DECRYPT button :\ndecrypts image, so that sensitive data is seen\n\n3.SEND button :\nsends the encrypted image to receiver via server.\n\n4.RECEIVE button :\n download the sent image from our server.\n\n5. ABOUT US :\nTeam information and communication."), size_hint=(None,None),size=(1000,1000))
        showInstructions.open()

    def dispInfo(self,instance):
        information = Popup(title="About Us", content=Label(text="Our Team:\n --> Swati Yadav             Contact: 123456789\n --> Tejas Dhopavkar     Contact: 123456789\n --> Prajkta Kodavade    Contact: 123456789\n --> Vidit Jain                  Contact: 123456789\n --> Girija Cheruku          Contact: 123456789\n\n\n For queries and feed back\n\n Email : abc@gmail.com"), size_hint=(None, None), size=(1000, 900))
        information.open()


    

    def encryptClicked(self,instance):
        print("Encrypt Activated")
        #ruleList = [105, 153, 153, 153, 150, 150, 51, 51]
        #ruleList = [153, 153, 153, 153, 216, 51, 83, 60]
        #ruleList = [153,153,153,153,51,51,105,51]
        #ruleList = [150,102,102,102,85,165,51,51]
        #ruleList = [102,153,102,102,150,105,51,51]
        ruleList = [102,102,102,102,51,86,240,153]
        cycle = 0
        img1 = self.img
        test = np.empty([512, 512], dtype=int)
        while cycle < 4:
            for m in range(0, 512):
                for n in range(0, 512):
                    dec = self.img[m][n]
                    obj1 = methods()
                    List = obj1.convertToBinary(dec)
                    # print(List)
                    res = []
                    for i in range(0, 8):
                        rule = ruleList[i]

                        if i == 0:
                            a = 0
                            b = List[i]
                            c = List[i + 1]
                        elif i == 7:
                            a = List[i - 1]
                            b = List[i]
                            c = 0
                        else:
                            a = List[i - 1]
                            b = List[i]
                            c = List[i + 1]

                        if rule == 51:
                            exp = (not b)
                            
                        elif rule == 85:
                        	exp = (not c)

                        elif rule == 86:
                            exp = ((a and (not c)) or (b and (not c)) or (c and (not a) and (not b)))
                        
                        elif rule == 102:
                        	exp = (b and (not c) or (c and (not b)))

                        elif rule == 105:
                            exp = ((a and b and (not c)) or (a and c and (not b)) or (b and c and (not a)) or (
                                    (not a) and (not b) and (not c)))

                        elif rule == 150:
                            exp = ((a and b and c) or (a and (not b) and (not c)) or (b and (not a) and (not c)) or (
                                    c and (not a) and (not b)))

                        elif rule == 153:
                            exp = ((b and c) or ((not b) and (not c)))
                            
                        elif rule == 165:
                        	exp = ((a and c) or ((not a) or (not c)))

                        elif rule == 240:
                            exp = (a)

                        res.append(int(exp))

                    List = res[:]
                    obj2 = methods()
                    ans = obj2.convertToDecimal(res)
                    test[m][n] = ans

            cycle += 1
            print("CYCLE:", cycle)
            '''if cycle == 4:
                # cv2.imshow(test)
                matplotlib.image.imsave("/storage/emulated/0/kivy/main/test_5.jpg", test,cmap='gray')
                showEncryptedImage()'''
                
            print("\n")
            self.img = test

        for i in range(0,512):
            for j in range(0,512):
                self.img[i][j]=(self.img[i][j]*187)%256

        matplotlib.image.imsave("/storage/emulated/0/kivy/main/test_5.jpg", self.img,cmap='gray')
        showEncryptedImage()

    def decryptClicked(self,instance):
        print("Decrypt Activated")
        #ruleList = [105, 153, 153, 153, 150, 150, 51, 51]
        # ruleList = [153, 153, 153, 153, 216, 51, 83, 60]
        #ruleList = [153, 153, 153, 153, 51, 51, 105, 51]
        #ruleList = [150,102,102,102,85,165,51,51]
        #ruleList = [102,153,102,102,150,105,51,51]
        ruleList = [102,102,102,102,51,86,240,153]
        
        for i in range(0,512):
            for j in range(0,512):  
                self.img[i][j]=(self.img[i][j]*115)%256
                
        cycle = 4
        img1 = self.img
        test = np.empty([512, 512], dtype=int)
        while cycle < 8:
            for m in range(0, 512):
                for n in range(0, 512):
                    dec = self.img[m][n]
                    obj1 = methods()
                    List = obj1.convertToBinary(dec)
                    # print(List)
                    res = []
                    for i in range(0, 8):
                        rule = ruleList[i]

                        if i == 0:
                            a = 0
                            b = List[i]
                            c = List[i + 1]
                        elif i == 7:
                            a = List[i - 1]
                            b = List[i]
                            c = 0
                        else:
                            a = List[i - 1]
                            b = List[i]
                            c = List[i + 1]

                        if rule == 51:
                            exp = (not b)
                            
                        elif rule == 85:
                        	exp = (not c)
                        	
                        elif rule == 86:
                        	exp = ((a and (not c)) or (b and (not c)) or (c and (not a) and (not b)))
                        
                        elif rule == 102:
                        	exp = (b and (not c) or (c and (not b)))
                        

                        elif rule == 105:
                            exp = ((a and b and (not c)) or (a and c and (not b)) or (b and c and (not a)) or (
                                    (not a) and (not b) and (not c)))

                        elif rule == 150:
                            exp = ((a and b and c) or (a and (not b) and (not c)) or (b and (not a) and (not c)) or (
                                    c and (not a) and (not b)))

                        elif rule == 153:
                            exp = ((b and c) or ((not b) and (not c)))
                            
                        elif rule == 165:
                        	exp = ((a and c) or ((not a) or (not c)))
                        
                        elif rule == 240:
                        	exp = (a)

                        res.append(int(exp))

                    List = res[:]
                    obj2 = methods()
                    ans = obj2.convertToDecimal(res)
                    test[m][n] = ans

            cycle += 1
            print("CYCLE:", cycle)
            if cycle == 8:
                
                matplotlib.image.imsave("/storage/emulated/0/kivy/main/test_5_result.png", test,cmap='gray')
                
                showDecryptedImage()
            print("\n")
            self.img = test



'''class P(FloatLayout):
    pass'''



class encryptApp(App):
    def build(self):
        return myGrid()


def showEncryptedImage():
    popupWindow = Popup(title="Encrypted Image", content=Image(source='/storage/emulated/0/kivy/main/test_5.jpg'),
                        size_hint=(None, None), size=(600,600))

    # open popup window
    popupWindow.open()

def showDecryptedImage():
    popupWindow = Popup(title="Decrypted Image", content=Image(source='/storage/emulated/0/kivy/main/test_5_result.png'),
                        size_hint=(None, None), size=(512, 512))

    # open popup window
    popupWindow.open()

encryptApp().run()
