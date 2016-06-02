myFile = open("energyfile.txt", "r")
energy = myFile.readlines()
energy = ', '.join(energy)
task_completed = True # Get checkbox value from gui
points = 5 # Get point value from gui

if (task_completed == True):
    energy = int(energy) + points

myFile = open("energyfile.txt", "w")    
print energy
myFile.seek(0)
myFile.truncate()
myFile.write(str(energy))
myFile.close()