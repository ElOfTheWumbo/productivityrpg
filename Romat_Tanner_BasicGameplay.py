import random
player_health = 100
computer_health = 100

# Loops until someone is killed  
while (player_health >=0 and computer_health >=0):    
    # 15 average damage    
    player_move = raw_input("Would you like to punch, kick or heal? ")
    if player_move.lower() == "punch":
        damage = random.randint(10, 20)
        computer_health = computer_health - damage
        print "You dealt ",damage," damage with ",player_move
    elif player_move.lower() == "kick":
        damage = random.randint(5,25)     
        computer_health = computer_health - damage
        print "You dealt ",damage," damage with ",player_move
    elif player_move.lower() == "heal":
        damage = random.randint(10, 15)
        player_health += damage
        print "You healed yourself for ",damage," hitpoints with ",player_move
    
    # 16 average damage    
    computer_move = random.randint(1, 3)
    if computer_move == 1:
        move = "punch"
        damage = random.randint(11, 21)              
        player_health = player_health - damage
        print "Your opponent dealt ",damage," damage with ",move   
    elif computer_move == 2:
        move = "kick"
        damage = random.randint(6,26)            
        player_health = player_health - damage
        print "Your opponent dealt ",damage," damage with ",move       
    else:
        move = "heal"
        damage = random.randint(10,15)
        computer_health = computer_health + damage
        print "Your opponent healed himself for ",damage," hitpoints with ",move            
        
    print "Computer's health: ",computer_health
    print "Player's health: ",player_health

# Declare a winner
if computer_health <= 0:
    print "You won!"
elif player_health <= 0:
    print "I am afraid you have been defeated"