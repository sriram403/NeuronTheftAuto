import cv2

def collect_roi_coordinates(image_path):
    # Read the image
    image = cv2.imread(image_path)
    clone = image.copy()  # Create a copy of the image for drawing
    coordinates = []

    def draw_points(event, x, y, flags, param):
        nonlocal clone, coordinates
        
        if event == cv2.EVENT_LBUTTONDOWN:  # Check for left mouse button click
            coordinates.append((x, y))  # Add the coordinates to the list
            cv2.circle(clone, (x, y), 5, (0, 0, 255), -1)  # Draw a red circle
            if len(coordinates) > 1:
                cv2.line(clone, coordinates[-2], coordinates[-1], (0, 0, 255), 2)  # Draw line connecting points

            cv2.imshow("Image", clone)  # Show the updated image

    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", draw_points)

    while True:
        cv2.imshow("Image", clone)
        key = cv2.waitKey(1)  # Wait for a key press
        if key == 27:  # Exit on 'ESC' key
            break

    cv2.destroyAllWindows()
    return coordinates