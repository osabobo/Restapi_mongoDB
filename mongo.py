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

#you can create your Api from here by edit this code
@app.route('/add', methods=['POST'])
def add_mytable():
    _json=request.json
    Name_of_song=_json['Name_of_song']
    #Name_of_the_podcast=_json['Name_of_the_podcast']
    #Host=_json['Host']
    #Participants=_json['Participants']
    #Title_of_the_audiobook=_json['Title_of_the_audiobook']
    #Author_of_the_title=_json['Author_of_the_title']
    #Narrator=_json['Narrator']
    Duration_in_number_of_seconds=_json['Duration_in_number_of_seconds']
    Upload_time=_json['Upload_time']
    if Name_of_song and  Duration_in_number_of_seconds and Upload_time and request.method == 'POST':
        id=mongo.db.mytable.insert({"Name_of_song":Name_of_song,"Duration_in_number_of_seconds": Duration_in_number_of_seconds,"Upload_time":Upload_time})
        response=jsonify('user added sucessfully')
        response.status_code=200
        return response
    else:
        return not found
#To delet your infotrmation from database
@app.route('/mytable/<id>', methods=['DELETE'])
def delete_mytable(id):
    mytable = mongo.db.mytable
    new_mytable = mytable.delete_one({'_id':objectId(id)})
    return 'None', 200
#To update the existing data
@app.route('/update/<id>', methods=['PUT'])
def update_mytable(id):
    _id=id
    _json=request.json
    Name_of_song=_json['Name_of_song']
    #Name_of_the_podcast=_json['Name_of_the_podcast']
    #Host=_json['Host']
    #Participants=_json['Participants']
    #Title_of_the_audiobook=_json['Title_of_the_audiobook']
    #Author_of_the_title=_json['Author_of_the_title']
    #Narrator=_json['Narrator']
    Duration_in_number_of_seconds=_json['Duration_in_number_of_seconds']
    Upload_time=_json['Upload_time']
    if Name_of_song and  Duration_in_number_of_seconds and Upload_time and request.method == 'PUT':
        mongo.db.mytable.update({'_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},{'$set':{'Name_of_song':Name_of_song,'Duration_in_number_of_seconds':Duration_in_number_of_seconds,'Upload_time':Upload_time}})
        resp=jsonify('user updated sucessfully')
        resp.status_code=200
        return resp


#To get data from your database
@app.route('/mytable', methods=['GET'])
def get_all_mytable():
    mytable = mongo.db.mytable.find()
    mytable= dumps(mytable)
    return mytable

@app.route('/mytable/<id>')
def get_one_table():
    mytable = mongo.db.mytable.find_one({'_id':objectId(id)})
    mytable= dumps(mytable)
    return mytable
@app.errorhandler(404)
def not_found(error=None):
    message={
         'status':404,
         'message':'Not found' + request.url
    }
    resp=jsonify(message)
    resp.status_code=404
    return resp
if __name__ == '__main__':
    app.run(debug=True)
