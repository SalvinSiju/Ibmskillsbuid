import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

# 1. Load Sample Water Quality Data (you can replace this with your own CSV)
data = {
    'pH': [7.0, 6.5, 8.1, 7.2, 5.4, 9.0],
    'Hardness': [204, 129, 250, 180, 120, 300],
    'Solids': [20791, 18630, 19909, 21320, 15000, 25000],
    'Chloramines': [7.3, 6.6, 9.1, 7.8, 5.9, 9.5],
    'Sulfate': [368, 310, 400, 370, 300, 420],
    'Conductivity': [564, 460, 612, 580, 450, 630],
    'Organic_carbon': [10.2, 9.5, 11.2, 10.7, 8.9, 12.3],
    'Trihalomethanes': [80, 75, 88, 85, 60, 90],
    'Turbidity': [3.0, 3.5, 2.8, 3.2, 4.0, 2.5],
    'Potability': [1, 1, 0, 0, 1, 0]  # 1 = Safe, 0 = Unsafe
}

df = pd.DataFrame(data)

# 2. Prepare Features and Labels
X = df.drop("Potability", axis=1)
y = df["Potability"]

# 3. Split into train and test (not mandatory here, but good practice)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the Model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 5. Save the Model
joblib.dump(model, "ml_model.pkl")

print("✅ Model trained and saved as ml_model.pkl")
