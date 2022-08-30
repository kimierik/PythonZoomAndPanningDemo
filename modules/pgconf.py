import pygame

#this is a good pygame conf file that can just be copy pasted to any project that needs pygame
#this sets put the window pretty good 

class pg_data():
    def __init__(self,width,height,caption):
        pygame.init()
        self.width=width
        self.height=height
        self.win=pygame.display.set_mode((width,height))
        self.fps=30
        pygame.display.set_caption(caption)
        self.cursor_x=self.width/2
        self.cursor_y=self.height/2

        

        self.colors={
            "black":(0,0,0),
            "white":(255,255,255),
            "red":(255,0,0),
            "blue":(0,0,255),
            "green":(0,255,0)
        }
        
