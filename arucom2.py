import numpy as np
import cv2
import cv2.aruco as aruco
#import arucom1
import wget
import ssl
import sys
import urllib

def calculateCenters (x1,y1,x2,y2):
    c=[]
    c.append((x1+x2)/2)
    c.append((y1+y2)/2)
    return c



#-----------------------------------------------
ssl._create_default_https_context = ssl._create_unverified_context
wget.download("http://192.168.1.9:8080/shot.jpg?rnd=327657")

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib import urlopen

#cap = cv2.VideoCapture(0)



while(True):

    cap = cv2.VideoCapture('http://192.168.1.9:8080/shot.jpg?rnd=327657')

    if cap.isOpened():
        #print("Device Opened\n")



        # Capture frame-by-frame
        ret, frame = cap.read()
        #print(frame.shape) #480x640
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
        parameters =  aruco.DetectorParameters_create()

        #print(parameters)

    #    '''    detectMarkers(...)
    #        detectMarkers(image, dictionary[, corners[, ids[, parameters[, rejectedI
    #        mgPoints]]]]) -> corners, ids, rejectedImgPoints
    #        '''
        #lists of ids and the corners beloning to each id
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        print(corners)
        print("\n")

        centers = [[],[],[]]

        if type(ids) is np.ndarray:
            #print(ids.size)
            for i in range(ids.size):
                #print(ids[i][0])
                centers[ids[i][0]] = calculateCenters(corners[i][0][0][0], corners[i][0][0][1], corners[i][0][2][0], corners[i][0][2][1])

            #   print(corners[0])
            #    print(corners[0][0][2])

        #It's working.
        # my problem was that the cellphone put black all around it. The alrogithm
        # depends very much upon finding rectangular black blobs
        print(centers)
        gray = aruco.drawDetectedMarkers(gray, corners, borderColor=(255, 0, 0))
        gray[centers[0][0],centers[0][1]] = [0,0,255]


        #print(rejectedImgPoints)
        # Display the resulting frame
        cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        print("Failed to open Device\n")

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()