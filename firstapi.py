from flask import Flask, render_template, flash, request, url_for, redirect, jsonify
app = Flask(__name__)

@app.route('/newdata', methods=['POST'])
def newData():
    newData = request.get_json()
    if newData != None:
        return ('Data Received'), 200
    else:
        return ('Data Not Received')

@app.route('/addData', methods=['POST'])
def addData():
    addData = request.get_json()
    if len(addData) >= 1:
        return ('Data Received'), 200
    else:
        return ('Data Not Received')
if __name__ == '__main__':
    app.run(debug=True)
