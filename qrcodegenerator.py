import qrcode
#i cretae a fuction and function name is generate_qr_code and i given two argument data,filename 
def generate_qr_code(data,filename):
    qr=qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img=qr.make_image(fill_color="black",back_color="white")
    img.save(filename)

#example usege
#and here i given my github account link 
data="https://github.com/pavithrannarayan24"
filename="example_qr.png"
#and here i call function 
generate_qr_code(data,filename)
