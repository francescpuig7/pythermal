from escpos.printer import Usb

""" Set your VendorId, ProductId -> See the readme.md """
p = Usb(0x20d1, 0x7007)
p.text("Hello World\n")
p.cut()
