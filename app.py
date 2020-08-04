from flask import Flask
from flask_mongoalchemy import MongoAlchemy
app = Flask(__name__)

app.config['MONGOALCHEMY_DATABASE']='MyDatabase'
app.config['MONGOALCHEMY_CONNECTION_STRING']='mongodb://alalwani:cr6xjy88jt@mycluster-shard-00-00-cfkbg.mongodb.net:27017,mycluster-shard-00-01-cfkbg.mongodb.net:27017,mycluster-shard-00-02-cfkbg.mongodb.net:27017/test?ssl=true&replicaSet=MyCluster-shard-0&authSource=admin&retryWrites=true&w=majority'

db=MongoAlchemy(app)

class Example(db.Document):
    name=db.StringField()
    password=db.StringField()

if __name__=='__main__':
    a=Example(name='aman',password='abc')
    a.save()


