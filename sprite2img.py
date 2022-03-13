import numpy as np
import cv2
with open('sample2.nes','rb') as f:
    b=f.read()
    characterROMPages=b[5]
    characterROMStart = 0x0010 + b[4] * 0x4000
    characterROMEnd = characterROMStart + b[5] * 0x2000
    characterROM = b[characterROMStart:characterROMEnd]
    CR_SIZE=b[5] * 0x2000

    IMG_W_NUM=64
    IMG_H_NUM=int(CR_SIZE/16/IMG_W_NUM)
    IMG_W=int(IMG_W_NUM*8)
    IMG_H=int(IMG_H_NUM*8)
    sp1=np.zeros((8,8))
    sp2=np.zeros((8,8))
    out_img=np.zeros((IMG_H,IMG_W))
    for hj in range(IMG_H_NUM):
        for wj in range(IMG_W_NUM):
            for i in range(8):
                j_idx=hj*16*IMG_W_NUM+wj*16
                sp1[i,:]=np.array(list(bin(characterROM[j_idx+i])[2:].zfill(8)))
                sp2[i,:]=np.array(list(bin(characterROM[j_idx+8+i])[2:].zfill(8)))
            out=sp1*85+sp2*170
            out_img[8*hj:8*hj+8,wj*8:wj*8+8]=out
    cv2.imwrite('out.png',out_img)
