xx="""
TRAINING 
"""
import numpy
from os import listdir
from os.path import isfile,join
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
import cv2

x=[]
y=[]
print(xx)
files_name=[f for f in listdir('testsdc') if isfile(join('testsdc',f))]

for name in files_name:
    img=cv2.imread(join('testsdc',name))
    cv2.imshow('Learning Image',img)
    cv2.waitkey(100)
    cv2.desstroyAllWindows()
    img=cv2.blur(img,(5,5))
    retval,img=cv2.threshold(img,201,255,cv2.THRESH_BINARY)
    img=cv2.resize(img,(24,24))
    image_as_array=numpy.ndarray.flatten(numpy.array(img))
    x.append(image_as_array)
    y.append(name.split('_')[0])

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=42)

scaler=StandardScaler()
scaler.fit(xtrain)
xtrain=scaler.transform(xtrain)
xtest=scaler.transform(xtest)

alg=MLPClassifier(solver='lbfgs',alpha=100.0,random_state=1,hidden_layer_sizes=50,verbose=True)
alg.fit(xtrain,ytrain)
print(alg.score(xtest,ytest))
joblib.dump(alg,'model.pkl')
print(xx)
