import mongoengine as mongoconnector
from statistics  import mean
class RatingManager(mongoconnector.Document):
    rating=mongoconnector.FloatField()
    rating_history=mongoconnector.ListField(mongoconnector.IntField(choices=[1,2,3,4,5]))
    dynamic_review=mongoconnector.ListField(mongoconnector.DynamicField())
    sorting_rating=mongoconnector.SortedListField(mongoconnector.IntField())
    #multi dimensional array##
    multi_rating=mongoconnector.ListField(mongoconnector.ListField(mongoconnector.IntField()))

    def calc_rating(self):
        self.rating=mean([n for n in self.rating_history if n is not None])

mongoconnector.connect("datatype",host="mongodb+srv://alalwani:cr6xjy88jt@mycluster-cfkbg.mongodb.net/datatype?retryWrites=true&w=majority")
rating_demo=RatingManager(**{'rating_history':[1,3,2],'dynamic_review':[1,'good',2],'sorting_rating':[4,3,2,1],'multi_rating':[[1,3,2],[2,1,3]]})
rating_demo.calc_rating()
rating_demo.save()
print(rating_demo.to_json(indent=4))

