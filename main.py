import pygame
import time
from pygame.locals import *

pygame.init()

lightcoral = (240, 128, 128)
lightsalmon = (255, 160, 122)
lightgreen = (144, 238, 144)
palegreen = (152, 251, 152)
lightseagreen = (32, 178, 170)
lightcyan = (224, 255, 255)
lightblue = (173, 216, 230)
lightskyblue = (135, 206, 250)
lightgoldenrodyellow = (250, 250, 210)
lightyellow = (255, 255, 224)
lightslategray = (119, 136, 153)
lightsteelblue = (176, 196, 222)
aliceblue = (240, 248, 255)
mintcream = (245, 255, 250)
lavenderblush = (255, 240, 245)
peachpuff = (255, 218, 185)

qlis = [['seagull.jpg', ['Eagle', 'Ostrich', 'Seagull', 'Swan'], 3],
        ['peacock.jpeg', ['Seagull', 'Peacock', 'Owl', 'Pelican'], 2],
        ['ostrich.jpg', ['Owl', 'Woodpecker', 'Ostrich', 'Penguin'], 3],
        ['toucan.jpg', ['Eagle', 'Toucan', 'Parrot', 'Penguin'], 2],
        ['eagle.jpeg', ['Owl', 'Robin', 'Eagle', 'Penguin'], 3]]

WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz App")
BG = pygame.transform.scale(pygame.image.load('bgmain.jpg'), (WIDTH, HEIGHT))
font = pygame.font.SysFont('georgia', 30)


def draw_text(text, font, text_col, x, y, scale):
    a = font.render(text, True, text_col)
    width = a.get_width()
    height = a.get_height()
    img = pygame.transform.scale(a, (width * scale, height * scale))
    WIN.blit(img, (WIDTH//2-width * scale//2, y))


# BUTTON CLASS
class Button:
    button_col = lightcyan
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = (0, 0, 0)
    width = 180
    height = 70

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_button(self, hover=False):
        col = self.hover_col if hover else self.button_col

        # Add a color transition effect
        if hover:
            col = (
                col[0] + (self.hover_col[0] - self.button_col[0]) // 2,
                col[1] + (self.hover_col[1] - self.button_col[1]) // 2,
                col[2] + (self.hover_col[2] - self.button_col[2]) // 2
            )

        pygame.draw.rect(WIN, col, self.rect, border_radius=10)
        pygame.draw.line(WIN, (255, 255, 255), (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(WIN, (255, 255, 255), (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(WIN, (0, 0, 0), (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(WIN, (0, 0, 0), (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)

        font = pygame.font.SysFont('georgia', 30)
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        WIN.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))

    def is_hover(self, pos):
        return self.rect.collidepoint(pos)

    def is_clicked(self, pos, click):
        return self.rect.collidepoint(pos) and click


# GAME LOOP
def main():
    run = True
    page = 'mainpage'
    score = 0
    DEFAULT_TIMER = 5
    pygame.time.Clock().tick(60)
    while run:
        WIN.fill(lightskyblue)  # Background color

        if page == 'mainpage':
            start_button = Button(WIDTH // 2 - 90, HEIGHT // 2 - 35, 'START')
            start_button.draw_button()

            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False
                elif event.type == MOUSEBUTTONDOWN:
                    if start_button.is_clicked(pygame.mouse.get_pos(), True):
                        page = 'quizpage'
                        score = 0

        elif page == 'quizpage':
            i = 0
            timer_start_time = time.time()

            while i < len(qlis):
                WIN.fill(lavenderblush)  # Background color

                img = pygame.transform.scale(pygame.image.load(qlis[i][0]), (int(WIDTH // 2.5), int(HEIGHT // 2.5)))

                WIN.blit(img, (WIDTH // 2 - WIDTH // 5, 50))

                opt1 = Button(WIDTH // 2 - 2 * text_font.render(qlis[i][1][0], True, (0, 0, 0)).get_width(), 400,
                              qlis[i][1][0])
                opt2 = Button(WIDTH // 2 + 2 * text_font.render(qlis[i][1][0], True, (0, 0, 0)).get_width(), 450,
                              qlis[i][1][1])
                opt3 = Button(WIDTH // 2 - 2 * text_font.render(qlis[i][1][2], True, (0, 0, 0)).get_width(), 500,
                              qlis[i][1][2])
                opt4 = Button(WIDTH // 2 + 2 * text_font.render(qlis[i][1][0], True, (0, 0, 0)).get_width(), 550,
                              qlis[i][1][3])

                dic = {1: opt1, 2: opt2, 3: opt3, 4: opt4}
                oplis = [1, 2, 3, 4]
                oplis.remove(qlis[i][2])
                op1 = dic[qlis[i][2]]

                elapsed_time = time.time() - timer_start_time
                timer_text = font.render(f'Time Left: {max(DEFAULT_TIMER - int(elapsed_time), 0)}s', True, (0, 0, 0))
                WIN.blit(timer_text, (WIDTH - timer_text.get_width() - 20, 20))

                for event in pygame.event.get():
                    if event.type == QUIT:
                        run = False
                        break
                    elif event.type == MOUSEBUTTONDOWN:
                        if op1.is_clicked(pygame.mouse.get_pos(), True):
                            score += 1
                            i += 1
                            timer_start_time = time.time()
                            
                        elif dic[oplis[0]].is_clicked(pygame.mouse.get_pos(), True) or \
                                dic[oplis[1]].is_clicked(pygame.mouse.get_pos(), True) or \
                                dic[oplis[2]].is_clicked(pygame.mouse.get_pos(), True):
                            i += 1
                            timer_start_time = time.time()
                        
                if elapsed_time >= DEFAULT_TIMER:
                    i += 1
                    timer_start_time = time.time()

                for button in dic.values():
                    button.draw_button()

                if i == len(qlis) - 1:
                    page = 'endpage'

                pygame.display.update()

        elif page == 'endpage':
            WIN.fill(palegreen)
            draw_text('score = ' + str(score), font, (0, 0, 0,), 584, 140, 1.5)
            if score == int(len(qlis)):
                draw_text('WELL DONE!', font, (0, 0, 0), 534, 70, 1.5)
            elif score >= int(len(qlis) * 0.75):
                draw_text('Brilliant!', font, (0, 0, 0), 534, 70, 1.5)
            elif score >= int(len(qlis) * 0.5):
                draw_text('GOOD!', font, (0, 0, 0), 604, 70, 1.5)
            elif score >= int(len(qlis) * 0.25):
                draw_text('BETTER NEXT TIME!', font, (0, 0, 0), 504, 70, 1.5)
            restar = Button(WIDTH // 2 - text_font.render('RESTART', True, (0, 0, 0)).get_width(), 320, 'RESTART')
            restar.draw_button()
            for event in pygame.event.get():
                if event.type == QUIT:
                    run = False
                elif event.type == MOUSEBUTTONDOWN:
                    if start_button.is_clicked(pygame.mouse.get_pos(), True):
                        page = 'mainpage'
                        score = 0

            pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
                break
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    text_font = pygame.font.SysFont(None, 30)
    main()
