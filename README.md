# Barcode_detection
- Provide barcode detection and object detection using open-cv and pyzbar 

- The respective code (barcode.py) provide better results when there will be sparse clutter of objects. (not perform well in dense clutter)
# Installation
Install open-cv:
 1. sudo apt-get install opencv-python

Install pyzbar library:
 1. pip install pyzbar (Read one-dimensional barcodes and QR codes from Python 2 and 3.)


# Example usage of pyzbar library
The decode function accepts instances of PIL.Image.
>>> from pyzbar.pyzbar import decode
>>> from PIL import Image
>>> decode(Image.open('pyzbar/tests/code128.png'))
```[
    Decoded(
        data=b'Foramenifera', type='CODE128',
        rect=Rect(left=37, top=550, width=324, height=76),
        polygon=[
            Point(x=37, y=551), Point(x=37, y=625), Point(x=361, y=626),
            Point(x=361, y=550)
        ],
        orientation="UP",
        quality=77
    )
    Decoded(
        data=b'Rana temporaria', type='CODE128',
        rect=Rect(left=4, top=0, width=390, height=76),
        polygon=[
            Point(x=4, y=1), Point(x=4, y=75), Point(x=394, y=76),
            Point(x=394, y=0)
        ],
        orientation="UP",
        quality=77
    )
]```



 
 
