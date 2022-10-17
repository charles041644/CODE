import cv2 
import numpy as np
import sys 




# rotate
def rotate(image, angle, center=None, scale=0.5):
    # 圖像長寬
    (h, w) = image.shape[:2]
 
    # 中心點
    if center is None:
        center = (w / 2, h / 2)
    # 旋轉
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

if __name__ == '__main__':
    image = cv2.imread(r'NTHU_CV_HW1/rotate_raw2.jpg')
    # img_1 = cv2.imread(r'NTHU_CV_HW1/1a_notredame.jpg')
    # img_2 = cv2.imread(r'NTHU_CV_HW1/1b_notredame.jpg')
    # img_3 = cv2.imread(r'NTHU_CV_HW1/chessboard-hw1.jpg')
    # check
    if image is None:
        print("Could not open or find the image")
        sys.exit()
    rotated = rotate(image, 30)
    cv2.imwrite("RotateScale_cornerdection_2.jpg",rotated)
    # cv2.imshow("Rotated by 30 Degrees", rotated)
    # cv2.imshow("image",image)
    # image = np.shape(image)
    # center = (image[0] / 2, image[1] / 2)
    # # threshold = 4
    # """
    # rotate
    # cv2.getRotationMatrix2D(center, angel, scale)
    # """
    # rotate = cv2.getRotationMatrix2D(center, 30, 1)
    
    # image_rotate = cv2.warpAffine(image, rotate, (image[0], image[1]))
    # cv2.imshow("image_rotate",image_rotate)

    # cv2.imwrite('image_rotate.jpg', image_rotate)
    # #image_path = 'image_rotate.jpg'
    # """
    # warpAffine
    # cv2.warpAffine(image, scale, (w,h))
    # """
    # scale = cv2.getRotationMatrix2D(center, 0, 0.5)
    # image_scale = cv2.warpAffine(image, scale, (image[1], image[0])) 
    # cv2.imwrite('image_scale.jpg', image_scale)
    # #image_path = 'image_scale.jpg'

    cv2.waitKey(0)
    cv2.destroyAllWindows()