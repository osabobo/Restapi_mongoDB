from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'test-database-1'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test-database-1'

mongo = PyMongo(app)


@app.route('/mytable', methods=['GET'])
def get_all_mytable():
    mytable = mongo.db.mytable.find()
    mytable= dumps(mytable)
    return mytable

if __name__ == '__main__':
    app.run(debug=True)
