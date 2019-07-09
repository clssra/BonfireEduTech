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

ipvale2 = 'http://10.17.2.46:8080/shot.jpg?rnd=562303'

def calculateCenters (x1,y1,x2,y2):
    c=[]
    c.append((x1+x2)/2)
    c.append((y1+y2)/2)
    return c

def checkdist(x1,y1,x2,y2,distmax=45):
    d = math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    if d <= distmax:
        return 1
    else:
        return 0



#-----------------------------------------------
ssl._create_default_https_context = ssl._create_unverified_context
#wget.download(ipvale)

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib import urlopen

#cap = cv2.VideoCapture(0)



while(True):

    cap = cv2.VideoCapture(ipvale2)

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

        # E = m * c 2
        # m = E / 2
        # c = radice E / m 

        centers = [[],[],[],[],[],[],[],[]]
        cornerID = [[],[],[],[],[],[],[],[]]


        if type(ids) is np.ndarray:
            #print(ids.size)
            for i in range(ids.size):
                if ids[i][0] > 7:
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

        #se vede il marker disegna i centri

        sound = NSSound.alloc()
        #-------------------------------------------------------------
        '''
        E = m*c^2
        '''

        f=0
        g=0


        if centers[0] and centers[1] and centers[2] and centers[3] and centers[4] and centers[5]:
        	# E 0 = 1 
        	if(checkdist(cornerID[0][0][0], cornerID[0][0][1], cornerID[1][1][0], cornerID[1][1][1]) and checkdist(cornerID[0][3][0], cornerID[0][3][1], cornerID[1][2][0], cornerID[1][2][1])):
        		f+=1
        	# = 1 m 2
        	if checkdist(cornerID[1][0][0], cornerID[1][0][1], cornerID[2][1][0], cornerID[2][1][1]) and checkdist(cornerID[1][3][0], cornerID[1][3][1], cornerID[2][2][0], cornerID[2][2][1]):
        	 	f+=1
        	# m 2 * 3
        	if checkdist(cornerID[2][0][0], cornerID[2][0][1], cornerID[3][1][0], cornerID[3][1][1]) and checkdist(cornerID[2][3][0], cornerID[2][3][1], cornerID[3][2][0], cornerID[3][2][1]):
        		f+=1
        	# * 3 c 4
        	if (checkdist(cornerID[3][0][0], cornerID[3][0][1], cornerID[4][1][0], cornerID[4][1][1]) and checkdist(cornerID[3][3][0], cornerID[3][3][1], cornerID[4][2][0], cornerID[4][2][1])):
        		f+=1
        	# # c 4 ^2 5

        	if (checkdist(cornerID[4][0][0], cornerID[4][0][1], cornerID[5][2][0], cornerID[5][2][1])):
        		f+=1

        	if f==5:
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # cv2.putText(gray,'AFFERMATIVE SENTENCE',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            #sleep(0.2)
	            sound.initWithContentsOfFile_byReference_('/Users/saracolosio/Downloads/sting.wav', True)
	            sound.play()

	            # font = cv2.FONT_HERSHEY_TRIPLEX
	            # cv2.putText(gray,'GREAT JOB -- H2O',(20,100), font, 1,(0,255,0),3,cv2.LINE_AA)
	            sleep(sound.duration())
	            sleep(1.5)
        	
        	# E 0, = 1, m 2, * 3, c 4, ^2 5, --- 6, radice 7


        	# for i in range(5):
        	# 	if(checkdist(cornerID[i][0][0], cornerID[i][0][1], cornerID[i+1][1][0], cornerID[i+1][1][1]) and checkdist(cornerID[i][3][0], cornerID[i][3][1], cornerID[i+1][2][0], cornerID[i+1][2][1])):
        	# 		f+=1

         #-----------------------------------------------------------------

        '''									 ___________
		         E   						| 1		  0 |
		  m =  -----  			---->     	|           |
				   2						| 2		  3	|
				 c  						 __________
-        '''
		
		
        if centers[0] and centers[1] and centers[2] and centers[4] and centers[5] and centers[6]:
            # m 2 = 1
            if (checkdist(cornerID[2][0][0], cornerID[2][0][1], cornerID[1][1][0], cornerID[1][1][1]) and checkdist(cornerID[2][3][0], cornerID[2][3][1], cornerID[1][2][0], cornerID[1][2][1])):
            #    font = cv2.FONT_HERSHEY_SIMPLEX
                g+=1
            #    cv2.putText(gray,'yeeee 0-1',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            # = 1 --- 6
            if (checkdist(cornerID[1][0][0], cornerID[1][0][1], cornerID[6][1][0], cornerID[6][1][1]) and checkdist(cornerID[1][3][0], cornerID[1][3][1], cornerID[6][2][0], cornerID[6][2][1])):
            #    font = cv2.FONT_HERSHEY_SIMPLEX
                g+=1
            #    cv2.putText(gray,'yeeee 1-2',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            # -- 6 E 0
            if (checkdist(cornerID[6][0][0], cornerID[6][0][1], cornerID[0][3][0], cornerID[0][3][1]) and checkdist(cornerID[6][1][0], cornerID[6][1][1], cornerID[0][2][0], cornerID[0][2][1])):
            #    font = cv2.FONT_HERSHEY_SIMPLEX
                g+=1
            #    cv2.putText(gray,'yeeee 2-3',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            # --- 6 2 5
            if (checkdist(cornerID[6][3][0], cornerID[6][3][1], cornerID[5][1][0], cornerID[5][1][1])):
                #font = cv2.FONT_HERSHEY_SIMPLEX
                g+=1
            #    cv2.putText(gray,'yeeee 3-4',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            # 2 5 c 4
            if (checkdist(cornerID[4][0][0], cornerID[4][0][1], cornerID[5][2][0], cornerID[5][2][1])):
                #font = cv2.FONT_HERSHEY_SIMPLEX
                g+=1
                #cv2.putText(gray,'yeeee 4-5',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)

        if g==5:
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # cv2.putText(gray,'AFFERMATIVE SENTENCE',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            #sleep(0.2)
            sound.initWithContentsOfFile_byReference_('/Users/saracolosio/Downloads/sting.wav', True)
            sound.play()

            # font = cv2.FONT_HERSHEY_TRIPLEX
            # cv2.putText(gray,'GREAT JOB -- H2O',(20,100), font, 1,(0,255,0),3,cv2.LINE_AA)
            sleep(sound.duration())
            sleep(1.5)

#-------------------------------------------------------------------------------------------------

        '''

        	# E 0, = 1, m 2, * 3, c 4, ^2 5, --- 6, radice 7

        4 1  7 6, 6 0, 6 2 	
       										 ___________
		      |   E   						| 1		  0 |
		  c = v -----  			---->     	|           |
				 m 							| 2		  3	|
				 	 						 __________
-       
        '''
        h=0
        if centers[0] and centers[1] and centers[2] and centers[4] and centers[6] and centers[7]:
            # c 4 = 1 
            if (checkdist(cornerID[4][0][0], cornerID[4][0][1], cornerID[1][1][0], cornerID[1][1][1]) and checkdist(cornerID[4][3][0], cornerID[4][3][1], cornerID[1][2][0], cornerID[1][2][1])):
            #    font = cv2.FONT_HERSHEY_SIMPLEX
                h+=1
            #    cv2.putText(gray,'yeeee 0-1',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            # = 1 v 7
            if (checkdist(cornerID[1][0][0], cornerID[1][0][1], cornerID[7][1][0], cornerID[7][1][1]) and checkdist(cornerID[1][3][0], cornerID[1][3][1], cornerID[7][2][0], cornerID[7][2][1])):
            #    font = cv2.FONT_HERSHEY_SIMPLEX
                h+=1
            #    cv2.putText(gray,'yeeee 1-2',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            # v 7 -- 6
            if (checkdist(cornerID[7][0][0], cornerID[7][0][1], cornerID[6][1][0], cornerID[6][1][1]) and checkdist(cornerID[7][3][0], cornerID[7][3][1], cornerID[6][2][0], cornerID[6][2][1])):
            #    font = cv2.FONT_HERSHEY_SIMPLEX
                h+=1
            #    cv2.putText(gray,'yeeee 2-3',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            # -- 6 E 0
            if (checkdist(cornerID[6][1][0], cornerID[6][1][1], cornerID[0][2][0], cornerID[0][2][1]) and checkdist(cornerID[6][0][0], cornerID[6][0][1], cornerID[0][3][0], cornerID[0][3][1])):
                #font = cv2.FONT_HERSHEY_SIMPLEX
                h+=1
            #    cv2.putText(gray,'yeeee 3-4',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            # --- 6 m 2
            if (checkdist(cornerID[6][2][0], cornerID[6][2][1], cornerID[2][1][0], cornerID[2][1][1]) and checkdist(cornerID[6][3][0], cornerID[6][3][1], cornerID[2][0][0], cornerID[2][0][1])):
                #font = cv2.FONT_HERSHEY_SIMPLEX
                h+=1
                #cv2.putText(gray,'yeeee 4-5',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            
        if h==5:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(gray,'QUESTION',(20,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            #sleep(0.2)
            sound.initWithContentsOfFile_byReference_('/Users/saracolosio/Downloads/sting.wav', True)
            sound.play()

            # font = cv2.FONT_HERSHEY_TRIPLEX
            # cv2.putText(gray,'GREAT JOB -- H2O',(20,100), font, 1,(0,255,0),3,cv2.LINE_AA)
            sleep(sound.duration())
            sleep(1)



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