# Swiggy-Restaurant-Recommendation-System-using-Streamlit
Restaurant recommendation system based on restaurant data provided in a CSV file. The system would recommend restaurants to users based on input features such as city, rating, cost, and cuisine preferences.

# Restaurant Recommendation System

## Overview
This **restaurant recommendation system** suggests restaurants baed on user preferances. It uses **cosine similarity** to find relevant restaurants based on features such as **city, cuisine, rating and cost**. The system will display results in Streamlit interface for an easy-to-use user experience.

## Features
- **Data Preprocessing:** Cleans and analyze restaurant data.
- **Encoding:** Applies **One-Hot Encoding** to categorical features **city, cuisine**.
- **Cosine Similarity Measures:** Uses **Cosine Similarity** to identify similar restaurants.
- **Result Mapping:** Maps recommendation results back to the original dataset.
- **Streamlit Application:** Provides an **interactive web interface** for users to get personalized restaurant recommendations.

## Dataset
The dataset consists of restaurant details, including:
- **Name**
- **City**
- **Cuisine**
- **Rating**
- **Rating Count**
- **Cost**

## Project Workflow
### 1. Data Preprocessing
- Removed duplicate entries.
- Handled missing values.
- Converted categorical columns to one hot encoding.
- Transformed cost and rating features into numeric values.

### 2. Encoding
- Applied **One-Hot Encoding** to categorical features (e.g., city, cuisine).
- Saved the encoder as a **Pickle file (`encoder.pkl`)**.
- Ensured all features are numerical after encoding.
- Created a preprocessed dataset (`encoded_data.csv`).
- Matched the indices of `cleaned_data.csv` and `encoded_data.csv`.

### 3. Recommendation Methodology
- Implemented **Cosine Similarity** to recommend restaurants.
- Used encoded numerical data for computations.

### 4. Result Mapping
- Mapped the recommendation results (indices) back to the **non-encoded dataset (`cleaned_data.csv`)**.

### 5. Streamlit Application
Built an **interactive web application** that:
- **Accepts user input** (e.g., preferred city, cuisine, rating, price range).
- **Processes the input** and calculated coisine similarity on the encoded dataset for recommendations.
- **Displays recommended restaurants** using `cleaned_data.csv`.

## Installation
### Prerequisites
Ensure you have **Python 3.7+** and install the required dependencies:
```sh
pip install pandas numpy scikit-learn streamlit 
```

## Running the Application
Run the Streamlit app using:
```sh
streamlit run app.py
```






