# Aria Meta Glasses-Object Recognition in daily life
   ![Aria Glasses](https://github.com/SalahElshafey/RGU-Aria-Meta-Glasses-Object-Recognition-in-Daily-Life/blob/main/Readme%20images/1.jpg?raw=true)
## Overview

The Aria Meta Glasses project aims to develop an advanced wearable technology designed to assist users, such as students, in seamlessly identifying objects within their environment. By leveraging sophisticated machine perception algorithms, the glasses can detect and recognize objects, such as a laptop, without the need for the user to interact with them physically. The recognition information is relayed through a connected device, providing the user with immediate contextual awareness. Additionally, the glasses are equipped with embedded sensors that offer real-time navigation, enhancing the user’s situational awareness. This project represents a significant step forward in integrating augmented reality and sensor technologies to create intuitive and practical applications for everyday use.

## Table of Contents
1. Aims and Objectives
2. Project Progress
3. Hardware
4. Software
5. Known Issues
6. Future Enhancements
7. Contact Information

## Aims and Objectives
* **Aim:** To develop a wearable device that enhances user interaction by providing real-time object recognition and contextual data such as navigation and weather.

* **Objectives:**
   - Implement machine perception algorithms for object recognition.
   - Integrate sensors (IMU, barometer) for environmental data.
   - Develop a real-time data processing framework.
   - Ensure seamless wireless connectivity with external devices.
![detection](https://github.com/SalahElshafey/RGU-Aria-Meta-Glasses-Object-Recognition-in-Daily-Life/blob/main/Readme%20images/2.jpg?raw=true)

## Project Progress
* App Installation:

   - Download iOS or Android apps for connecting with the glasses.
   ![aria installation](https://github.com/SalahElshafey/RGU-Aria-Meta-Glasses-Object-Recognition-in-Daily-Life/blob/main/Readme%20images/3.png?raw=true)
   - Install the Desktop Companion App to manage .vrs files and view recorded videos.
* Recording & Dataset Preparation:
 

    - Successfully recorded videos around the RGU campus using the glasses.
    - Annotated and prepared datasets using Roboflow, starting with **269** images and expanding to **822** images.

    - dataset link:
    ``` https://liverguac-my.sharepoint.com/:f:/g/personal/s_elshafey_rgu_ac_uk/Eke8asSkZwJIm8RdG9Cpd6gBgeCvZ0ecC2ZTf6TrIr0xig?e=tQbnYX ```

* Object Recognition & Code Development:

  - Developed object recognition models using YOLOv8n.

For yolov8n package installation check:
``` https://github.com/ultralytics/ultralytics ```
  - Initial code was deployed using the COCO dataset, followed by integration with the Aria Glasses dataset.
* Live Streaming:
  - Successfully implemented YOLOv8n model for live streaming using both USB and Wi-Fi.

## Hardware
- **Mono Scene Cameras:** Two cameras for visual tasks like Visual SLAM.
- **POV RGB Camera:** Forward-facing high-resolution camera.
- **Eye-Tracking Cameras:** Two inward-facing cameras for tracking gaze.
- **IMUs:** For tracking motion and orientation.
- **Microphone Array:** For spatial audio capture.
- **Magnetometer, Barometer, Thermometer:** For environmental awareness.
- **GNSS Receiver:** Provides geographic positioning.
- **Wi-Fi & Bluetooth Transceiver:** For wireless connectivity.

## Software
- **YOLOv8:** For real-time object detection.
- **COCO Pre-trained Dataset:** For initial training.
- **Roboflow:** For dataset annotation and preparation.

## Known Issues
- **Wi-Fi Streaming:** The stream opens but does not catch frames.
- **USB Streaming:** Works but prioritizes Wi-Fi even if the Wi-Fi is off.

## Future Enhancements
- **3D Detection:** Transition from 2D object detection to 3D.
- **Live Sensor Data:** Utilize live sensor data once Wi-Fi streaming is stabilized.

## RGU Report link
![RGU Report](https://github.com/SalahElshafey/RGU-Aria-Meta-Glasses-Object-Recognition-in-Daily-Life/blob/main/Readme%20images/3.png?raw=true)
## Contact Information
For more details or inquiries, please contact:
- Salah Elshafey
linkedin : https://www.linkedin.com/in/salah-elshafey-3550461a1/









