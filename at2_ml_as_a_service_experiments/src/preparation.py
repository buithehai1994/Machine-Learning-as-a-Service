import pandas as pd
from lightgbm import LGBMRegressor  # Import LGBMRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import altair as alt
import gc  # For garbage collection
import pickle  # Import pickle for saving models
from sklearn.preprocessing import StandardScaler

class PredictiveModel:
    def __init__(self):
        # Initialize the LGBMRegressor with specific parameters
        self.model = LGBMRegressor(max_depth=12, min_data_in_leaf=20, min_child_samples=16,n_estimators=1000)  # Use relevant LGBM parameters
        self.scaler = StandardScaler()

    def scale_features(self, X):
        """Scale features using StandardScaler."""
        return self.scaler.fit_transform(X)  # Fit and transform training data

    def train(self, X, y,epochs=1):
        """Train the model using the provided features and target."""
        # Fit the model without scaling
        
        for epoch in tqdm(range(epochs), desc="Training Epochs"):
            self.model.fit(X, y)  # Refit for demonstration, typically you'd fit once
            
        return self.model
        
    def predict(self, X):
        """Make predictions on the given features."""
        return self.model.predict(X)  # Expecting scaled input

    def evaluate(self, y_true, y_pred):
        """Calculate MSE and MAE as evaluation metrics."""
        mse = mean_squared_error(y_true, y_pred)
        mae = mean_absolute_error(y_true, y_pred)
        return mse, mae

    def create_prediction_df(self, y_true, y_pred):
        """Create a DataFrame for predictions."""
        return pd.DataFrame({
            'index': range(len(y_true)),
            'actual': y_true.values.flatten(),
            'predicted': y_pred.flatten()
        })

    def visualize_predictions(self, prediction_df, sample_size=500):
        """Visualize actual vs predicted values."""
        train_downsampled = prediction_df.sample(n=min(sample_size, len(prediction_df)), random_state=42)

        scatter = alt.Chart(train_downsampled).mark_circle(size=60, opacity=0.7).encode(
            x=alt.X('actual:Q', title='Actual Values'),
            y=alt.Y('predicted:Q', title='Predicted Values'),
            tooltip=['index', 'actual', 'predicted']
        ).properties(
            title='Actual vs. Predicted Values'
        )

        line = alt.Chart(train_downsampled).mark_line(color='red').encode(
            x='actual:Q',
            y='actual:Q'
        )

        scatter_plot = scatter + line
        return scatter_plot

    def save_model(self, file_path):
        """Save the trained model and scaler to a file using pickle."""
        try:
            with open(file_path, 'wb') as f:
                pickle.dump((self.model, self.scaler), f)  # Save both model and scaler
        except Exception as e:
            print(f"Error saving model: {e}")

    def load_model(self, file_path):
        """Load a previously saved model using pickle."""
        try:
            with open(file_path, 'rb') as f:
                self.model, self.scaler = pickle.load(f)  # Load both model and scaler
        except Exception as e:
            print(f"Error loading model: {e}")
            
    def save_scaler(self, file_path):
        """Save the scaler to a file."""
        try:
            with open(file_path, 'wb') as f:
                pickle.dump(self.scaler, f)  # Save the scaler
            print("Scaler saved successfully.")
        except Exception as e:
            print(f"Error saving scaler: {e}")

    def clean_up(self):
        """Perform garbage collection to free up memory."""
        gc.collect()
