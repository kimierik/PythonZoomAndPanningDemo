import pygame
from . import pgconf







class ObjectOwner:
    def __init__(self,game):
        self.game=game
        self.G_walls=[]
        self.zoomoffset=1.0
        self.panoffset=[-self.game.cursor_x,-self.game.cursor_y]
        #make a setter for zoom and pan offset
        self.XOFFSET=30
        self.YOFFSET=30
        self.afterzoom=[0,0]
        self.beforezoom=[0,0]
        self.cursorDiff=[0,0]
        


    def zoom(self,diff):
        self.zoomoffset*=diff


    def make_G_wall(self,x,y,w,h):
        self.G_walls.append(G_wall(x,y,w,h,self.XOFFSET,self.YOFFSET))


    def render_cursor(self):
        rect=pygame.Rect(self.game.cursor_x-10/2,
               self.game.cursor_y-10/2,
               10,
               10
               )
        pygame.draw.rect(self.game.win,self.game.colors["green"],rect)


    def world_to_screen(self,cords):
        cords[0]=int((cords[0]-self.panoffset[0])*self.zoomoffset)
        cords[1]=int((cords[1]-self.panoffset[1])*self.zoomoffset)
        return cords

    def screen_to_world(self,cords):
        cords[0]=(cords[0]/self.zoomoffset)+self.panoffset[0]
        cords[1]=(cords[1]/self.zoomoffset)+self.panoffset[1]
        return cords
    


    def update_values_after(self):
        self.afterzoom = self.screen_to_world([self.game.cursor_x,self.game.cursor_y])
        self.cursorDiff[0]=self.beforezoom[0]-self.afterzoom[0]
        self.cursorDiff[1]=self.beforezoom[1]-self.afterzoom[1]

    def update_value_before(self):
        self.beforezoom = self.screen_to_world([self.game.cursor_x,self.game.cursor_y])


    def render_G_walls(self):
        for G_wall in self.G_walls:
            #seperation probably not needed
            box_corners=[[],[],[],[]]
            data=G_wall.get_world_corners()

            self.panoffset[0]+=(self.cursorDiff[0])/3
            self.panoffset[1]+=(self.cursorDiff[1])/3
            #magick number seems to fux most of our issues
            #why is cursordiff 3 times too big?
            #tbh idk why it is needed

            for i,item in enumerate(data):
                box_corners[i]=self.world_to_screen(item)
                #box_corners[i]= item

            pygame.draw.polygon(self.game.win,self.game.colors["black"],box_corners)




class G_wall:
    def __init__(self,xc,yc,wc,hc,xo,xy):
        self.xc=xc
        self.yc=yc
        #xc and yc is x and y cordinates
        self.wc=wc
        self.hc=hc
        self.SizeMultipliers=[xo,xy]
        #w and h is to be changed to how many things in the grid do they take
        #w is how many to the rigth etc
        self.WorldCords=[xc*self.SizeMultipliers[0],yc*self.SizeMultipliers[1],wc*self.SizeMultipliers[0],hc*self.SizeMultipliers[1]]
        #cannot be assigned on init
        #bc of how python "compiles" self.corners would be changed even if we did not want it to change
        """
        self.corners=(
                    [self.WorldCords[0],          self.WorldCords[1]],          
                    [self.WorldCords[0]+self.WorldCords[2],  self.WorldCords[1]],         
                    [self.WorldCords[0]+self.WorldCords[2],          self.WorldCords[1]+self.WorldCords[3]], 
                    [self.WorldCords[0],  self.WorldCords[1]+self.WorldCords[3]],
                    )
                    """


    def get_data(self):
        return [self.xc,self.yc,self.wc,self.hc]

    def get_world_corners(self):
        return (
                    [self.WorldCords[0],          self.WorldCords[1]],          
                    [self.WorldCords[0]+self.WorldCords[2],  self.WorldCords[1]],         
                    [self.WorldCords[0]+self.WorldCords[2],          self.WorldCords[1]+self.WorldCords[3]], 
                    [self.WorldCords[0],  self.WorldCords[1]+self.WorldCords[3]],
                    )


