# mongo1.py

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

# data base name : 'test-database-1'
mydb = client['test-database-1']

import datetime

myrecord = [{
"Name_of_song":"Hey Jude",
"Duration_in_number_of_seconds": 10,
"Upload_time":datetime.datetime.utcnow()

},

{
"Name_of_the_podcast":"99% Invisible, The Moth",
"Duration_in_number_of_seconds":7,
"Upload_time":datetime.datetime.utcnow(),
"Host":"Apple podcast",
"Participants":["john","Andrew","Akin","osagie","Agnes","Timi","Peter","Tolu","kingsley","David"]
},
{
"Title_of_the_audiobook":"The Wrong Family",
"Author_of_the_title":"Tarryn Fisher",
"Narrator":"Andrew",
"Duration_in_number_of_seconds":8,
"Upload_time":datetime.datetime.utcnow()
}
]

record_id = mydb.mytable.insert_many(myrecord)

print(record_id)
print(mydb.list_collection_names())
