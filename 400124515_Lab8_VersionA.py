'''
Hamdan Basharat
4000124515
basham1
IBEHS 1P10
Lab 8 Version A Assignment
Novenmber 5th, 2017
'''
#importing the required libraries
import math

#request the user to input values for variables. Values were saved as floats
initialDiameter = float(input("Please enter the initial diameter of the test material: "))
initialLength = float(input("Please enter the intial length of the test material: "))
yieldStrength = float(input("Please enter the yield strength of the test material: "))

#requests the user to input the name of the file they wish to open. Opens, reads, and saves the contents of the file under the list copiedFile. Closes the original file afterwards
inFile = input("File Name: ")
copiedFile = open(inFile,'r')
data = copiedFile.readlines()
copiedFile.close()

#creates a list under the variable dataList
dataList = []
#fills the list with the same number of indexes as the number of indexes in the data list
for l in range(len(data)):
    dataList.append(l)

#splits the lines in the list into separate strings and then sets them to float.
for i in range(len(data)):
    dataList[i] = data[i].split()
    dataList[i][0] = float(dataList[i][0])
    dataList[i][1] = float(dataList[i][1])
    #print(dataList[i])

#checks if the data provided is valid. If not, the program is closed
i = 0
for i in range(len(dataList)):
    if dataList[i][0] < 0 or dataList[i][1] < 0:
        print("Provided set is invalid.")
        quit()
    else:
        i += 1
if len(dataList) < 10 or len(dataList) > 100:
        print("Provided set is invalid.")
        quit()

#creates a list under the variable SSValues
SSValues = []

#fills the list with the same number of indexes as the number of indexes in the data list
for l in range(len(data)):
    SSValues.append(l)

#splits the lines in the list into separate strings and then sets them to float
for i in range (len(data)):
    data[i] = data[i].split()
    x = (data[i][0])
    y = (data[i][1])
#calculates the values for stress and strain and assigns the values under the correct index in SSValues
    stress = (float(x)/((math.pi/4)*initialDiameter**2))
    strain = (float(y)/initialLength)
    SSValues[i] = [stress, strain]
    #print(SSValues[i])

#creates variables for plastic deformation and tensile strength
plasticDeform = 0
tensileStr = 0

#stores the index value of SSValues where plastic deformation is noted (Stores none if there is no plastic deformation)
for i in range(len(SSValues)):
    a = SSValues[i][0]
    if a >= yieldStrength:
              plasticDeform = SSValues[i]
              break
    else:
              plasticDeform = None
    i += 1
              
#stores the index value of SSValues where tensile strength is noted (Stores none if there is no tensile strength)
for i in range(1,len(SSValues)-1):
    if SSValues[i][0] > SSValues[i-1][0] and SSValues[i][0] > SSValues[i+1][0]:
              tensileStr = SSValues[i]
              break
    else:
              tensileStr = None
    i += 1

#prints out the index for plastic deformation and tensile strength
if plasticDeform == None:
    print("There was no plastic deformation. This means that all of the stress and strain values fell under linear elastic deformation.")
else:
    print("Plastic Deformation is seen when stress and strain equal " + str(plasticDeform) + ". This index is the set of values where the graph of stress and strain changes from linear elastic deformation to plastic deformation")
if tensileStr == None:
    print("There was no tensile strength. This means that there was no stress value that was larger than the stress values before and after it.")
else:
    print("Tensile Strength is seen when stress and strain equal " + str(tensileStr) + ". This index is the set of values with the largest stress value.")

