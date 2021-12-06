import os
import platform

global listStd 
listStd = ["Kim Yzabelle Ramal", "Bianca Kiesha Maldonado", "Gerlie Tordecilla", "Abby Bruce"] 

def manageStudent(): 

	print(""" 

  ---------------------------------------------------------
 |========================================================| 
 |======== Welcome To Enrollment System =========|
 |========================================================|
  ---------------------------------------------------------

Enter 1 : To View Student List
Enter 2 : To Apply New Student
Enter 3 : To Search Student 
Enter 4 : To Remove Student 
		
		""")

	try: 
		userInput = int(input("Please Select An Above Option: ")) 
	except ValueError:
		exit("\nThat's Not A Number") 
	else:
		print("\n") 

	
	if(userInput == 1): 
		print("List of Student\n")  
		for Student in listStd:
			print("=> {}".format(Student))

	elif(userInput == 2): 
		newStd = input("Enter New Student: ")
		if(newStd in listStd):
			print("\nThis Student {} Already In The Database".format(newStd))  
		else:	
			listStd.append(newStd)
			print("\n=> New Student {} Successfully Add \n".format(newStd))
			for Students in listStd:
				print("=> {}".format(Students))	

	elif(userInput == 3): 
		srcStd = input("Enter Student Name To Search: ")
		if(srcStd in listStd): 
			print("\n=> Record Found Of Student {}".format(srcStd))
		else:
			print("\n=> No Record Found Of Student {}".format(srcStd)) 

	elif(userInput == 4): 
		rmStd = input("Enter Student Name To Remove: ")
		if(rmStd in listStd): 
			listStd.remove(rmStd)
			print("\n=> Student {} Successfully Deleted \n".format(rmStd))
			for Students in listStd:
				print("=> {}".format(Students))
		else:
			print("\n=> No Record Found of This Student {}".format(rmStd)) 
	 
	elif(userInput < 1 or userInput > 4): 
		print("Please Enter Valid Option")
						

manageStudent()

def runAgain(): 
	runAgn = input("\nContinue Transaction? y/n: ")
	if(runAgn.lower() == 'y'):
		
		manageStudent()
		runAgain()
	else:
		quit() 

runAgain()