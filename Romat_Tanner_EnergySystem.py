myFile = open("energyfile.txt", "r")
energy = myFile.readlines()
energy = ', '.join(energy)
task_completed = False # Get checkbox value from gui
points = 5 # Get point value for completion from gui
button_clicked = True # Get clicked value from gui
button2_clicked = True # Get clicked value from gui
button3_clicked = True # Get clicked value from gui

# Gives a certain amount of points based on task completed
if (task_completed == True):
    energy = int(energy) + points
 
# Takes away an energy point is the player or enemy has been defeated    
if player_health <= 0 or enemy_dead == True:
    energy = int(energy) - 1
    
if button_clicked == True or button2_clicked == True or button3_clicked == True:
    energy = int(energy) - 1
    button_clicked = False
    button2_clicked = False
    button3_clicked = False   
       
myFile = open("energyfile.txt", "w")    
print energy
myFile.seek(0)
myFile.truncate()
myFile.write(str(energy))
myFile.close()
