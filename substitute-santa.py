#Substitute Santa
#Tim Jensen
#TEINF-20
#141221


options = list()
genre = input("Namn på önskelistan: ")
option = ""
count = 1
while option != "klar":
   option = input("Option "+str(count)+": ")
   if option != "done":
      options.append(option)
      count += 1

with open(genre+'.txt', 'w+') as text_file:
  text_file.write("\n".join(options))