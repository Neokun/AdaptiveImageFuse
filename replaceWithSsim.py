import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage.measure import compare_ssim as ssim

def replaceWithSsim(I, P, win_size=None, threshold=None):
    """Compute the mean structural similarity index between two images then replace I by P
        Input:
            I: the multispectral intensity
            P: the panchromatic image
            win_size: kich thuoc cua so truot NxN
            threshold: nguong nho nhat de thay I[x,y] = P[x,y]
                        mac dinh la mean SSIM
        Output:
            new I
    """

    mssim, ssim_image = ssim(I, P, win_size=win_size, full=True, multichannel=True)
    if (threshold == None):
        threshold = mssim

    # cv2.imshow("ssim_image", ssim_image)
    # cv2.waitKey(0)
    # print(threshold)

    n, m = I.shape
    I_new = I.copy()

    for i in range(n):
        for j in range(m):
            if (ssim_image[i][j] >= threshold):
                I_new[i][j] = P[i][j]

    # cv2.imshow("I_new", I_new)
    # cv2.waitKey(0)

    return I_new

# I = cv2.imread('./Input/10_MS.png', cv2.IMREAD_GRAYSCALE)
# cv2.imshow("test",I)
# cv2.waitKey(0)
# P = cv2.imread('./Input/10_PAN.png', cv2.IMREAD_GRAYSCALE)
# cv2.imshow("test",P)
# cv2.waitKey(0)
# replaceWithSsim(I, P, 7)