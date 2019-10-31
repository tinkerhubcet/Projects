# Face Recognition with OpenCV and Python

## Introduction

What is face recognition? Or what is recognition? When you look at an apple fruit, your mind immediately tells you that this is an apple fruit. This process, your mind telling you that this is an apple fruit is recognition in simple words. So what is face recognition then? I am sure you have guessed it right. When you look at your friend walking down the street or a picture of her, you recognize that she is your friend Jolly😉. Interestingly when you look at your friend or a picture of her, you look at her face first before looking at anything else. Ever wondered why you do that? This is so that you can recognize him by looking at his face. Well, this is you doing face recognition. 

But the real question is how does face recognition works? It is quite simple and intuitive. Take a real life example, when you meet someone first time in your life you don't recognize him, right? While he talks or shakes hands with you, you look at his face, eyes, nose, mouth, color and overall look. This is your mind learning or training for the face recognition of that person by gathering face data. Then she tells you that her name is Jolly(Take a good look at that face!). At this point your mind knows that the face data it just learned belongs to Jolly. Now your mind is trained and ready to do face recognition on Jolly's face. Next time when you will see her or her face in a picture you will immediately recognize her. This is how face recognition work. The more you will meet her, the more data your mind will collect about Jolly and especially her face and the better you will become at recognizing him. 

Now the next question is how to code face recognition with OpenCV, after all this is the only reason why you are reading this article, right? OK then. You might say that our mind can do these things easily but to actually code them into a computer is difficult? Don't worry, it is not. Thanks to OpenCV, coding face recognition is as easier as it feels. The coding steps for face recognition are same as we discussed it in real life example above.

## OpenCV Face Recognizers

OpenCV has three built in face recognizers and thanks to OpenCV's clean coding, you can use any of them by just changing a single line of code. Below are the names of those face recognizers and their OpenCV calls. 

1. EigenFaces Face Recognizer Recognizer - `cv2.face.createEigenFaceRecognizer()`
2. FisherFaces Face Recognizer Recognizer - `cv2.face.createFisherFaceRecognizer()`
3. Local Binary Patterns Histograms (LBPH) Face Recognizer - `cv2.face.createLBPHFaceRecognizer()`

# Coding Face Recognition with OpenCV

The Face Recognition process in this program is divided into three steps.

1. **Prepare training data:** In this step we will read training images for each person/subject along with their labels, detect faces from each image and assign each detected face an integer label of the person it belongs to.
2. **Train Face Recognizer:** In this step we will train OpenCV's LBPH face recognizer by feeding it the data we prepared in step 1.
3. **Testing:** In this step we will pass some test images to face recognizer and see if it predicts them correctly.
