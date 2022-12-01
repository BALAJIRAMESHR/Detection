import cv2

face_cascade=cv2.CascadeClassifier(r'C:\Users\Balaji\Documents\PYTHON codes\opencv\haarcascade_frontalface_default.xml')
image = cv2.imread(r"C:\Users\Balaji\Documents\PYTHON codes\opencv\image\Elon_musk.jpg")





gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)




faces=face_cascade.detectMultiScale(gray)

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w, y+h),(255,0,0),2)


# image = cv2.imread("C:\Users\Balaji\Documents\PYTHON codes\opencv\image\balaji.jfif")

    

cv2.putText(image, 'Elon musk',(15,120), cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2) 
                  

cv2.imshow('img',image)

    
   
cv2.waitKey(0)
