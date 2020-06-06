import cv2

def frame_diff(prev_frame, cur_frame, next_frame):
    diff_frames_1 = cv2.absdiff(next_frame, cur_frame)
    diff_frames_2 = cv2.absdiff(cur_frame, prev_frame)


    return cv2.bitwise_and(diff_frames_1,diff_frames_2)

## Below is the funtion to grab current frame from webcam

def get_frame(cap, scaling_factor):
    _, frame = cap.read()

    ## resizing the image based on the scaling factor and returning it

    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)


    ##### Converting the image to gray scale and returning it

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    return gray

### define the main function and initialize the video capturing object

if  __name__ == '__main__':
    ####Defining the video capturing object
    cap = cv2.VideoCapture(0)
    ####Definig the scaling factor
    scaling_factor = 0.7
    ###grab the current frame
    cur_frame = get_frame(cap,scaling_factor)
    prev_frame = get_frame(cap,scaling_factor)
    next_frame = get_frame(cap, scaling_factor)

    while True :
        cv2.imshow("Object Movement", frame_diff(prev_frame,cur_frame, next_frame))
        prev_framsde=cur_frame
        cur_frame=next_frame

        next_frame=get_frame(cap,scaling_factor)
        ##Check if user pressed esc key if so break

        key = cv2.waitKey(1000)
        if key == 27 :
            break

        cv2.destroyAllWindows()


