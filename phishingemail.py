import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset
df = pd.read_csv(
    r"C:\Users\Madhi\OneDrive\Desktop\madhi\phishing_email\Phishing_Email.csv"
)

# Remove empty rows
df = df.dropna()

# Features
X = df['Email Text']

# Labels
y = df['Email Type']

# Convert labels to numbers
y = y.map({
    'Safe Email': 0,
    'Phishing Email': 1
})

# Convert text into numerical features
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("\n===== PHISHING EMAIL DETECTION MODEL =====")
print(f"\nAccuracy: {accuracy:.2%}")

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

# Test custom email
print("\n===== EMAIL CHECKER =====")

email = input("\nPaste an email:\n\n")

email_vector = vectorizer.transform([email])

prediction = model.predict(email_vector)

if prediction[0] == 1:
    print("\n⚠️ Result: PHISHING EMAIL DETECTED")
else:
    print("\n✅ Result: SAFE EMAIL")