import cv2
cap = cv2.VideoCapture(0)

def get_next_frame():
    img = None
    if cap.isOpened():
        _, img = cap.read()
    return img

def main():
    while cv2.waitKey(10) != 27:
        img = get_next_frame()
        if img is None:
            print 'No webcam detected!'
            break
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(grey, (5,5), 0)
        ret, thresh1 = cv2.threshold(blur, 70, 255,
                                     cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        cv2.imshow('input', thresh1)

if __name__ == '__main__':
    main()
