# Multilingual Chatbot Analytics Pipeline

## Project Overview
This project is an end-to-end data analytics pipeline that analyzes customer interactions with a multilingual support chatbot. The goal of this project is to showcase the complete data lifecycle: from generating synthetic data using AI, to cleaning and validating the dataset using Python and Pandas, and finally extracting business insights through an interactive Tableau dashboard.

## 📊 Dashboard Preview
*(Note: The interactive dashboard was built in Tableau. Below is a static snapshot of the final visualization.)*

![Tableau Dashboard](Screenshot%201948-05-13%20at%201.56.17%20PM.png)

## 🛠️ Tools & Technologies Used
* **Python:** Used for API interaction, data generation, and statistical summaries.
* **Pandas:** Used for data cleaning, type formatting (datetime parsing), checking for null values, and Exploratory Data Analysis (EDA).
* **Jupyter Notebook:** Used as the primary environment for data validation and cross-analysis.
* **Tableau:** Used to design the final business intelligence dashboard and visualize key performance indicators (KPIs).
* **Large Language Models (LLMs):** Used to programmatically generate highly realistic, 1,000-row synthetic conversational data.

## 📂 Repository Files
* `chatbot_data.csv`: The raw dataset containing 1,000 unique customer interactions, including metrics like intent, duration, and sentiment.
* `chatbot analyzed data.ipynb`: The Jupyter Notebook containing the data extraction checks, Pandas data type conversions, and initial Exploratory Data Analysis.
* `chatbot interactions.py`: The Python script showcasing how the synthetic data was engineered and generated via AI.
* `Screenshot 1948-05-13 at 1.56.17 PM.png`: Visual proof of the Tableau analytics.

## 📈 Key Workflow Steps
1. **Data Engineering:** Engineered a dataset of simulated customer interactions (Customer_ID, Intent, Chat_Duration, Sentiment, Resolution_Status).
2. **Data Validation:** Imported the raw CSV into a Jupyter Notebook to verify data integrity. Handled data typing for time-series analysis and ensured a clean, 0-null dataset.
3. **Exploratory Data Analysis (EDA):** Grouped categorical variables and analyzed statistical distributions of chat durations to understand the baseline metrics before visualization.
4. **Visual Analytics:** Connected the cleaned CSV to Tableau to build out intuitive, user-friendly charts that non-technical stakeholders can use to gauge chatbot performance and customer satisfaction.
