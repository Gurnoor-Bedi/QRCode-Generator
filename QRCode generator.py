import qrcode
import matplotlib.pyplot as plt
data=input("Enter your data.")
qr=qrcode.QRCode(
  version=None,
  error_correction=qrcode.constants.ERROR_CORRECT_L,
  box_size=10,
  border=4,


  
)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
plt.imshow(img,cmap="gray")
plt.axis("off")
plt.show()