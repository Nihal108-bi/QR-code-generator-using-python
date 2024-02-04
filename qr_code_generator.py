import qrcode as qr
from PIL import Image

qr=qr.QRCode(version=1,
             error_correction=qr.constants.ERROR_CORRECT_H,
             box_size=10,border=10) 

qr.add_data("https://www.instagram.com/?hl=en")             
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="pink")
img.save("mr_nj_insta.png")
