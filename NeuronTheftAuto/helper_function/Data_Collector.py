import cv2
import numpy as np
import time
from NeuronTheftAuto.helper_function.keypress import key_check
from PIL import ImageGrab
import os
import pickle

file_name = 'training_data.pkl'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    with open(file_name, 'rb') as file:
        training_data = pickle.load(file)
else:
    print('File does not exist, starting fresh!')
    training_data = []

capture_x, capture_y, capture_width, capture_height = 0, 25, 800, 600
resized_w, resized_h = 80, 60

def keys_to_output(keys):
    #A,W,D,LShift,Space
    output = [0, 0, 0, 0, 0]
    if 'A' in keys:
        output[0] = 1
    if 'W' in keys:
        output[1] = 1
    if 'D' in keys:
        output[2] = 1
    if 'Lshift' in keys:
        output[3] = 1
    if ' ' in keys:
        output[4] = 1
    return output

def main():
    global training_data 
    for i in list(range(5))[::-1]:
        print(i + 1)
        time.sleep(1)
    while True:
        screenshot = ImageGrab.grab(bbox=(capture_x, capture_y, capture_x + capture_width, capture_y + capture_height))
        screen = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen, (resized_w, resized_h))
        keys = key_check()
        output = keys_to_output(keys)
        training_data.append([screen,output])
        if len(training_data) % 100 == 0:
            print(len(training_data))
            with open(file_name, 'wb') as file:
                pickle.dump(training_data, file)
        cv2.imshow('screen', screen)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    main()