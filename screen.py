import pygame, sys

pygame.init()
screen = pygame.display.set_mode((879,579))
bg = pygame.image.load('background-1.gif')
base_font = pygame.font.Font(None,32  )
user_text = ''
game_guide = pygame.image.load('game_guide.png')
# text_box = makeTextBox(397,433,464,0,'guess here',0,24)
# showTextBox(text_box)
# entry = textBoxInput(text_box)
ok = 0
running = True
while running:
    mouse_x, mouse_y = pygame.mouse.get_pos()
#     print(mouse_y)
    for event in pygame.event.get():
        game_guide = pygame.image.load('game_guide.png')
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                
                if (30 < mouse_x < 65) and (10 < mouse_y < 50):
                    ok = 1
                else:
                    ok = 0
                    
                    
            
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode
                
                
    screen.blit(bg,(0,0))
    text_surface = base_font.render(user_text,True,(0,0,0))
    screen.blit(text_surface,(415,453))
    if ok == 1:
        screen.blit(game_guide,(50,50))
    pygame.display.update()
        
pygame.quit()    
# w    
# W