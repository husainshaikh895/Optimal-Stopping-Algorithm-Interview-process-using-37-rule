# OPTIMAL STOPPING ALGORITHM - SOFTWARE FOR HR(ADMIN) FOR INTERVIEW PROCESS
#---------------------------------------------------------------------------------------------------------------
#Developers 
# HUSAIN SHAIKH
#----------------------------------------------------------------------------------------------------------------
import math
#for ceil function
import time
#for taking a break between processes so user can see
import csv
#for storing data to a csv file
import matplotlib.pyplot as plt

#Simple classifier for features

from sklearn import tree
#defining tree object using its constructor
pr=tree.DecisionTreeClassifier()

#---------------------------------------------------------------------------------------------------------------
def find37(number):
	return math.ceil(0.37*number)
#to return 37% of the candidates

def check(candidates,lookup):
	if(len(candidates)>=lookup):
		return 1
	else:
		return 0
#if lookup phase is over


def take_interview(prnlist):
	name=input("\n\nPlease Enter the name of the candidate : ")
	PRN=input("Enter the PRN : ")
	while((PRN in prnlist) or PRN==None):
		PRN=input("----PRN already exists or Invalid---Please Enter the PRN again.")
	apt_score=int(input("Please Enter the APTITUDE SCORE of {} : ".format(name)))
	while(apt_score<0 or apt_score>100):
		apt_score=int(input("----Please Enter a valid value between 0 to 100 : "))
	pers_score=int(input("Please Enter the PERSONALITY SCORE of {} : ".format(name)))
	while(pers_score<0 or pers_score>100):
		pers_score=int(input("----Please Enter a valid value between 0 to 100 : "))
	genknow_score=int(input("Please Enter the GENERAL KNWLEDGE SCORE of {} : ".format(name)))
	while(genknow_score<0 or genknow_score>100):
		genknow_score=int(input("----Please Enter a valid value between 0 to 100 : "))
	techknow_score=int(input("Please Enter the TECHNICAL KNOWLEDGE SCORE of {} : ".format(name)))
	while(techknow_score<0 or techknow_score>100):
		techknow_score=int(input("----Please Enter a valid value between 0 to 100 : "))
	base_score=(apt_score + pers_score + genknow_score + techknow_score)/4
	return name,base_score,PRN,apt_score,pers_score,genknow_score,techknow_score


#----------------------------------------------------------------------------------------------------------

print("Optimal Stopping Algorithm Demonstration using Interview process.")
time.sleep(1)
print("\n---------Developed by HUSAIN SHAIKH--------\n")
candidates={}
lookup_cands={}
selected_cands={"Name":["PRN","Aptitude","Personality","General Knowledge","Technical Knowledge","Final Score"]}
prnlist=[]
#to store prn to uniquely identify candidates

number=int(input("\nHow many candidates are there ? "))
to_be_selected=int(input("How many candidates do you want to select ? "))


while(number<to_be_selected or to_be_selected<=0):
	print("----Something went wrong...\nPlease recheck figures. Please try again...")
	number=int(input("\n\nHow many candidates are there ? "))
	to_be_selected=int(input("How many candidates do you want to select ? "))
	
#----------------------------------------------------------------------------------------------------------------	
lookup=find37(number)
check_flag=0
#to check if lookup phase is over
count=0
#----------------------------------------------------------------------------------------------------------------



print("-------- Interview Process will start Now... -------------")
lookup_score=0
lookup_count=0
features=[]
label=[]





#lookup phase
while(check_flag==0):
	name,base_score,PRN,apt_score,pers_score,genknow_score,techknow_score=take_interview(prnlist)
	listov=[PRN,apt_score,pers_score,genknow_score,techknow_score,base_score]
	count+=1
	prnlist.append(PRN)
	candidates[name]=base_score
	lookup_cands[name]=listov
	lookup_score+=base_score
	lookup_count+=1
	print("Name : {}   Score : {}   ".format(name,base_score) )
	eg=[apt_score,pers_score,genknow_score,techknow_score]
	features.append(eg)
	#adding training data for later predictions
	select=input("Do you want to select this candidate ? yes or no ? ")
	if(select.startswith("y") or select.startswith("Y")):
		selected_cands[name]=listov
		to_be_selected-=1
		label.append(1)
		prnlist.append(PRN)
		print("Candidate {} is selected.".format(name))
	else:
		label.append(0)
	if(to_be_selected==0):
		break
	
	check_flag=check(candidates,lookup)

print("----------------------------------------------------------------------------------------------")
if(to_be_selected>0):
	threshold_score=lookup_score/lookup_count
	print("\n\nThreshold of lookup phase is : ",threshold_score)
	print("Candidates above this total score will be selected automatically or else prompted for rejected.")
# End of lookup phase

print("The Features for training so far are : ",features)
print("And the labels are : ",label)

print("----------------------------------------------------------------------------------------------")
#--------------------------------------------------------------------------------------------------
#Start of selection phase


selection_flag=0
#to check if we got into selection phase
# start of consideration of selection
pr=pr.fit(features,label)
#training data for predictions later
while(to_be_selected>0 and number>len(candidates)):
	#len(candidates) is total candidates interviewed
	selection_flag=1
	name1,base_score1,PRN1,apt_score1,pers_score1,genknow_score1,techknow_score1=take_interview(prnlist)
	listov1=[PRN1,apt_score1,pers_score1,genknow_score1,techknow_score1,base_score1]
	count+=1
	print("Name : {}   Score : {}   ".format(name1,base_score1) )
	candidates[name1]=base_score1

#Machine learning prediction---------------------------------------------------------------------------------
	test = [apt_score1,pers_score1,genknow_score1,techknow_score1]
	suggest = pr.predict([test])
	if(suggest==1):
		print("Decision Tree suggests that you select this candidate.")
	else:
		print("Decision Tree suggests that you reject this candidate.")
#-------------------------------------------------------------------------------------------------------------
	if(base_score1>=threshold_score):
		
		selected_cands[name1]=listov1
		prnlist.append(PRN1)
		#adding new entry to the features and label
		features.append([test])
		label.append(1)
		print("{} is SELECTED with the base score of {} .".format(name1,base_score1))
		to_be_selected-=1
	else:
		select1=input("Candidate's overall performance seems to be below threshold value. The algorithm suggests that you reject this candidate. Do you still want to select this candidate?[Y/N]")
		if(select1.startswith("y") or select1.startswith("Y")):
			features.append([test])
			label.append(1)
			selected_cands[name1]=listov1
			prnlist.append(PRN1)
			print("{} is SELECTED with the base score of {} .".format(name1,base_score1))
			to_be_selected-=1
		else:
			label.append(0)
			print("Candidate {} was rejected.".format(name1))
#-------------------------------------------------------------------------------------------------------------
	

print("Interview process is finished!!!")
time.sleep(1)
#---------------------------------------------------------------------------------------------------------------
#calculating statistics
print("\nCalculating Statistics...")
max_score=0
min_score=101
topper_name=""
topper_score=0
downer_name=""
downer_score=101

for cands,score in candidates.items():
	if(score>topper_score):
		topper_name=cands
		topper_score=score
	if(score<downer_score):
		downer_name=cands
		downer_score=score
	
time.sleep(3)
# Show statistics 
print("\n\n---------------------------- Statistics ----------------------------------")
print("\n\nINTERVIEWED candidates are : ",candidates.keys())
if(selection_flag==1):
	print("\nLookup/Threshold score was ",threshold_score)
print("Maximum score was : {} : {}".format(topper_name,topper_score))
print("Minimum score was : {} : {}".format(downer_name,downer_score))
print("Machine Learning data is : ")
print("Features : ",features)
print("Label : ",label)
time.sleep(1)
print("\n\nSELECTED Candidates are : ",selected_cands.keys())
print("\n\nTotal Candidates INTERVIEWED : ",count)
print("Total Candidates SELECTED : ",len(selected_cands)-1)
print("Total Candidates REJECTED : ",count-(len(selected_cands)-1))
print("---------------------------------------------------------------------------")

#--------------------------------------------------------------------------------------------------------------

#Writing data to csv file
with open('selected.csv','w') as csvf:
	[csvf.write('{},{},{},{},{},{},{}\n'.format(key,*value)) for key,value in selected_cands.items()]
	csvf.close()



#---------------------------------------------------------------------------------------------------------------
time.sleep(7)


#plotting of bar graph
first=plt.bar(range(len(candidates)), list(candidates.values()), align='center', color='b')
plt.xticks(range(len(candidates)), list(candidates.keys()),rotation="50")
plt.xlabel("Candidates")
plt.ylabel("Score")
plt.title("Optimal Stopping Algorithm")
n=0
for cands,score in candidates.items():
	if(selection_flag):
		if(score<threshold_score):
			first[n].set_color("r")
		if(score>=threshold_score):
			first[n].set_color("y")
	if(cands in selected_cands):
		first[n].set_color("g")
	n=n+1
plt.show()

#---------------------------------------------------------------------------------------------------------------





	





	
