import pandas as pd
import os

def read_spam():
    category = 'spam'
    directory = './enron1/spam'
    return read_category(category, directory)

def read_ham():
    category = 'ham'
    directory = './enron1/ham'
    return read_category(category, directory)

def read_category(category, directory):
    emails = []
    for filename in os.listdir(directory):
        if not filename.endswith(".txt"):
            continue
        with open(os.path.join(directory, filename), 'r') as fp:
            try:
                content = fp.read()
                emails.append({'name': filename, 'content': content, 'category': category})
            except:
                print(f'skipped {filename}')
    return emails

ham = read_ham()
spam = read_spam()

df = pd.DataFrame.from_records(ham)
df = df.append(pd.DataFrame.from_records(spam))
#Data preprocessing
import re

def preprocessor(e):
    cleaned_text = re.sub('[^a-zA-Z]', ' ', e)
    cleaned_text = cleaned_text.lower()
    return cleaned_text
    pass

#splitting dataset
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

df = pd.DataFrame.from_records(ham)
df = df.append(pd.DataFrame.from_records(spam))

# The CountVectorizer converts a text sample into a vector (think of it as an array of floats).
# Each entry in the vector corresponds to a single word and the value is the number of times the word appeared.
# Instantiating a CountVectorizer. 
vectorizer = CountVectorizer(preprocessor=preprocessor)



# Using train_test_split to split the dataset into a train dataset and a test dataset.
# The machine learning model learns from the train dataset.
# Then the trained model is tested on the test dataset to see if it actually learned anything.
# its done to improve its accuracy on the test dataset and a high accuracy on the train dataset.
X_train, X_test, y_train, y_test = train_test_split(df['content'], df['category'], test_size=0.2, random_state=42)



# Using the vectorizer to transform the existing dataset into a form in which the model can learn from.
X_train_transformed = vectorizer.fit_transform(X_train)
X_test_transformed = vectorizer.transform(X_test)


# Using the LogisticRegression model to fit to the train dataset.
# Here, we fitted a scatter plot to a line.
# Logistic Regression is another form of regression. 
# However, Logistic Regression helps us determine if a point should be in category A or B, which is a perfect fit.
model = LogisticRegression()
model.fit(X_train_transformed, y_train)


# Validating that the model has learned something.
# The model operates on vectors. The test set was transformed first using the vectorizer. 
# Then the predictions was generated.
y_pred = model.predict(X_test_transformed)


# `accuracy_score` tells us how well we have done. 
# 90% means that every 9 of 10 entries from the test dataset were predicted accurately.
# The `confusion_matrix` is a 2x2 matrix that gives us more insight.
# The top left shows us how many ham emails were predicted to be ham (that's good!).
# The bottom right shows us how many spam emails were predicted to be spam (that's good!).
# The other two quadrants tell us the misclassifications.
# Finally, the `classification_report` gives us detailed statistics which you may have seen in a statistics class.

#accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

#confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", conf_matrix)

#classifictaion report
class_report = classification_report(y_test, y_pred)
print("Classification Report:\n", class_report)

# Let's see which features (aka columns) the vectorizer created. 
# They should be all the words that were contained in the training dataset.
features = vectorizer.get_feature_names_out()
print("Features (words):", features)



# looking at coef_[0] which represents the importance of each feature.
# What does importance mean in this context?
# Some words are more important than others for the model.
# It's nothing personal, just that spam emails tend to contain some words more frequently.
# This indicates to the model that having that word would make a new email more likely to be spam.
coefficients = model.coef_[0]


# Iterating over importance and finding the top 10 positive features with the largest magnitude.
# Similarly, finding the top 10 negative features with the largest magnitude.
# Positive features correspond to spam. Negative features correspond to ham.

top_negative_indices = coefficients.argsort()[:10]
top_negative_features = [features[idx] for idx in top_negative_indices]
print("Top 10 negative features (ham-related):", top_negative_features)

# It was seen that `http` is the strongest feature that corresponds to spam emails. 
# It makes sense. Spam emails often want you to click on a link.