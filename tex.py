import pygame as pg


pg.init()
screen = pg.display.set_mode((900,600))
bg = pg.image.load('Group_2.png')
COLOR_INACTIVE = pg.Color('grey')
COLOR_ACTIVE = pg.Color('black')
FONT = pg.font.Font(None, 32)
game_guide = pg.image.load('Group_6.png')

        
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.enter = pg.Rect(x, y, w, h)
        

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
#         if event.type == pg.MOUSEBUTTONDOWN:    
#             if self.enter.collidepoint(event.pos):
#                 print('hello')
#                  
                        
        if event.type == pg.KEYDOWN:
            if self.active:
                    
                if event.key == pg.K_RETURN:
                    self.text = self.text.lower()
                    cities = ['an giang','ba ria-vung tau','bac giang','bac kan','bac lieu','bac ninh','ben tre','binh dinh','binh duong','binh phuoc','binh thuan','ca mau','can tho','cao bang','da nang','dak lak','dak nong','dien bien','dong nai', 'dong thap','gia lai','ha giang','ha nam','ha noi','hai duong','ha tinh','hai duong','hai phong','hau giang','hoa binh','ho chi minh','hung yen','khanh hoa','kien giang','kon tum','lai chau','lam dong','lang son','lao cai','long an','nam dinh','nghe an','ninh binh','ninh thuan','phu tho','phu yen','quang binh','quang nam','quang ngai','quang ninh','quang tri','soc trang','son la','tay ninh','thai binh','thai nguyen','thanh hoa','thua thien hue','tien giang','tra vinh','tuyen quang','vinh long','vinh phuc','yen bai']
                    if self.text in cities:
                        print(self.text) 
 
                    else: 
                        print("Khong hop le")
                       
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)


    def draw(self, screen):
        # Blit th screen
        screen.blit(bg,(0,0))
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+10, self.rect.y+18))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)
        #pg.draw.rect(screen, self.color, self.enter, 2)

def main():
    clock = pg.time.Clock()
    #enter = InputBox(395,500,465,55)
    input_box1 = InputBox(397,434,465,55)
    input_boxes = [input_box1]
    done = False
    ok = 0
    while not done:
        mouse_x, mouse_y = pg.mouse.get_pos()
        for event in pg.event.get():
            game_guide = pg.image.load('Group_6.png')
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:                
                    if (30 < mouse_x < 65) and (10 < mouse_y < 50):
                        ok = 1
                        
                    else:
                        ok = 0
                    
        for box in input_boxes:
            box.draw(screen)
        if ok == 1:
            screen.blit(game_guide,(90,90))
        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()