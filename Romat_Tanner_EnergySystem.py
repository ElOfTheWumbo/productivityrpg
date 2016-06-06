import productivityrpg.py

myFile = open("energyfile.txt", "r")
energy = myFile.readlines()
energy = ', '.join(energy)
task_completed = False # Get checkbox value from gui
points = 5 # Get point value for completion from gui

if (task_completed == True):
    energy = int(energy) + points
 
# Takes away an energy point is the player or enemy has been defeated    
if player_health <= 0 or enemy_dead == True:
    energy = int(energy) - 1
    

myFile = open("energyfile.txt", "w")    
print energy
myFile.seek(0)
myFile.truncate()
myFile.write(str(energy))
myFile.close()
