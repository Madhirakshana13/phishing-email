# Phishing Email Detection Model

*Overview*
This project uses Machine Learning and Scikit-Learn to classify emails as Phishing or Safe.

*Features*
- Email classification
- TF-IDF feature extraction
- Naive Bayes classifier
- Accuracy calculation
- Confusion matrix generation
- Custom email testing

*Technologies Used*
- Python
- Pandas
- Scikit-Learn
- NumPy

*Dataset*

The dataset used for this project can be downloaded from Kaggle:
https://www.kaggle.com/datasets/subhajournal/phishingemails

-The dataset is not included in this repository because of GitHub file size limitations.
-Download it separately and place it in the project folder before running the code.

*Results*

- Accuracy: 91.49%
- Successfully detects phishing emails
- Successfully identifies legitimate emails

##Example

Phishing Email:
"URGENT! Your bank account has been suspended. Click here immediately to verify your password."

Output:
PHISHING EMAIL DETECTED

Safe Email:
"Hello Team, the project review meeting is scheduled for tomorrow at 10 AM."

Output:
SAFE EMAIL
