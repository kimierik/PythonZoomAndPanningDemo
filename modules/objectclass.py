import pygame
from . import pgconf



def matrixmulti(multipmatrix,cordmatrix):
    #this matrix can only calculate if the following are true
    #multimatrix will always be x row 3 collum
    #cord matrix will always be 3row 1 collum
    #only in cord matrix only input (x,y,z)touple in that format
    returncords=[0,0,0,0]
    #x,y,z=cordmatrix
    iterator=0
    for mrow in multipmatrix:#mrow is touple and each () in the given matrix
        for i in range(len(mrow)):#i is every number in the touple
            returncords[iterator]+=(mrow[i]*cordmatrix[i])  
            #multiplier always gives us the right answer

        iterator+=1

    return returncords




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


#assumes it is not panned or zoomed
    def world_to_screen(self,cords):
        cords[0]=int((cords[0]-self.panoffset[0])*self.zoomoffset)
        cords[1]=int((cords[1]-self.panoffset[1])*self.zoomoffset)
        return cords

#anything that comes has a direct ref to a screen location
#as the zoom only exists on screen space we beed to remove it
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
            data=G_wall.get_data()
            data[0]=data[0]*self.XOFFSET#x
            data[1]=data[1]*self.YOFFSET#y
            data[2]=data[2]*self.XOFFSET#w
            data[3]=data[3]*self.YOFFSET#h

            #print(self.screen_to_world([self.game.cursor_x,self.game.cursor_y]))
            #1-----2
            #|     |
            #|     |
            #4-----3

            #what
            #place to walls own calss do not call every render like this
            box_corners=[
                    [data[0],          data[1]],          
                    [data[0]+data[2],  data[1]],         
                    [data[0]+data[2],          data[1]+data[3]], 
                    [data[0],  data[1]+data[3]],
                    ]

            self.panoffset[0]+=(self.cursorDiff[0])/3
            self.panoffset[1]+=(self.cursorDiff[1])/3
            #magick number seems to fux most of our issues
            #why is cursordiff 3 times too big?
            #tbh idk why it is needed

            for i,item in enumerate(box_corners):
                box_corners[i]=self.world_to_screen(item)
                box_corners[i]= item

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


    def get_data(self):
        return [self.xc,self.yc,self.wc,self.hc]




