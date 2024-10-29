# Rent Price Prediction

This project aims to predict rental prices of residential properties in Pune using various machine learning models. The dataset is scraped from Makaan.com and processed to build predictive models.

## Dataset Automation Script

### dataset_automation.py

This script uses Selenium to scrape data from Makaan.com and stores it in a CSV file.

#### Prerequisites

- Python 3.x
- Selenium
- Pandas
- ChromeDriver

#### Instructions

1. Install the required libraries:
   ```bash
   pip install selenium pandas
   ```

2. Download ChromeDriver and place it in your desired location.

3. Update the `webdriver.Chrome()` path in the script to the location of your ChromeDriver.

4. Run the script:
   ```bash
   python dataset_automation.py
   ```

5. The script will create a `scraped_data.csv` file containing the scraped data.

## Rent Price Prediction Notebook

### rent-price-prediction.ipynb

This Jupyter Notebook processes the scraped data and builds various machine learning models to predict rental prices.

#### Prerequisites

- Python 3.x
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

#### Instructions

1. Install the required libraries:
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn
   ```

2. Open the notebook:
   ```bash
   jupyter notebook rent-price-prediction.ipynb
   ```

3. Run the notebook cells to process the data, build models, and evaluate their performance.

## Data Description

The dataset contains the following columns:

- **title**: The title of the property listing.
- **price**: The rental price of the property.
- **area**: The area of the property in square feet.
- **location**: The location of the property in Pune.
- **status**: The furnishing status of the property (Furnished, Semi-Furnished, Unfurnished).
- **bedroom**: The number of bedrooms in the property (extracted from the title).

## Model Evaluation

The notebook evaluates the following machine learning models:

- Linear Regression
- Lasso Regression
- Ridge Regression
- K-Nearest Neighbors Regressor
- Support Vector Regressor
- AdaBoost Regressor
- Decision Tree Regressor
- Random Forest Regressor

The models are evaluated using the following metrics:

- R2 score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

## Visualization

The notebook includes visualizations for:

- Distribution of rental prices
- Scatter plots for rent vs. number of bedrooms
- Scatter plots for area vs. number of bedrooms
- Box plot of rental prices
- Kernel density plot of rental prices

## Notes

- Ensure that the dataset (`rent.csv`) is placed in the correct location specified in the notebook.
- The code snippets and visualizations are based on the data scraped from Makaan.com and may vary if the website's structure changes.
