import cv2
import glob

# Get all frame file paths
frames = sorted(glob.glob("frame_*.png"))

# Display frames as a video
for frame_path in frames:
    frame = cv2.imread(frame_path)
    cv2.imshow("Animation", frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):  # Display each frame for 100 ms
        break

cv2.destroyAllWindows()
