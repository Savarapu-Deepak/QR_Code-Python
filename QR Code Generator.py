# QR Code Generator using Python Program.
# Two Modules are required to generate a QR code in Python.
# a) qrcode and b) Image
import qrcode
import image

qr = qrcode.QRCode(version = 15  # Higher the Number, higher the complicated image.
                   , box_size = 10,
                   border = 5)
data = '{Name : Savarapu Deepak, Age = 25, Role : Python Developer}'
qr.add_data(data)
qr.make(fit=True) # Make function ensures that entire dimension of the qr code is utilized.
img = qr.make_image(fill = 'black', back_color = 'White')
img.save('QrCode.png')