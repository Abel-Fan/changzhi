from flask import Flask,render_template,jsonify
import pickle

app = Flask(__name__)

with open("datas.txt",'rb') as f:
    datas = pickle.load(f)


# 路由
@app.route("/",methods=['GET'])  # get post
def index():
    return render_template('index.html')

@app.route('/getData/<start>',methods=['GET'])
def getData(start):
    start = int(start)
    res = datas[start:start+10]
    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)
