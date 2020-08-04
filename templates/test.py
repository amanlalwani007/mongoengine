'''class Employee():
    def __init__(self,name,last):
        self.name=name
        self.last=last
    @property
    def email(self):
        return "{}.{}".format(self.name,self.last)

    @email.deleter
    def fullname(self,email):
        self.name,self.last=email.split(".")

a=Employee("aman","lalwani")
print(a.name)
print(a.last)
print(a.email)
a.fullname="aman.lalwi"
print(a.email)'''

'''from flask import Flask
from flask_mongoalchemy import MongoAlchemy
app = Flask(__name__)

app.config['MONGOALCHEMY_DATABASE']='MyDatabase'
app.config['MONGOALCHEMY_CONNECTION_STRING']="mongodb://alalwani:cr6xjy88jt@mycluster-shard-00-00-cfkbg.mongodb.net:27017,mycluster-shard-00-01-cfkbg.mongodb.net:27017,mycluster-shard-00-02-cfkbg.mongodb.net:27017/test?ssl=true&replicaSet=MyCluster-shard-0&authSource=admin&retryWrites=true&w=majority"

db=MongoAlchemy(app)

class Example(db.Document):
    name=db.StringField()
    password=db.StringField()

if __name__=='__main__':
    a=Example(name='aman',password='abc')
    a.save()
    a=Example.query.filter(Exampele.name=="aman").first()
    print(a.name)
    a.password=newpassword
    a.remove() #To remove the data from database
   '''

from pymongo import MongoClient
if __name__=='__main__':
    client=MongoClient('mongodb://alalwani:cr6xjy88jt@mycluster-shard-00-00-cfkbgr.mongodb.net:27017,mycluster-shard-00-01-cfkbg.mongodb.net:27017,mycluster-shard-00-02-cfkbg.mongodb.net:27017/test?ssl=true&replicaSet=MyCluster-shard-0&authSource=admin&retryWrites=true&w=majority')
    db=client.gettingStarted#getting Started is database names
    people=db.people #people  is a collection
    persondocument={"name":{"first":"prem","last":"lalwani"},"course":"Btech"}
    #people.insert_one(persondocument)
    print(client.list_database_names())


#why nosql and document db is good
#mongoengine a proper mongodb odm
#SqlAlchemy is the python SQL toolkit and object relational mapper that gives application developer  the  full power and flexibility of SQL
# mongoengine is an object document mapper for pymongo

#mongodb,mongoengine,redis,sqlalchemy,django
#djangoorm or use sqlalchemy(another ORM package use for work with sql databases)
#mongo db stores binary tokenized json(or you can say document)
#with pymongo you have to pass dicionary and get dictionary by query










