import os
import pandas
import joblib
from sklearn.linear_model import LinearRegression

data = pandas.read_csv("SalaryData.csv")
#print(ds)

X = data['YearsExperience'].values.reshape(30,1)
#print(X.shape)

y = data['Salary']

model = LinearRegression()
model.fit(X,y)


def Exp():
        #os.system("tput setaf 2")
        exp  = float(input( "\t \t \t \t Enter the year of experience: "))
        #os.system(tput setaf 7")

        print("\t \t \t \tSalary should be : "  ,  model.predict([[exp]]))
while True:
	Exp()
	while True:
		quit = input("\n Do you want to continue Y/N :")
		if (quit == "Y") or (quit == "y"):
			break
		elif ("N" in quit) or ("n" in quit):
			exit()
		else:
			print("please press vaild key ")
			continue
            
        
            
joblib.dump(model,"salary.pk1")


