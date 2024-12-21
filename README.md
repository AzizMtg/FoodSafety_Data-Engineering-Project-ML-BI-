# SAFE: Revolutionizing Food Safety Management

## Overview
The SAFE project addresses key challenges in food safety management by leveraging data engineering and machine learning. It integrates predictive analytics and interactive dashboards to empower stakeholders—customers, restaurant owners, and health inspectors—with actionable insights.

## Features
- **Intuitive Platform**: A user-friendly interface consolidates essential food safety data.
- **Interactive Dashboards**:
  - Tailored KPIs and insights for clients, inspectors, and restaurant owners.
  - Machine learning models for predictive analytics.
- **Machine Learning Integration**:
  - Sentiment analysis for customer feedback.
  - Classification models for risk and grade predictions.
  - Clustering models to identify high-risk facilities.
  - Regression models for revenue prediction.
- **Real-Time Deployment**:
  - Seamless integration with Power BI and Django-based web applications.
  - Role-based access for personalized user experiences.

## Data Engineering Process
1. **ETL Process**: Data cleaning, transformation, and loading using SSIS.
2. **Data Warehouse Design**: Dimensional modeling with fact tables (inspection, reviews, revenue) and shared dimensions (facility, time, geography, etc.).
3. **Interactive Dashboards**:
   - Power BI dashboards for different user roles.
   - Python visualizations for dynamic model predictions.

## Machine Learning Models
1. **Natural Language Processing**: Sentiment analysis of customer reviews using SVC.
2. **Risk Prediction**: SVM for classifying facilities as "Safe" or "At Risk."
3. **Grade Prediction**: KNN for predicting restaurant grades based on inspection and environmental data.
4. **Clustering**: K-Means for grouping facilities based on performance and risk factors.
5. **Revenue Prediction**: Gradient Boosting Regressor for financial insights.

## Deployment
- Machine learning models saved as `.pkl` files for integration with Power BI and Django.
- Website with ML models and PowerBI Dashboards Integrated
- Role-specific dashboards with real-time predictions and analytics.

## Future Plans
- Expand datasets to include more states and granular inspection data.
- Optimize machine learning models using advanced algorithms.
- Refine the user interface for a seamless experience.
- Real-world deployment with partnerships in the restaurant industry.

## Team
Developed by Team InfoFlow, guided by Professors Nardine Hanfi and Mariem Glaa.

## References
- Datasets from Kaggle.
- FDA Food Code standards.
- Academic references for data preprocessing and machine learning techniques.
