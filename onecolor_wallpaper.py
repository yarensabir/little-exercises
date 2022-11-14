import cv2
import mediapipe as mp
import numpy as np

def rgb_to_bgr(r,g,b):
    bgr = [b,g,r]
    return bgr
    
def bgr_to_rgb(b,g,r):
    rgb = [r,g,b]
    return rgb

def make_pic(r,g,b, height = 2000, width = 2000):   
    img = np.zeros((height,width,3), np.uint8)
    img[:,:] = rgb_to_bgr(r,g,b)
    name = "/home/yaren/Documents/.nft/?/(" + str(r) +","+ str(g)+"," + str(b) +").png"
    cv2.imwrite(name, img)
    cv2.imshow('img',img)
    cv2.waitKey(10)

make_pic(143,105,99)