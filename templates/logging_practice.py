import logging

#change configuration


logger=logging.getLogger(__name__)
file_handler=logging.FileHandler('test_log')

logging.basicConfig(filename='test.log',level=logging.DEBUG,
format='%(asctime)s:%(levelname)s:%(message)s')
def add(x,y):
    return x+y

#there are five logging levels
#debug:-detailed information,typically of interest only when diagnsing problems
#info:-confirmation tha things are working as expected
#warning:-An indication that something unexpected reported,or indiaction of some problem
#in the near future ,the software is still working as expected
#Error:-Due to a more serious problem ,the software has not been able to perform some functions.
#crirical:-a serious error ,indiacationg that the program itself may be unable t ocontinue running.


#the default level is warning which means it does not print out debug or info
a=add(1,2)
logging.debug(a)

#create a log file

