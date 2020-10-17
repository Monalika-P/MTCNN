from mtcnn.mtcnn import MTCNN
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import cv2
import mtcnn

folder = 'datasets/'


def draw_faces(data, result_list, j):
    for i in range(len(result_list)):
        # get coordinates
        x1, y1, width, height = result_list[i]['box']
        x2, y2 = x1 + width, y1 + height
        #print(A)

        # plot face
        cv2.imshow("Object Detected", data[y1:y2, x1:x2])
        filename = folder + 'Mona' + str(j) + '.jpg'
        cv2.imwrite(filename, data[y1:y2, x1:x2])

detector = MTCNN()

# import the opencv library
import cv2

# define a video capture object
camera = cv2.VideoCapture(0)
j = 0

while (True):

    # Capture the video frame
    # by frame
    return_value, image = camera.read()

    # Display the resulting frame
    cv2.imshow("Image", image)
    faces = detector.detect_faces(image)
    draw_faces(image, faces, j)
    j = j + 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if j == 50:
        break

# After the loop release the cap object
camera.release()
# Destroy all the windows
cv2.destroyAllWindows()
