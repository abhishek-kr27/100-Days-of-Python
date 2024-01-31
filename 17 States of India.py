states_of_India=["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", 
"Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala",
"Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", 
"Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", 
"Uttarakhand", "West Bengal","Bombay"]

print(states_of_India[0])
print(states_of_India[-1]) #print the list by backward 

#modify the list 
states_of_India[1]= "Delhi" #Arunachal pradesh became a Delhi 
states_of_India.append("Jammu") #add Jammu at the last in a list
states_of_India.extend("Kashmir") #'K', 'a', 's', 'h', 'm', 'i', 'r'at the last in a list
states_of_India.insert(0,"Bombay") #Bombay at a 0 position and whole the list is increment by one by inserting a data 
states_of_India.remove("Delhi") #remove the name from the list
states_of_India.pop(1) #poping(remove) the data by giving their location from the list

a= states_of_India.copy() #copy the list
# states_of_India.reverse() #reverse the string
# states_of_India.clear() #clear whole list
print(states_of_India.index("Bombay")) #get the location of data 
print(states_of_India.index("Bombay",5)) #get the location of next same data
print(states_of_India.count("Assam")) #get the location number of the string from the list

print(states_of_India)
# print(a)
