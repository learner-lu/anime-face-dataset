import cv2
import sys
import os.path
from glob import glob
import argparse
import time
COUNT = 1

def detect(filename, output,cascade_file="animeface.xml"):
    global COUNT
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(24, 24))
    for i, (x, y, w, h) in enumerate(faces):
        face = image[y: y + h, x:x + w, :]
        face = cv2.resize(face, (256, 256))
        save_filename = '%s-%d.jpg' % (os.path.basename(filename).split('.')[0], COUNT)
        COUNT += 1
        cv2.imwrite(os.path.join(output,save_filename), face)


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='face detector')
    parser.add_argument('-i', '--input', help='input image file', required=True)
    parser.add_argument('-o', '--output',default='faces', help='output directory')
    args = parser.parse_args()
    if not os.path.isdir(args.output):
        os.makedirs(args.output)
    
    file_list = os.listdir(args.input)
    for filename in file_list:
        file_name = os.path.join(args.input,filename)
        try:
            detect(file_name,args.output)
        except Exception as e:
            print(e)
            print(file_name)

    # file_name = 'imgs/341501.jpg'
    # detect(file_name)
