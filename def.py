from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def fun():
    return render_template('index.html')

@app.route('/form', methods=['GET'])
def form_d():
    return 'Data received'

@app.route('/form_data', methods=['GET'])
def form_1():
    var = request.form
    print(var)
    
    return var
if __name__=='__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)






