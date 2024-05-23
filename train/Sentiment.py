from train.preprocess import CleanReview
import pickle
cr=CleanReview()
class SentimentAnalysis():
    def sentiment_analysis(self,review):
        text=cr.clean_html(review)
        text=cr.convert_lower(text)
        text=cr.remove_special(text)
        text=cr.remove_emojis(text)
        text=text.replace('readmore','')
        text=cr.stem_words(text)
        text=cr.join_back(text)
        with open('train/Sentiments.pkl', 'rb') as file:
            model = pickle.load(file)
        number=model.predict([text])
        return number