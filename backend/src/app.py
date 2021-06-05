from flask import Flask, redirect, url_for, request
from flask import jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

from googleAPI import send_GG_API

import test

app = Flask(__name__)
cors = CORS(app)

@app.route('/',methods = ['POST', 'GET'])
def hello_worldd():
   if request.method == 'GET':
      return jsonify(test.test("./data/"))
   if request.method == 'POST':
      print(request.files['voice_file'])
      f = request.files['voice_file']
      f.save(secure_filename(f.filename))
      name = f.filename
      return send_GG_API(name)

      
if __name__ == '__main__':
   app.run(debug= True, host="0.0.0.0", port=80)