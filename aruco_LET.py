import numpy as np
import cv2
import cv2.aruco as aruco
import math
import wget
import ssl
import sys
import urllib
from AppKit import NSSound
from time import sleep

ipold = 'http://192.168.1.2:8080/shot.jpg?rnd=189828'
ipnew = 'http://192.168.1.9:8080/shot.jpg?rnd=436060'
ipxia = 'https://192.168.1.14:8080/shot.jpg?rnd=142522'
ipfab = 'https://172.20.10.13:8080/shot.jpg?rnd=245139'
ipvale = 'https://192.168.43.140:8080/shot.jpg?rnd=94568'
ipnico = 'https://192.168.43.140:8080/shot.jpg?rnd=565089'

def calculateCenters (x1,y1,x2,y2):
    c=[]
    c.append((x1+x2)/2)
    c.append((y1+y2)/2)
    return c

def checkdist(x1,y1,x2,y2,distmax=40):
    d = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    if d <= distmax:
        return 1
    else:
        return 0
#-------------------------------------------------

'''
NIPOTE
PITONE
TOPINE
'''


#-----------------------------------------------
ssl._create_default_https_context = ssl._create_unverified_context
#wget.download(ipfab)

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib import urlopen

#cap = cv2.VideoCapture(0)



while(True):

    cap = cv2.VideoCapture(ipfab)

    if cap.isOpened():
        #print("Device Opened\n")



        # Capture frame-by-frame
        ret, frame = cap.read()
        #print(frame.shape) #480x640
        # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = frame;
        aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
        parameters =  aruco.DetectorParameters_create()

        #print(parameters)

    #    '''    detectMarkers(...)
    #        detectMarkers(image, dictionary[, corners[, ids[, parameters[, rejectedI
    #        mgPoints]]]]) -> corners, ids, rejectedImgPoints
    #        '''
        #lists of ids and the corners beloning to each id
        corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
        #print(corners)
        print("\n")

        # THE PEN IS ON THE TABLE
        # IS THE PEN ON THE TABLE ?

        centers = [[],[],[],[],[],[],[]]
        cornerID = [[],[],[],[],[],[],[]]


        if type(ids) is np.ndarray:
            #print(ids.size)
            for i in range(ids.size):
                if ids[i][0] > 6:
                    print("Sono un programma di merdaaa!!")
                else:
                    centers[ids[i][0]] = calculateCenters(corners[i][0][0][0], corners[i][0][0][1], corners[i][0][2][0], corners[i][0][2][1])
                    cornerID[ids[i][0]] = (corners[i][0][0][0], corners[i][0][0][1]), (corners[i][0][1][0], corners[i][0][1][1]), (corners[i][0][2][0], corners[i][0][2][1]),(corners[i][0][3][0], corners[i][0][3][1])
                    print(ids)
                    print(cornerID)
        #print(ids)
            #   print(corners[0])
            #    print(corners[0][0][2])

        #It's working.
        # my problem was that the cellphone put black all around it. The alrogithm
        # depends very much upon finding rectangular black blobs
        #print(centers)
        gray = aruco.drawDetectedMarkers(gray, corners, borderColor=(255, 0, 0))
        sound = NSSound.alloc()
        #se vede il marker disegna i centri


        # if centers[0]:
        #     center0 = (int(centers[0][0]), int(centers[0][1]))
        #     cv2.circle(gray,(center0), 1, (255,0,0), -1)
        #     #cv2.line(gray,(int(centers[1][0]), int(centers[1][1])),(center0),(255,0,0),5)
        # if centers[1]:
        #     center1 = (int(centers[1][0]), int(centers[1][1]))
        #     cv2.circle(gray,(center1), 1, (255,0,0), -1)
        # if centers[2]:
        #     center2 = (int(centers[2][0]), int(centers[2][1]))
        #     cv2.circle(gray,(center2), 1, (255,0,0), -1)
        # if centers[3]:
        #     center0 = (int(centers[3][0]), int(centers[3][1]))
        #     cv2.circle(gray,(center0), 1, (255,0,0), -1)
        # if centers[4]:
        #     center0 = (int(centers[4][0]), int(centers[4][1]))
        #     cv2.circle(gray,(center0), 1, (255,0,0), -1)
        # if centers[5]:
        #     center0 = (int(centers[5][0]), int(centers[5][1]))
        #     cv2.circle(gray,(center0), 1, (255,0,0), -1)
        # if centers[6]:
        #     center0 = (int(centers[6][0]), int(centers[6][1]))
        #     cv2.circle(gray,(center0), 1, (255,0,0), -1)

        # se vede i marker

        #-------------------------------------------------------------
        '''
        NIPOTE  012345
        '''

        f=0
        '''
        FAI IL CHECK SULLE INIZIALI DELLE PAROLEEEEEE!!!!
        '''

        if centers[0] and centers[1] and centers[2] and centers[3] and centers[4] and centers[5]:

            # N 0 I 1
            if (checkdist(cornerID[0][0][0], cornerID[0][0][1], cornerID[1][1][0], cornerID[1][1][1]) and checkdist(cornerID[0][3][0], cornerID[0][3][1], cornerID[1][2][0], cornerID[1][2][1])):
            #    font = cv2.FONT_HERSHEY_SIMPLEX
                f+=1
            #    cv2.putText(gray,'yeeee 0-1',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            # I 1 P 2
            if checkdist(cornerID[1][0][0], cornerID[1][0][1], cornerID[2][1][0], cornerID[2][1][1]) and checkdist(cornerID[1][3][0], cornerID[1][3][1], cornerID[2][2][0], cornerID[2][2][1]):
            #    font = cv2.FONT_HERSHEY_SIMPLEX
                f+=1
            #    cv2.putText(gray,'yeeee 1-2',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            #P 2 O 3
            if checkdist(cornerID[2][0][0], cornerID[2][0][1], cornerID[3][1][0], cornerID[3][1][1]) and checkdist(cornerID[2][3][0], cornerID[2][3][1], cornerID[3][2][0], cornerID[3][2][1]):
            #    font = cv2.FONT_HERSHEY_SIMPLEX
                f+=1
            #    cv2.putText(gray,'yeeee 2-3',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            #O 3 T 4
            if checkdist(cornerID[3][0][0], cornerID[3][0][1], cornerID[4][1][0], cornerID[4][1][1]) and checkdist(cornerID[3][3][0], cornerID[3][3][1], cornerID[4][2][0], cornerID[4][2][1]):
                #font = cv2.FONT_HERSHEY_SIMPLEX
                f+=1
            #    cv2.putText(gray,'yeeee 3-4',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            # T 4 E 5
            if checkdist(cornerID[4][0][0], cornerID[4][0][1], cornerID[5][1][0], cornerID[5][1][1]) and checkdist(cornerID[4][3][0], cornerID[4][3][1], cornerID[5][2][0], cornerID[5][2][1]):
                #font = cv2.FONT_HERSHEY_SIMPLEX
                f+=1
                #cv2.putText(gray,'yeeee 4-5',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)

        if f==5:
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # cv2.putText(gray,'NIPOTEEE',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            #sleep(0.2)
            sound.initWithContentsOfFile_byReference_('/Users/saracolosio/Downloads/sting.wav', True)
            sound.play()
            sleep(sound.duration())
            sleep(1.5)
            #break

#-------------------------------------------------------------------------------------------------
        '''
        PITONE   214305
        '''
        g=0

        if centers[0] and centers[1] and centers[2] and centers[3] and centers[4] and centers[5]:
            # p 2 I 1
            if (checkdist(cornerID[2][0][0], cornerID[2][0][1], cornerID[1][1][0], cornerID[1][1][1]) and checkdist(cornerID[2][3][0], cornerID[2][3][1], cornerID[1][2][0], cornerID[1][2][1])):
            #    font = cv2.FONT_HERSHEY_SIMPLEX
                g+=1
            #    cv2.putText(gray,'yeeee 0-1',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            # I 1 t 4
            if checkdist(cornerID[1][0][0], cornerID[1][0][1], cornerID[4][1][0], cornerID[4][1][1]) and checkdist(cornerID[1][3][0], cornerID[1][3][1], cornerID[4][2][0], cornerID[4][2][1]):
            #    font = cv2.FONT_HERSHEY_SIMPLEX
                g+=1
            #    cv2.putText(gray,'yeeee 1-2',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            # t 4 O 3
            if checkdist(cornerID[4][0][0], cornerID[4][0][1], cornerID[3][1][0], cornerID[3][1][1]) and checkdist(cornerID[4][3][0], cornerID[4][3][1], cornerID[3][2][0], cornerID[3][2][1]):
            #    font = cv2.FONT_HERSHEY_SIMPLEX
                g+=1
            #    cv2.putText(gray,'yeeee 2-3',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            #O 3 n 0
            if checkdist(cornerID[3][0][0], cornerID[3][0][1], cornerID[0][1][0], cornerID[0][1][1]) and checkdist(cornerID[3][3][0], cornerID[3][3][1], cornerID[0][2][0], cornerID[0][2][1]):
                #font = cv2.FONT_HERSHEY_SIMPLEX
                g+=1
            #    cv2.putText(gray,'yeeee 3-4',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            # n 0  E 5
            if checkdist(cornerID[0][0][0], cornerID[0][0][1], cornerID[5][1][0], cornerID[5][1][1]) and checkdist(cornerID[0][3][0], cornerID[0][3][1], cornerID[5][2][0], cornerID[5][2][1]):
                #font = cv2.FONT_HERSHEY_SIMPLEX
                g+=1
                #cv2.putText(gray,'yeeee 4-5',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)

        if g==5:
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # cv2.putText(gray,'PITONEE',(20,100), font, 1,(0,255,0),3,cv2.LINE_AA)
            #sleep(0.2)
            sound.initWithContentsOfFile_byReference_('/Users/saracolosio/Downloads/sting.wav', True)
            sound.play()
            sleep(sound.duration())
            sleep(1.5)
            #break

        #-------------------------------------------------------------
        '''
        TOPINE  432105
        '''

        h=0
        '''
        FAI IL CHECK SULLE INIZIALI DELLE PAROLEEEEEE!!!!
        '''

        if centers[0] and centers[1] and centers[2] and centers[3] and centers[4] and centers[5]:

            # T 4 0 3
            if (checkdist(cornerID[4][0][0], cornerID[4][0][1], cornerID[3][1][0], cornerID[3][1][1]) and checkdist(cornerID[4][3][0], cornerID[4][3][1], cornerID[3][2][0], cornerID[3][2][1])):
            #    font = cv2.FONT_HERSHEY_SIMPLEX
                h+=1
            #    cv2.putText(gray,'yeeee 0-1',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            # 0 3 P 2
            if checkdist(cornerID[3][0][0], cornerID[3][0][1], cornerID[2][1][0], cornerID[2][1][1]) and checkdist(cornerID[3][3][0], cornerID[3][3][1], cornerID[2][2][0], cornerID[2][2][1]):
            #    font = cv2.FONT_HERSHEY_SIMPLEX
                h+=1
            #    cv2.putText(gray,'yeeee 1-2',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            #P 2 I 1
            if checkdist(cornerID[2][0][0], cornerID[2][0][1], cornerID[1][1][0], cornerID[1][1][1]) and checkdist(cornerID[2][3][0], cornerID[2][3][1], cornerID[1][2][0], cornerID[1][2][1]):
            #    font = cv2.FONT_HERSHEY_SIMPLEX
                h+=1
            #    cv2.putText(gray,'yeeee 2-3',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            # I 1 N 0
            if checkdist(cornerID[1][0][0], cornerID[1][0][1], cornerID[0][1][0], cornerID[0][1][1]) and checkdist(cornerID[1][3][0], cornerID[1][3][1], cornerID[0][2][0], cornerID[0][2][1]):
                #font = cv2.FONT_HERSHEY_SIMPLEX
                h+=1
            #    cv2.putText(gray,'yeeee 3-4',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            # N 0 E 5
            if checkdist(cornerID[0][0][0], cornerID[0][0][1], cornerID[5][1][0], cornerID[5][1][1]) and checkdist(cornerID[0][3][0], cornerID[0][3][1], cornerID[5][2][0], cornerID[5][2][1]):
                #font = cv2.FONT_HERSHEY_SIMPLEX
                h+=1
                #cv2.putText(gray,'yeeee 4-5',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)

        if h==5:
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # cv2.putText(gray,'TOPINEEE',(20,100), font, 1,(0,255,0),3,cv2.LINE_AA)
            #sleep(0.2)
            sound.initWithContentsOfFile_byReference_('/Users/saracolosio/Downloads/sting.wav', True)
            sound.play()
            sleep(sound.duration())
            sleep(1.5)
            #break

#-------------------------------------------------------------------------------------------
        '''
        PRINTAAAAA
        '''
        #print(rejectedImgPoints)
        # Display the resulting frame

        cv2.namedWindow("frame", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("frame",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

        cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        print("Failed to open Device\n")

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
