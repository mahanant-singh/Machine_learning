import pickle 
from model import MyLr
lr=MyLr()
pickle.dump(lr,open('customlr1.pkl',"wb"))
