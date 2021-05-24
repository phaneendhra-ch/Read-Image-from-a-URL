import urllib.request
import numpy as np
import cv2

url_image = "https://i.ibb.co/tcb11Hb/danger-toxic-skull-wallpaper-1536x2048-115-203.jpg"

with urllib.request.urlopen(url_image) as emb :
	e = emb.read()

img_emb = np.array(bytearray(e),dtype=np.uint8)

img_emb1 = cv2.imdecode(img_emb,1)
cv2.imshow('dsads',img_emb1)

