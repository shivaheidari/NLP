import shap
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Sample phishing emails
emails = [
    "Your account has been compromised. Click here to secure it now!",
    "Reminder: Your company meeting is scheduled for tomorrow at 10 AM.",
    "Update your payment information immediately to avoid suspension!",
]

# Labels (1 = phishing, 0 = legit)
labels = [1, 0, 1]

# Convert text to TF-IDF vectors
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(emails)

# Train a simple phishing detection model
model = LogisticRegression()
model.fit(X, labels)

# Use SHAP for explainability
explainer = shap.LinearExplainer(model, X)  # Works for linear models
shap_values = explainer(X)

# Visualize SHAP explanation
shap.text_plot(shap_values)
