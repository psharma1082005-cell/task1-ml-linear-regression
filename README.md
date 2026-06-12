# TASK 1: HOUSE PRICE PREDICTION USING LINEAR REGRESSION

## Internship Project Report

**Submitted By**

**Name: Prachi Sharma**

---

## Objective

The objective of this project is to develop a Machine Learning model capable of predicting house prices using the California Housing Dataset. Linear Regression was selected as the predictive algorithm because it is one of the most fundamental and widely used supervised learning techniques for regression problems.

---

## Introduction

Machine Learning enables computers to learn patterns from data and make predictions without being explicitly programmed. In this project, a Linear Regression model was implemented to estimate housing prices based on several features such as median income, house age, number of rooms, population, latitude, and longitude.

The California Housing Dataset is a popular benchmark dataset used for regression tasks and provides valuable insights into housing market trends.

---

## Dataset Description

The California Housing Dataset contains information collected from housing districts in California.

### Features Used

- **MedInc** (Median Income)
- **HouseAge**
- **AveRooms**
- **AveBedrms**
- **Population**
- **AveOccup**
- **Latitude**
- **Longitude**

### Target Variable

- **MedHouseVal** (Median House Value)

---

## Exploratory Data Analysis (EDA)

Before building the model, the dataset was explored to understand its structure and characteristics.

### EDA Steps Performed

1. Loaded dataset using Scikit-Learn.
2. Displayed first few records using `head()`.
3. Checked dataset information using `info()`.
4. Generated statistical summary using `describe()`.
5. Verified missing values.
6. Visualized relationships between actual and predicted values.

### Dataset Sample (First 5 Records)

```
   MedInc  HouseAge  AveRooms  AveBedrms  Population  AveOccup  Latitude  Longitude  MedHouseVal  
0  8.3252      41.0  6.984127   1.023810       322.0  2.555556     37.88    -122.23        4.526  
1  8.3014      21.0  6.238137   0.971880      2401.0  2.109842     37.86    -122.22        3.585  
2  7.2574      52.0  8.288136   1.073446       496.0  2.802260     37.85    -122.24        3.521  
3  5.6431      52.0  5.817352   1.073059       558.0  2.547945     37.85    -122.25        3.413 
4  3.8462      52.0  6.281853   1.081081       565.0  2.181467     37.85    -122.25        3.422  
```

### Observations

- Dataset contained numerical features only.
- No major missing value issues were observed.
- Features showed meaningful relationships with house prices.

---

## Model Development

### Algorithm Used

**Linear Regression**

Linear Regression establishes a relationship between independent variables and the target variable by fitting a straight-line equation to observed data.

### Steps Followed

1. Import required libraries (NumPy, Pandas, Scikit-Learn, Matplotlib).
2. Load California Housing Dataset.
3. Separate features and target variable.
4. Split data into training and testing datasets (80-20 split).
5. Train Linear Regression model.
6. Predict house prices on testing data.
7. Evaluate model performance.

---

## Model Evaluation

The following evaluation metrics were used:

### Mean Absolute Error (MAE)

Measures the average magnitude of prediction errors.

### Root Mean Squared Error (RMSE)

Measures the standard deviation of prediction errors and penalizes larger errors.

### R² Score

Indicates how well the model explains the variance in the target variable.

---

## Results ✅

The Linear Regression model was successfully trained and tested on the California Housing Dataset.

### Model Performance Metrics:

```
MAE (Mean Absolute Error)   = 0.5332
RMSE (Root Mean Squared Error) = 0.7456
R² Score                    = 0.5758
```

### Detailed Output:

**Mean Absolute Error (MAE):** 0.5332001304956553
- On average, predictions are off by ~$53,320 (since target is in $100,000s)

**Root Mean Squared Error (RMSE):** 0.7455813830127764
- Standard deviation of errors is ~$74,558

**R² Score:** 0.5757877060324508
- The model explains ~57.58% of the variance in house prices

### Interpretation

The generated predictions showed a meaningful correlation with actual house prices. With an R² Score of 0.576, the model performs reasonably well as a baseline regression model for housing price prediction. The MAE of 0.533 indicates moderate prediction accuracy.

---

## Visualization

### Scatter Plot: Actual vs Predicted House Prices

A scatter plot was generated showing the relationship between actual and predicted house prices. The plot demonstrates:

- Each point represents a housing sample
- A positive trend indicates that predicted values follow actual values reasonably well
- The clustering pattern shows the model successfully learned patterns from the dataset
- Some outliers are visible, suggesting room for improvement through advanced algorithms

---

## Future Improvements

The performance of the model can be enhanced using:

- **Random Forest Regressor** - Reduces overfitting through ensemble methods
- **Decision Tree Regressor** - Captures non-linear relationships
- **Gradient Boosting** - Sequential improvement of predictions
- **XGBoost** - Powerful gradient boosting implementation
- **Hyperparameter Tuning** - Optimize model parameters
- **Feature Engineering** - Create new meaningful features
- **Polynomial Regression** - Model non-linear relationships

---

## Conclusion

This project successfully demonstrated the implementation of a Linear Regression model for predicting housing prices. The model was trained, evaluated, and visualized using Python and Scikit-Learn. The project provided practical exposure to:

- Data preprocessing and exploration
- Model training and testing
- Evaluation metrics and performance assessment
- Data visualization and interpretation
- Predictive analytics

Overall, the project highlights the effectiveness of Machine Learning techniques in solving real-world prediction problems and serves as a strong foundation for advanced regression models.

---

## Project Summary

| Metric | Value |
|--------|-------|
| **Dataset** | California Housing Dataset |
| **Algorithm** | Linear Regression |
| **Training-Test Split** | 80-20 |
| **Number of Features** | 8 |
| **MAE** | 0.5332 |
| **RMSE** | 0.7456 |
| **R² Score** | 0.5758 |
| **Status** | ✅ Complete |
| **Date Submitted** | 2026-06-12 |

**Libraries Used:** NumPy, Pandas, Scikit-Learn, Matplotlib

---

**All files have been successfully uploaded to the repository!** 🚀
