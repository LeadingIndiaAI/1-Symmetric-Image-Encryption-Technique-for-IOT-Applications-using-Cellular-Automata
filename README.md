# Image-encryption-decryption-app-using-cellular-automata
 
Here we have two different apps using cellular automata for image encryption and decryption. Image is taken from the mobile phone's gallery.
Follow the steps on google to setup your project with firebase

# 1)	IMAGE EN-DECRYPTION APP (This app has been made in ANDROID STUDIO):  
It uses Google Cloud Firebase as storage for images received and being sent to this app. In the server side the image stored in firebase is used for encryption or decryption as per requirement.It does not require any php code, just adding the project to firebase is enough. 

•	The app fetches the image from the folder of the mobile phone.

•	The image is sent to Google Cloud Firebase to be stored there.

•	On server side the image is converted to grayscale format.

•	A predefined rule list contains the rules to be applied to each pixel value.

•	The rules of cellular automata are applied to each pixel value for a certain number of cycles( i.e. till encryption is achieved)

•	This encrypted image is then stored in Firebase.

•	On pressing the decrypt button, the app selects the encrypted image and applies the rules of cellular automata to it so that we can obtain the original image in the server.

•	The decrypted image is then sent to mobile.

# 2)	 KIVY APP :
App using kivy:
•	The app fetches the image from the folder of the mobile phone.

•	The image is converted to grayscale format.

•	A predefined rule list contains the rules to be applied to each pixel value.

•	The rules of cellular automata are applied to each pixel value for a certain number of cycles( i.e. till encryption is achieved)

•	This encrypted image is then stored in the mobile.

•	On pressing the decrypt button, the app selects the encrypted image and applies the rules of cellular automata to it so that we can obtain the original image.

•	The decrypted image is also saved to mobile.






