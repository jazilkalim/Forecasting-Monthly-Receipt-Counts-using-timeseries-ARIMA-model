import numpy as np

class custom_ARIMA:
    def __init__(self):
        self.theta = None
        self.errors = None

    def fit(self, data, theta_range=np.linspace(-1, 1, 100)):
        # Differencing the data to remove trend
        self.data_diff = np.diff(data, n=1)
        self.original_data = np.array(data)
        
        best_theta = None
        best_sse = float('inf')

        # Grid search for optimal theta
        for theta in theta_range:
            sse = self.calculate_sse(self.data_diff, theta)
            if sse < best_sse:
                best_theta = theta
                best_sse = sse

        self.theta = best_theta
        _, self.errors = self.ma1_model(self.data_diff, self.theta)
        print(f"Fitted Theta (MA(1) coefficient): {self.theta}")
        return self

    def calculate_sse(self, data, theta):
        _, errors = self.ma1_model(data, theta)
        sse = np.sum(errors[1:] ** 2)  # We skip the first value
        return sse

    def ma1_model(self, data, theta):
        forecasts = []
        errors = np.zeros(len(data))  # Initialize residuals (errors)

        for i in range(1, len(data)):
            forecast = theta * errors[i - 1]  # MA(1) only uses the last residual
            errors[i] = data[i] - forecast  # Calculate current error (residual)
            forecasts.append(forecast)

        return forecasts, errors

    def predict(self, steps):
        if self.theta is None:
            raise ValueError("Model must be fitted before making predictions.")
        
        # Start predictions from last differenced value
        last_diff_value = self.data_diff[-1]
        last_error = self.errors[-1]
        future_forecasts = []
        cumulative_forecast = self.original_data[-1]

        for i in range(steps):
            # Predict future differenced values using the last residual (error) and theta
            future_diff_forecast = last_diff_value + (self.theta * last_error)
            cumulative_forecast += future_diff_forecast
            future_forecasts.append(cumulative_forecast)

            last_diff_value = future_diff_forecast
            last_error = np.random.normal(loc=np.mean(self.errors), scale=np.std(self.errors)) * 0.1

        return future_forecasts