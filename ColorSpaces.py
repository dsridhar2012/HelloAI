import cv2
import numpy as np

def get_frame(cap, scaling_factor):
    _, frame =cap.read()
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    return frame

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    scaling_factor = 0.5
    while True:
        frame = get_frame(cap,scaling_factor)
        ##### Converting the image to HSV color space using the inbuild fucntion available in OpenCV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower = np.array([0,70, 60])
        upper = np.array([50, 150, 255])
        ### Threshold the HSV image to get only skin color
        mask = cv2.inRange(hsv, lower, upper)
        img_bitwise_and = cv2.bitwise_and(frame, frame, mask=mask)
        ## RUN the median blugging to smooth the image
        img_median_blurred = cv2.medianBlur(img_bitwise_and, 5)  ##### read more on this
        ####Display the input and output frames
        cv2.imshow("input", frame)
        cv2.imshow("output", img_median_blurred)
        c = cv2.waitKey(1000)
        if c == 27:
            break
        cv2.destroyAllWindows()

