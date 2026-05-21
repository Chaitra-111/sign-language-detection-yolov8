import cv2
import os
import time
import uuid

# =========================
# LABELS / CLASSES
# =========================
labels = ['hello', 'thanks', 'yes', 'no']

# Number of images per label
number_imgs = 10

# Base image path
IMAGES_PATH = os.path.join(
    'Tensorflow',
    'workspace',
    'images',
    'collectedimages'
)

# =========================
# CREATE FOLDERS
# =========================
for label in labels:
    path = os.path.join(IMAGES_PATH, label)
    os.makedirs(path, exist_ok=True)

print("\nFolders created successfully!")

# =========================
# START IMAGE COLLECTION
# =========================
for label in labels:

    print(f"\n========== Collecting for: {label} ==========")

    # Open webcam
    cap = cv2.VideoCapture(0)

    # Check webcam
    if not cap.isOpened():
        print("ERROR: Cannot open webcam")
        break

    # Countdown before capture
    for i in range(5, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)

    imgnum = 0

    while imgnum < number_imgs:

        ret, frame = cap.read()

        # If frame not captured
        if not ret:
            print("Failed to capture frame")
            continue

        # Flip camera for mirror effect
        frame = cv2.flip(frame, 1)

        # Add text on screen
        cv2.putText(
            frame,
            f'Label: {label} | Image: {imgnum + 1}/{number_imgs}',
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Press 'C' to Capture | 'Q' to Quit",
            (10, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

        # Show webcam
        cv2.imshow('Image Collection', frame)

        key = cv2.waitKey(1) & 0xFF

        # =========================
        # PRESS C TO CAPTURE
        # =========================
        if key == ord('c'):

            imgname = os.path.join(
                IMAGES_PATH,
                label,
                f'{label}.{uuid.uuid1()}.jpg'
            )

            cv2.imwrite(imgname, frame)

            print(f"Captured: {imgname}")

            imgnum += 1

            # Small delay after capture
            time.sleep(0.5)

        # =========================
        # PRESS Q TO QUIT
        # =========================
        elif key == ord('q'):
            print("\nExiting...")
            cap.release()
            cv2.destroyAllWindows()
            exit()

        # =========================
        # CLOSE WINDOW BUTTON
        # =========================
        if cv2.getWindowProperty('Image Collection', cv2.WND_PROP_VISIBLE) < 1:
            print("\nWindow closed")
            cap.release()
            cv2.destroyAllWindows()
            exit()

    # Release webcam after each label
    cap.release()
    cv2.destroyAllWindows()

print("\n========== IMAGE COLLECTION COMPLETED ==========")