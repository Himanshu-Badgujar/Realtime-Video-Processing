import cv2

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use H.264 codec
output_filename = 'output.mp4'  # Use .mp4 file extension
fps = 30
output_dimensions = (640, 480)  # Adjust according to your requirements

# Create a VideoWriter object
out = cv2.VideoWriter(output_filename, fourcc, fps, output_dimensions)

# Start capturing frames
cap = cv2.VideoCapture(0)  # Use 0 for the default webcam, adjust as needed

while True:
    ret, frame = cap.read()  # Read a frame from the video source
    if not ret:
        break

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply blur to the grayscale frame
    blurred_frame = cv2.GaussianBlur(gray_frame, (25, 25), 0)  # Increased kernel size

    # Write the blurred frame to the output
    out.write(blurred_frame)

    # Display the original, grayscale, and blurred frames
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Grayscale Frame', gray_frame)
    cv2.imshow('Blurred Frame', blurred_frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
