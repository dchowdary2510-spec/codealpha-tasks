# Object Detection and Tracking System

A real-time Object Detection and Tracking application built using Python, Streamlit, OpenCV, and YOLO. The system can detect and track objects from images, videos, and webcam feeds while maintaining a detection history log.

## Features

- Real-time object detection using YOLO
- Object tracking across video frames
- Webcam live detection support
- Video file upload and processing
- Detection history logging
- Object count monitoring
- Custom class filtering
- Interactive Streamlit dashboard

## Technologies Used

- Python
- Streamlit
- OpenCV
- Ultralytics YOLO
- Pandas
- NumPy

## Project Structure

Object_Detection_Tracking/
│
├── app.py
├── detector.py
├── detection_history.csv
├── requirements.txt
├── .gitignore
└── README.md

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Object_Detection_Tracking
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

## How It Works

1. Upload an image or video, or start webcam detection.
2. The YOLO model processes each frame.
3. Objects are detected and tracked in real time.
4. Detection details are displayed on the dashboard.
5. Detection history is automatically saved to a CSV file.

## Supported Detection Classes

Examples include:

- Person
- Cell Phone
- Book
- Mouse
- Earbuds
- And other classes supported by the YOLO model

## Application Features

### Image Detection
Detect objects from uploaded images.

### Video Detection
Process uploaded videos frame by frame.

### Webcam Detection
Perform live object detection using a webcam.

### Detection History
Store detection records in a CSV file for analysis.

### Class Filtering
Select specific object classes to detect and track.

## Sample Use Cases

- Smart surveillance systems
- Traffic monitoring
- Retail analytics
- Classroom monitoring
- Object counting applications
- Security and safety systems

## Future Enhancements

- Face recognition
- Email/SMS alerts
- Cloud database integration
- Advanced object analytics
- Mobile application support

## Output

The system displays:

- Detected object labels
- Confidence scores
- Bounding boxes
- Object counts
- Detection history records

## Author

Developed as part of the CodeAlpha Internship Program.