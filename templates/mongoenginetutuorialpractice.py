#mongo db is based on bson documents
#bson is compressed extended form of json
#role of ongoengine is to create a structure that
#is not present in mongodb
#it is more efficient for those system where there
#are more reads than writes
'''
mongodb     |  python
object      |  dictionary
field       |    key
#requied=True is that we need that field
#default value is when the value does not pass
#choices are used when you want to define that you want to define
this field value should be in between these choices
regex:-you can also  define the regex and pattern of the field
'''

import mongoengine as me
import datetime
from statistics import mean
import bson
from decimal import Decimal

'''AUTHORS=["Stephen","Albert","Dantdm"]
class FamousQuote(me.Document):
    text=me.StringField(max_length=200,min_length=2)
    #author_name=me.StringField(db_field="xyz",default="author unknown",required=True)
    #author_name=me.StringField(choices=AUTHORS)
    author_name=me.StringField()
    year=me.IntField()
    earth_population=me.LongField()
    rating=me.FloatField()
    price=me.DecimalField()
    confirmed_real=me.BooleanField()
    ref=me.ObjectIdField()
me.connect("test",host="mongodb+srv://alalwani:password@mycluster-cfkbg.mongodb.net/test?retryWrites=true&w=majority")

my_quote=FamousQuote()
my_quote.text="jus for testing"
my_quote.author_name="abc"
my_quote.year=2001
my_quote.earth_population=21000000
my_quote.rating=4.3
my_quote.price=Decimal("0.10")
my_quote.confirmed_real=True
my_quote.ref=bson.ObjectId()
my_quote.save()
print(my_quote.to_json(indent=4))
'''
#using data structures in mongodb
'''
class FamousQuote(me.Document):
    text=me.StringField()
    rating=me.FloatField()
    #rating_history=me.ListField(me.IntField(choices=[1,2,3,4,5]))
    #rating_history=me.ListField(me.DynamicField())
    rating_history=me.SortedListField(me.IntField())
    #multi dimensional array
    tic_toe_board=me.ListField(me.ListField(me.StringField()))

    def calc_rating(self):
        self.rating=mean([n for n in self.rating_history if n is not None])





me.connect("test",host="mongodb+srv://alalwani:password@mycluster-cfkbg.mongodb.net/test?retryWrites=true&w=majority")
my_quote=FamousQuote()
my_quote.text='abc'
my_quote.rating_history=[2,4,3]
my_quote.calc_rating()
my_quote.tic_toe_board=[["","X","0"],["","0","X"],["X","X",""]]
my_quote.save()
print(my_quote.to_json(indent=4 ))'''

'''python vs mongodb
dictionary  in python| object in mongodb 
1.keys are object     | strings in bson/json and mongodb
'''
#dictfield,mapfield,embeddded documents,generic embedded document field




me.connect("test2",host="mongodb+srv://alalwani:password@mycluster-cfkbg.mongodb.net/test2?retryWrites=true&w=majority")

'''
class Rating(me.EmbeddedDocument):
    rating=me.IntField()
    user_name=me.StringField()
    when=me.DateTimeField(default=datetime.datetime.now)
    meta={
        "allow_inheritance":True
    }
class RatingeithComment(Rating):
    comment=me.StringField()




class FamousQuote(me.Document):
    text=me.StringField()
    id=me.SequenceField()
    #last_rating=me.DictField()
    translations=me.MapField(me.StringField())
    rating=me.FloatField()
    #last_rating=me.EmbeddedDocumentField(Rating)
    rating_history=me.EmbeddedDocumentListField(Rating)
    #using embedded generiic document field you can define any embedded document
    last_rating=me.GenericEmbeddedDocumentField()
    def calc_rating(self):
        self.rating=mean([d.rating for d in self.rating_history if d is not None])

my_quote=FamousQuote()
my_quote.text="aman"
#my_quote.last_rating={"rating":5,"user_name":"aman","when":datetime.datetime.now()}
my_quote.translations={"aman":"lalwani"}
my_quote.last_rating=Rating()
my_quote.last_rating.rating=5
my_quote.last_rating.user_name="alalwani"

my_quote.rating_history.append(Rating(rating=3,user_name='joe'))
my_quote.rating_history.append(Rating(**{"rating":1,"user_name":"Joe"}))
my_quote.calc_rating()
my_quote.last_rating=my_quote.rating_history[-1]
my_quote.save()
print(my_quote.to_json(indent=4))
#first returs none if no record exist which protect your code  from keyerror

#print(my_quote.rating_history.first())
#print(my_quote.rating_history.delete()):=returns no of entry deleted

#print(my_quote.rating_history.get(user_name="Joe").user_name)
print(my_quote.rating_history.count())
print(my_quote.rating_history.exclude(rating=1))
#update_commans

print(my_quote.rating_history.filter(rating=1).update(user_name="aman") )
'''


#file storage in mongodb
'''mongo db is not that much great with files ,mongo db uses grid fs file system '''
'''grid fs stores length,chunk size ,uploaddate,md5,filename,contentType,aliases,metadata'''
'''fs_chunks:- it is a collection which store the body of a ducument
fs_files:-it contains the indexes '''
class FamousQuote(me.Document):
    text=me.StringField()
    other_notes=me.FileField()
    icon=me.ImageField(size=(400,200,True),thumbnail_size=(20,20,True))
'''
obj=FamousQuote()
obj.text="aman"
obj.other_notes.new_file()
obj.other_notes.write(b"abc abc abc")
obj.other_notes.close()
obj.save()
print(obj.to_json(indent=4))
'''


#uploading image
'''obj=FamousQuote()
obj.text="my photo"
fh=open("/home/am.lalwani/Desktop/Youtube/db.jpg","rb")
obj.other_notes.put(fh,filename="aman_dp.jpg",metadata={"a":"b"})
obj.save()
'''

'''q=FamousQuote.objects(text="aman").first()
print(q.other_notes.read(size=4))
'''
'''when you read the file you reach out to end of the file q.other_notes.seek(0) to point to start of the file 
q.other_notes.delete()
q.save()
if file is deleted and then after you try to access it then you will get None
q.other_notes.replace(open("abc.txt","rb"))

'''
'''SequesnceField is an integer that is automatically incremented 
alternative:-
1.objectid
2. Use a imestamp
3.use timestamp and geneation number 

'''
