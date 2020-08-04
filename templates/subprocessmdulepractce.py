import subprocess
from subprocess import PIPE
#subprocess.run('ls -la',shell=True)

#run same command without shell =True
#p1=subprocess.run(['ls','-la'],stdout=PIPE)
#capture_output/stdout=True instead of printing  the output to the console it will return the output
#don 't do shell true if you are woreking with user input

#subprocess.run('ls',shell=True)
#print(p1.stdout.decode())
#decode gives the code in same format convert bytes to string

#with open('output.txt','w') as f:
 #   p1=subprocess.run(['ls','-la'],stdout=f)'''

# to get stderr get
#print(p1.stderr)
#check=True when we want to throw an Exception when command fails
#passing an output of one process as input to another
#p2=subprocess.run(['grep','-n','test'],capture_output=True,text=True,input=p1.stdout)

#p1=subprocess.run('cat test.txt|grep -n test',capture_output=True,shell=True)
