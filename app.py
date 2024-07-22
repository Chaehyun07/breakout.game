import  pygame

pygame.init()

#컬러코드 rgb
bbeige_marke = (250, 237, 201)
ford_dark_charcoal = (50, 50, 50)

#화면 크기 설정
screen_width = 800
screen_height = 600

#공 생성
ball_width = 10 #공 크기 지정
ball_height = 10
ball_x = screen_width // 2 - ball_width // 2 #공 위치지정
ball_y =  screen_height //2 - ball_height // 2
ball_dx = 3
ball_dy = -3

screen = pygame.display.set_mode((screen_width,screen_height))
#게임 표시 제목
pygame.display.set_caption("벽돌 깨기 게임")

#메인 반복구간
running = True

clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event in  pygame.event.get() :
         if event.type == pygame.Quit :
            running = False

    ball_x += ball_dx
    ball_y += ball_dy


    screen.fill(bbeige_marke)

    pygame.draw.ellipse(screen, ford_dark_charcoal,(ball_x, ball_y, ball_width, ball_height)
                        )

    pygame.display.flip()
    clock.tick(60)
pygame.Quit()