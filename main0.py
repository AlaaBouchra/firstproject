# Import the libraries
import pygame          
import time  
import random               

# Initialize the Pygame library
pygame.init()                




# Define color constants
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set both the width and height of the game window
dis_width = 600              
dis_height = 400             

# Create the game window
dis = pygame.display.set_mode((dis_width, dis_height))  

# Set the title of the game window
pygame.display.set_caption('Snake Game') 

# Create a clock object to track time in the game
clock = pygame.time.Clock()  

# Set the size of each block in the snake
snake_block = 10  

# Set the speed of the snake
snake_speed = 10             

# Create font objects for displaying text
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
# Define a Player class to store player-related information
class Player:

    # Player's atributes  
    name = ''              
    score = 0                

    # Return a string representing the player's score
    def win(self):
        return f"{self.name} has {self.score}"  

    # Increment the player's score by 1
    def incScore(self):
        self.score += 1 



# Create an instance of the Player class
player1 = Player()            

# Function to draw the snake on the screen
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Function to display a message on the screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

# Main game loop
def gameLoop():

    # Use this boolean variable to trigger if the game is over, or if the game window should be closed
    game_over = False  
    game_close = False       

    # Initial x/y-coordinate of the snake's head
    x1 = dis_width / 2       
    y1 = dis_height / 2     


    # Change in x/y-coordinate of the snake's head
    x1_change = 0 
    y1_change = 0            

    # List to store the coordinates of the snake
    snake_List = [] 

    # Initial length of the snake         
    Length_of_snake = 1     

    # x/y-coordinate of the food item
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0   
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0  

    # Main game loop
    while not game_over:
        while game_close == True:
            
            # Fill the screen backround
            dis.fill(blue)                         
            
            # Reset the player's score
            player1.score = 0                      
            
            # Display a game over message
            message("You Lost! Press Q-Quit or C-Play", red) 

            # Update the display
            pygame.display.update()

            # Handle keyboard events in the game over screen
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

                    # If Q is pressed, quit the game
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

                    # If C is pressed, restart the game
                    if event.key == pygame.K_c: 
                        gameLoop()

        # Handle keyboard events in the game
        for event in pygame.event.get():

            # If the window close button is clicked, quit the game
            if event.type == pygame.QUIT: 
                game_over = True
            if event.type == pygame.KEYDOWN:

                # Move the snake left when the left arrow key is pressed
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                
                # Move the snake right when the right arrow key is pressed
                elif event.key == pygame.K_RIGHT: 
                    x1_change = snake_block
                    y1_change = 0
                
                # Move the snake up when the up arrow key is pressed
                elif event.key == pygame.K_UP:      
                    y1_change = -snake_block
                    x1_change = 0

                # Move the snake down when the down arrow key is pressed
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # If the snake hits the boundaries of the game window, end the game
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Update the x/y-coordinate of the snake's head
        x1 += x1_change
        y1 += y1_change

        # Fill the screen with blue color
        dis.fill(blue)
        
        # Draw the food item on the screen
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # Append the current head position to the snake list
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # Remove the oldest segment of the snake if it exceeds the desired length
        if len(snake_List) > Length_of_snake:
            del snake_List[0]                      

        # If the snake collides with itself, end the game
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw the snake on the screen
        our_snake(snake_block, snake_List)

        # Render and display the player's score
        value = score_font.render(f"Your Score: {player1.score}", True, yellow)
        dis.blit(value, [0, 0])

        # Update the display
        pygame.display.update()

        # Generate new coordinates for the food item
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0  
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                
            # Increase the length of the snake
            Length_of_snake += 1 

            # Increase the player's score 
            player1.incScore()

        # Limit the frame rate of the game (per second)
        clock.tick(snake_speed)

    # Quit the Pygame library
    pygame.quit()
    
    # Quit the program
    quit()



# Call the main game loop to start the game
gameLoop()