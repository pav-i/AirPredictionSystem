# AI-Based Air Pollution Detection System

This project presents an advanced system for predicting Air Quality Index (AQI) using machine learning techniques. It leverages diverse data sources, robust algorithms, and visualizations to enhance prediction accuracy and support actionable insights for air quality management.

## Table of Contents
- Abstract
- Features
- Installation
- Usage
- Results
- Technologies Used
- Future Enhancements
- Contributors


## Abstract
The system integrates machine learning models like Random Forest and Long Short-Term Memory (LSTM) networks to forecast AQI based on multi-source data, including satellite imagery, meteorological data, and historical AQI records. It features real-time dashboards to aid decision-making for environmental and public health management.

## Features
- *Accurate AQI Prediction*: Combines Random Forest and LSTM models for enhanced accuracy.
- *Multi-source Data Integration*: Merges structured and unstructured datasets.
- *Real-time Visualizations*: User-friendly dashboards for effective data interpretation.
- *Comparative Analysis*: Evaluates performance against benchmark models.

## Installation
1. *Clone the repository*:
   bash
   git clone <repository-link>
   cd <project-directory>
   
2. *Install dependencies*:
   bash
   pip install -r requirements.txt
   
3. *Prepare data*:
   - Place the AQI datasets in the Data directory.
   - Use dataExtract.py and extractCombine.py to process data.

4. *Run the application*:
   bash
   python app.py
   

## Usage
1. Access the web application via the local server (e.g., http://127.0.0.1:5000/).
2. Input environmental parameters for AQI prediction.
3. View the results categorized as Good, Satisfactory, Alert, or Hazardous.

## Results
- *Model Performance*:
  - *Random Forest*: Accuracy: 92.5%, F1 Score: 91.0%.
  - *LSTM*: Accuracy: 94.2%, F1 Score: 92.9%.
- *Comparison Graphs*: Historical AQI trends and model performance are visualized for better insights.

## Technologies Used
- *Languages*: Python
- *Libraries*: TensorFlow, Scikit-learn, BeautifulSoup, Matplotlib, Flask
- *Tools*: Web scraping (BeautifulSoup), Data visualization (Seaborn)

## Future Enhancements
- Incorporate IoT sensor data and geospatial analytics for improved predictions.
- Develop lightweight models for mobile and low-power devices.
- Extend the application to rural and less-monitored regions.

## Contributors
- PN Pavithra (1MS22CS097)
- Nihareeka Mohanty (1MS22CS090)
