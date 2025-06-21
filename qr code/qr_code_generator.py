import qrcode


data = 'https://www.instagram.com/_.craziee_boy._/'

qr_image = qrcode.make(data)
qr_image.save(r"D:\python\qr code\insta_qr.png")#saving the generated qr in specifed path

