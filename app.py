from flask import *
from train.homepage import Search
from train.reviews import Extract
from train.Sentiment import SentimentAnalysis
app=Flask(__name__)
# search class object  for product
dt=Search()
# Extract class object for reviews extraction
rev=Extract()
# object of sentimentanalysis
SA=SentimentAnalysis()
# path declarations of home page 
@app.route('/')
def login():
    return render_template('login.html')
@app.route('/home')
def Home():
    return render_template('home.html')
#path declarations of details page 
@app.route('/details',methods=['POST'])
def details():
    search_query=request.form['search']
    details=dt.amazon_product(search_query)
    return render_template('details.html',details=details)
#path declarations of review and sentiment page
@app.route('/sentiments',methods=['POST'])
def sentiments():
    buy_link = request.form['buy_link']
    review=rev.review_extract(buy_link)
    sent=[]
    for i in review:
        sent.append(SA.sentiment_analysis(i))
    return render_template('sentiment.html',review=review,sent=sent)
if __name__=="__main__":
    app.run(debug=True)