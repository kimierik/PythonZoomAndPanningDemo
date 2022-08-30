from modules import pgconf
from modules import objectclass
import pygame

game=pgconf.pg_data(900,900,"testing")



def main():
    run=True
    owner=objectclass.ObjectOwner(game)
    owner.make_G_wall(0,0,4,4)
    owner.make_G_wall(-2,-5,2,4)
    owner.make_G_wall(8,6,1,1)
    

    clk=pygame.time.Clock()
    while run:
        clk.tick(game.fps)
        
        game.win.fill(game.colors["white"])


        owner.render_G_walls()
        owner.render_cursor()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run=False

        key=pygame.key.get_pressed()


        if key[pygame.K_a]:
            owner.panoffset[0]-=1
        if key[pygame.K_d]:
            owner.panoffset[0]+=1
        if key[pygame.K_w]:
            owner.panoffset[1]-=1
        if key[pygame.K_s]:
            owner.panoffset[1]+=1

        owner.update_value_before()
        if key[pygame.K_i]:
            if owner.zoomoffset>=0.2:
                owner.zoom(0.995)
        if key[pygame.K_k]:
            owner.zoom(1.005)

        owner.update_values_after()


if __name__=="__main__":
    main()
