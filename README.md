# Forecasting-Monthly-Receipt-Counts-using-timeseries-ARIMA-model

### Key Steps and Approaches

#### Data Exploration and Analysis
* Conduct a thorough examination of the daily receipt data to identify trends, patterns, and anomalies.
* Utilize exploratory data analysis (EDA) techniques to uncover potential features that could be predictive.

#### Data Preprocessing and Transformation
* Convert the data to a stationary series using Box-Cox transformations and differencing to ensure model stability.
* Analyze autocorrelation to determine the optimal lag values for the time series model.

#### Model Development
* Implement a custom ARIMA model incorporating moving average techniques to assess errors and predict future values.
* Tailor the model to accurately forecast monthly receipt counts.

#### Model Deployment and Evaluation
* Predict monthly receipt counts for the next year using appropriate conversion and scaling techniques.
* Develop custom functions to avoid reliance on external libraries.
* Save the trained model in a pickle file for future use.
* Create an interactive user interface using a Flask server to host the model at runtime.
* Package the application in a Docker container for easy deployment and reusability.

**Overall, this project aims to leverage time series forecasting techniques to provide valuable insights into future receipt trends, enabling informed decision-making and resource planning.**


## Directory Structure
* Notebook folder: Python notebook for EDA and creating model
* Flask server : All files needed to run the model prediction web service.
* Docker Image: Docker image to run the project in a docker container
