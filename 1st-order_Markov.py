import cv2
from math import log
import numpy as np

img = cv2.imread("moomin.png", 0)
# img = cv2.resize(img, (400,400))
___, img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# cv2.imwrite("lalala.png",img)
img = img.flatten()

print(img.shape)

bb = 0
bw = 0
wb = 0
ww = 0

for i in range(0,len(img),2):
	if img[i] == 0 and img[i+1] == 0:
		bb += 1
	elif img[i] == 0 and img[i+1] == 255:
		bw += 1
	elif img[i] == 255 and img[i+1] == 0:
		wb += 1
	elif img[i] == 255 and img[i+1] == 255:
		ww += 1
print("bb = "+str(bb))
print("bw = "+str(bw))
print("wb = "+str(wb))
print("ww = "+str(ww))
prob_bb = bb/(bb+wb)
prob_bw = bw/(bw+ww)
prob_wb = wb/(bb+wb)
prob_ww = ww/(bw+ww)
prob_b = (bw+wb+2*bb)/(2*(bb+bw+wb+ww))
prob_w = (bw+wb+2*ww)/(2*(bb+bw+wb+ww))
print("prob_bb = "+str(prob_bb))
print("prob_bw = "+str(prob_bw))
print("prob_wb = "+str(prob_wb))
print("prob_ww = "+str(prob_ww))
print("prob_b = "+str(prob_b))
print("prob_w = "+str(prob_w))
# entropy = -prob_bb*log(prob_bb, 2)
# entropy -= prob_bw*log(prob_bw, 2)
# entropy -= prob_wb*log(prob_wb, 2)
# entropy -= prob_ww*log(prob_ww, 2)
# print("entropy = "+str(entropy))
hw = -prob_ww*log(prob_ww, 2) - prob_bw*log(prob_bw, 2)
hb = -prob_bb*log(prob_bb, 2) - prob_wb*log(prob_wb, 2)
print("H(w) = "+str(hw))
print("H(b) = "+str(hb))
print("H = "+str(prob_b*hb+prob_w*hw))