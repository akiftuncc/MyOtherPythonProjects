file = open("Password List.txt", 'r')
lines = file.readlines()
x = {}
new_list = []
count = 0
for i in lines:
    line = i.split("\t")
    for j in line:
        count += 1
      #  if count % 5 == 4:
        j = j.replace("\n", "")            
        if len(j) in x.keys():
            x[len(j)] += (j)
        else:
            x[len(j)] = (j)
for i in range(8,20):
    count = 0
    sena = ""
    x[i].split("\n")
    for k in x[i]:
        sena += x[i][count]
        if len(sena) % i == 0:
            new_list.append(sena)
            sena = ""
        count += 1
file.close()
file = open("Password Sorted List.txt", "a")
count = 0
for i in new_list:
    count+=1
    file.write(i+"     ")
    if count == 5:
        file.write("\n")
        count = 0
        
file.close()

