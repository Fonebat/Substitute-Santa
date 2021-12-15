#Substitute Santa
#Tim Jensen
#TEINF-20
#141221

meny = input("""
   Välj vad du vill göra

   1. Skriv en önskelista
   2. Läs en färdigskriven önskelista
   3. Stäng ner
""")

if "1" in meny:
   önskor = list()
   önskelista = input("Vems önskelista?: ")
   print("Skriv 'Klar' när du vill avsluta din lista")
   önska = ""
   count = 1

   while önska != "klar":
      önska = input("Önska "+str(count)+": ")
      if önska != "klar":
         önskor.append(önska)
         count += 1

   with open(önskelista+'.txt', 'w+') as text_file:
      text_file.write("\n".join(önskor))

elif "2" in meny:
   önskor = list()
   önskelista = input("Vems önskelista?: ")
   with open(önskelista+'.txt', 'r') as text_file:
      lines = text_file.readlines()
      for line in lines:
         print(line, end="")

elif "3" in meny:
   exit()