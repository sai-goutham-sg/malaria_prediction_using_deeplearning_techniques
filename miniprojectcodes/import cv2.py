import cv2

# Initialize camera
camera = cv2.VideoCapture(0)

# Initialize video recorder
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))

# Main loop
while True:
    # Read frame from camera
    ret, frame = camera.read()

    # Write frame to video recorder
    video_out.write(frame)

    # Display frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
camera.release()
video_out.release()
cv2.destroyAllWindows()


