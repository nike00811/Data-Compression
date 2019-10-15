import cv2
from math import log
import numpy as np

img = cv2.imread("moomin.png", 0)
# img = cv2.resize(img, (400,400))v
___, img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
img = img.flatten()
while len(img) % 3 != 0:
	img = np.append(img, 0)
print(img.shape)
bbb = 0
bbw = 0
bwb = 0
bww = 0
wbb = 0
wbw = 0
wwb = 0
www = 0

for i in range(0,len(img),3):
	if   img[i] ==   0 and img[i+1] ==   0 and img[i+2] ==   0:
		bbb+=1
	elif img[i] ==   0 and img[i+1] == 255 and img[i+2] ==   0:
		bbw+=1
	elif img[i] ==   0 and img[i+1] ==   0 and img[i+2] == 255:
		bwb+=1
	elif img[i] ==   0 and img[i+1] == 255 and img[i+2] == 255:
		bww+=1
	elif img[i] == 255 and img[i+1] ==   0 and img[i+2] ==   0:
		wbb+=1
	elif img[i] == 255 and img[i+1] ==   0 and img[i+2] == 255:
		wbw+=1
	elif img[i] == 255 and img[i+1] == 255 and img[i+2] ==   0:
		wwb+=1
	elif img[i] == 255 and img[i+1] == 255 and img[i+2] == 255:
		www+=1
print("bbb = "+str(bbb))
print("bbw = "+str(bbw))
print("bwb = "+str(bwb))
print("bww = "+str(bww))
print("wbb = "+str(wbb))
print("wbw = "+str(wbw))
print("wwb = "+str(wwb))
print("www = "+str(www))
prob_bbb = bbb/(bbb+wbb)
prob_bbw = bbw/(bbw+wbw)
prob_bwb = bwb/(bwb+wwb)
prob_bww = bww/(bww+www)
prob_wbb = wbb/(bbb+wbb)
prob_wbw = wbw/(bbw+wbw)
prob_wwb = wwb/(bwb+wwb)
prob_www = www/(bww+www)
prob_b = 0
prob_w = 0
for i in img:
	if i == 0:
		prob_b+=1
	elif i == 255:
		prob_w+=1
prob_b /= len(img)
prob_w /= len(img)
print("prob_b = "+str(prob_b))
print("prob_w = "+str(prob_w))
print(prob_w+prob_b)
print("prob_bbb = "+str(prob_bbb))
print("prob_bbw = "+str(prob_bbw))
print("prob_bwb = "+str(prob_bwb))
print("prob_bww = "+str(prob_bww))
print("prob_wbb = "+str(prob_wbb))
print("prob_wbw = "+str(prob_wbw))
print("prob_wwb = "+str(prob_wwb))
print("prob_www = "+str(prob_www))
hw = -prob_bbw*log(prob_bbw, 2)
hw -= prob_bww*log(prob_bww, 2)
hw -= prob_wbw*log(prob_wbw, 2)
hw -= prob_www*log(prob_www, 2)

hb = -prob_bbb*log(prob_bbb, 2)
hb -= prob_bwb*log(prob_bwb, 2)
hb -= prob_wbb*log(prob_wbb, 2)
hb -= prob_wwb*log(prob_wwb, 2)

print("H(w) = "+str(hw))
print("H(b) = "+str(hb))
print("H = "+str(prob_b*hb+prob_w*hw))