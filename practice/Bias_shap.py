import shap
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# Sample phishing emails
emails = [
    "Your account has been compromised. Click here to secure it now!",
    "Reminder: Your company meeting is scheduled for tomorrow at 10 AM.",
    "Update your payment information immediately to avoid suspension!",
]


labels = [1, 0, 1]


vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(emails)


model = LogisticRegression()
model.fit(X, labels)


X_dense = X.toarray()

# SHAP for explainability
explainer = shap.Explainer(model, X_dense)  # Generic explainer
shap_values = explainer(X_dense)

shap.summary_plot(shap_values, X_dense, feature_names=vectorizer.get_feature_names_out())
