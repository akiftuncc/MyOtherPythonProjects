import random
key_list = ["a","b","c","d","e","f","g","h","i","j",
            "k","l","m","n","o","p","q","r","s","t",
            "u","v","w","y","z","x"]
spec_char_list = [".",":",",","*",";","/","+","-","%"]
for x in range(1500):
    password = ""
    for i in range(random.randint(8, 20)):
        if random.randint(1, 5) == 1:
            password += str(random.randint(0, 9))  
        elif random.randint(1, 5) == 2:
            password += spec_char_list[random.randint(0, 8)]            
        else:
            if 1==random.randint(1, 2):
                password += key_list[random.randint(0, 25)]
            else:
                password += key_list[random.randint(0, 25)].upper()
                
    file = open("Password List.txt", "a")
    if x % 5 == 4:
        a = "\n"
    else:
        a = "\t"
    file.write(password+a)
















