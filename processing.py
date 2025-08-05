import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)             # Remove special chars
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text) # Remove single chars
    text = re.sub(r'\s+', ' ', text)            # Remove extra spaces
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)
