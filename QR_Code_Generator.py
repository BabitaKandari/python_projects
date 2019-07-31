import pyqrcode
import png
def qr_code():
    q=pyqrcode.create("hello QR code")
    q.png('my.png',scale=6)
    print("QR code generated")

if __name__ == "__main__":
    qr_code()