import cv2
import os
import time
import uuid

# Labels/classes
labels = ['hello', 'thanks', 'yes', 'no']

# Number of images per class
number_imgs = 10

# Image path
IMAGES_PATH = os.path.join(
    'Tensorflow',
    'workspace',
    'images',
    'collectedimages'
)

# Create folders if not exist
for label in labels:
    os.makedirs(os.path.join(IMAGES_PATH, label), exist_ok=True)

# Start collecting images
for label in labels:

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    print(f'\nCollecting images for: {label}')
    print('Starting in 5 seconds...')
    time.sleep(5)

    for imgnum in range(number_imgs):

        ret, frame = cap.read()

        if not ret:
            print("Failed to capture image")
            continue

        # Image filename
        imgname = os.path.join(
            IMAGES_PATH,
            label,
            f'{label}.{uuid.uuid1()}.jpg'
        )

        # Save image
        cv2.imwrite(imgname, frame)

        # Show webcam
        cv2.imshow('Image Collection', frame)

        print(f'Collected image {imgnum + 1}')

        # Wait 1 second
        time.sleep(1)

        # Press q to stop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()

cv2.destroyAllWindows()

print("\nImage collection completed!")