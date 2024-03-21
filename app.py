from flask import *
from train.homepage import home
from train.searchpage import Search
app=Flask(__name__)
# home details
hm=home()
flipkart_df=hm.snapdeal()
# creating of objects of search page
dt=Search()

# path declarations
@app.route('/')
def Home():
    flipkart=flipkart_df['url']
    url=flipkart_df['link']
    return render_template('home.html',flipImage=flipkart,flipurl=url)
@app.route('/login')
def Login():
    pass
@app.route('/register')
def Register():
    pass
@app.route('/logout')
def logout():
    pass
@app.route('/details')
def details():
    index=request.args.get('flipdeat')
    return render_template('details.html')
@app.route('/sentiments')
def sentiments():
    pass

if __name__=="__main__":
    app.run(debug=True)