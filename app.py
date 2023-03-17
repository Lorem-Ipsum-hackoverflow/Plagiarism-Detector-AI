from flask import Flask,render_template,request
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app = Flask(__name__)

@app.route('/', methods= ['GET','POST'])
def index(similarpar = 0):
        
        try :
            par1 =  request.form.get('para1')
            par2 = request.form.get('para2')
            
            par1 = str(par1)
            par2 = str(par2)
            
            paras1 = preprocess(par1)
            paras2 = preprocess(par2)
            vectorizer = TfidfVectorizer().fit_transform([paras2,paras1])
        except ValueError:
            return render_template('index.html', similarpar = similarpar, par1=par1 , par2=par2)
        else : 
            
            
            similarity_score = cosine_similarity(vectorizer[0], vectorizer[1])[0][0]
            
            similarpar = int( similarity_score * 100 )
            vectorizer = []
            
            print(similarpar)
            
            
        return render_template('index.html', similarpar = similarpar, par1=par1 , par2=par2) 
        
def preprocess(txt):
    txt = re.sub('\n', ' ', txt)
    txt = re.sub('[^\w\s]', '', txt)
    # Convert to lowercase
    txt = txt.lower()
    return txt



if __name__ == '__main__':
    app.run(debug=True)
