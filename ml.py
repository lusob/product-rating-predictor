from sklearn.feature_extraction.text import CountVectorizer
import logging
import joblib

logging.basicConfig(level=logging.INFO)

class RatingPredictor:
    # Load the token matrix to make the predictions
    model = joblib.load('../data/ppl.pkl')
    def predict(self, product_text):
        # Convert text to tokens
        y_pred = self.model.predict([product_text])
        return y_pred[0]
