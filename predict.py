import pandas as pd
from prophet import Prophet

# Load the data
df = pd.read_csv("/home/asus/Projects/prediction_prophet/fake_data_table.csv")
print("Dataframe-")
print(df[['Date', 'Clothing']].head(30))

# Select and rename the columns for Prophet
clothing_df = df[["Date", "Clothing"]].rename(columns={"Date": "ds", "Clothing": "y"})

# Initialize and fit the Prophet model
m = Prophet()
m.fit(clothing_df)

# Create a dataframe for future predictions
future = m.make_future_dataframe(periods=180)
print("Future dataframe-")
print(future.tail())

# Make predictions
forecast = m.predict(future)
print("Prediction-")
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(182))

# Save the 'ds' and 'yhat' columns to a CSV file
output_csv_path = "/home/asus/Projects/prediction_prophet/forecast_output.csv"
forecast[['ds', 'yhat']].to_csv(output_csv_path, index=False)
print(f"Forecast saved to {output_csv_path}")
