# TextGameMaker
Make text games with a python module

# Documentation:
Making objects:\n
  There are 7 values in an object, and they are; Usable, Takeable, Position, Name, Look_Text, Use_Text, and Take_Text.
  What the values do:
    - Usable: Either True or False. Tells the program if the object can be used.
    - Takeable: Either True or False. Tells the program if the object can be taken.
    - Position: List with 2 values. Tells the program where the object is so it can calculate if the player is in the same room.
    - Name: String. Tells the program the objects name. *Must include "The" if applicable*
    - Look_Text: String. When the player inputs "look ?" or "look at ?" it will print this value to the player's screen.
    - Use_Text: String. When the player inputs "use ?" it will print this value to the player's screen.
    - Take_Text: String. When the player inputs "take ?" it will print this value to the player's screen.
  
  Special Cases:
    Name needs "The" if applicable.
    In position: The x value is stored as the first list object.

Player:
  There is 1 value in the Player object, and it is the position.
  What it does:
    Stores the players position.
    
  Special Cases:
    The x value is stored first in the list.

Rooms:
  There are 3 values in the Room class. They are; Position, Look_Text, and Go_Text.
  What they do:
    - Position: List. Stores the position.
    - Look_Text: String. When the player inputs "look" it will print this value to the player's screen.
    - Go_Text: String. When the player inputs "go ?" and it is aimed at this room it will print this value to the screen.
    
  Special Cases:
    N/A
