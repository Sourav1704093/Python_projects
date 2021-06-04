import pyqrcode

def qrcode():
    q = pyqrcode.create(input())
    q.png('gen_qrcode.png',scale=7)
    print('qrcode generated')

if __name__=='__main__':
    qrcode()