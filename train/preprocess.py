import re
import nltk
from nltk.corpus import stopwords

class CleanReview():

    def clean_html(self,text):
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)
    
    def convert_lower(self,text):
        return text.lower()
    
    def remove_special(self,text):
        x = ''
        for i in text:
            if i.isalnum():
                x = x + i
            else:
                x = x + ' '
        return x
    def remove_stopwords(self,text):
        x = []
        for i in text.split():
            if i not in stopwords.words('english'):
                x.append(i)
        y = x[:]
        x.clear()
        return y
    def stem_words(self,text):
        ps=nltk.PorterStemmer()
        y=[]
        for i in text:
            y.append(ps.stem(i))
        z = y[:]
        y.clear()
        return z
    def remove_emojis(self,text):
        # Define the regex pattern for emojis
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   u"\U00002500-\U00002BEF"  # chinese char
                                   u"\U00002702-\U000027B0"
                                   u"\U00002702-\U000027B0"
                                   u"\U000024C2-\U0001F251"
                                   u"\U0001f926-\U0001f937"
                                   u"\U00010000-\U0010ffff"
                                   u"\u2640-\u2642"
                                   u"\u2600-\u2B55"
                                   u"\u200d"
                                   u"\u23cf"
                                   u"\u23e9"
                                   u"\u231a"
                                   u"\ufe0f"  # dingbats
                                   u"\u3030"
                                   "]+", flags=re.UNICODE)

        # Remove emojis from the text
        text_no_emoji = emoji_pattern.sub(r'', text)
        return text_no_emoji
    def join_back(self,list_input):
        return " ".join(list_input)
    
