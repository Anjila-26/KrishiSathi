# KrishiSathi: Empowering Farmers with Smart Technologies

## Team: The Kripples

### Overview
KrishiSathi is a project developed by a dynamic team of B.Tech students in Artificial Intelligence from Kathmandu University, Nepal. Our goal is to assist Nepalese farmers in optimizing farm management, increasing productivity, and maximizing profitability through the integration of artificial intelligence (AI) technologies.

### Key Features
1. **Personalized Dashboard:** We provide a user-friendly interface for farmers to track their income, expenses, and overall farm performance efficiently.
2. **Crop Price Monitoring:** Farmers can access daily crop prices from local markets and trading centers, aiding in informed decision-making regarding sales and purchases.
3. **Livestock Management:** Our platform includes a module for farmers to input and track information about their livestock, such as breed, age, and health status, facilitating better animal care and management.

### Future Prospects
We aim to further enhance KrishiSathi by developing a Computer Vision Model to automate tasks like animal counting, providing even greater support to farmers in their day-to-day activities.

### Contributors
- Anjila Subedi: Backend Development & AI Enthusiast
- Aagaman Bhattarai: Mobile App Development & NLP Specialist
- Nawap Bastola: AI Expert & API Developer
- Siddhartha Devkota: Frontend Development & NLP Integration Specialist

### Motivation
KrishiSathi is inspired by the need to uplift Nepalese farmers, particularly small and medium-scale ones, who face challenges in optimizing labor, tracking income, and accessing market information. By harnessing the power of AI, we strive to empower farmers and contribute to the growth of Nepal's agricultural sector.


# Animal Sight - Animal Detection System

The Animal Sight - Animal Detection System is a technology-driven solution designed to address the challenges posed by human-animal conflicts in wildlife-rich areas. By leveraging surveillance cameras, machine learning algorithms, and real-time alerting mechanisms, the system aims to detect and mitigate potential conflicts between humans and wildlife, thereby enhancing safety, reducing economic losses, and promoting coexistence.

## Features

### Object Detection
Utilizes machine learning-based object detection algorithms to identify various animal species, including potential intruders, across multiple surveillance cameras.

### Real-time Alerting
Triggers instant alerts via SMS notifications to concerned authorities, farmers, or property owners upon detecting intruding animals, enabling timely intervention to prevent conflicts.

### Centralized Data Management
Stores detection event data, including timestamps, camera IDs, geolocations, and detected classes, in a centralized database for easy access, retrieval, and analysis.

### Scalability and Flexibility
Designed to scale and adapt to different environmental conditions and user requirements, with customizable alert parameters and support for additional cameras and features.

## How to Use

### Installation

1. Clone the repository:

3. Configure Firebase credentials:
- Replace Firebase credentials and database URL with your own values in `YOUR-DB-firebase-adminsdk-......json`.

4. Install Tensorflow 2 Object Detection API:
- Note: Tensorflow<=2.12 version is supported for this.

### Run the Application

1. Set FLASK_APP environment variable:
- Set the FLASK_APP environment variable to the name of your Flask application file (without the .py extension). You can do this in your terminal or command prompt before running `flask run`.
  ```
  set FLASK_APP=your_app_name
  ```

2. Run Flask:
- After setting the FLASK_APP environment variable, try running Flask again:
  ```
  flask run
  ```

- Or without setting up FLASK_APP environment variable, simply run:
  ```
  python app.py
  ```

## Information about ML Model

The ML model used to detect the objects in a video feed is MobileNetV2. The dataset used to train the model was scraped from these sources: Pexels and 123rf.




