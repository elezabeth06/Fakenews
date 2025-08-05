from model import train_model
from predict import predict_news

if __name__ == "__main__":
    print("Training model...")
    train_model()
    print("\nModel trained successfully.\n")

    while True:
        news = input("Enter news to classify (or type 'exit'): ")
        if news.lower() == 'exit':
            break
        print("Prediction:", predict_news(news))
