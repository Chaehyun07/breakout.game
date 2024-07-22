import  pygame

pygame.init()

#컬러코드 rgb
bbeige_marke = (250, 237, 201)
ford_dark_charcoal = (50, 50, 50)
black = (0, 0, 0)

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

#패드 설정
paddle_width = 100
paddle_height = 10
paddle_x = screen_width // 2 - paddle_width // 2
paddle_y = screen_height - 40
paddle_dx = 0
paddle_speed = 6

screen = pygame.display.set_mode((screen_width,screen_height))
#게임 표시 제목
pygame.display.set_caption("벽돌 깨기 게임")

#메인 반복구간
running = True

clock = pygame.time.Clock()


while running:
    #이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
           running = False
            #키가 눌렸을 때 발생
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_dx = -paddle_speed
            if event.key == pygame.K_RIGHT:
                paddle_dx = paddle_speed
           #키가 떼어졌을 때 발생
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle_dx = 0

#패들 이동
    paddle_x += paddle_dx
    if paddle_x < 0:
        paddle_x = 0
    if paddle_x > screen_width - paddle_width:
        paddle_x = screen_width - paddle_width


    ball_x += ball_dx
    ball_y += ball_dy

#공 튕기기
    if ball_x <= 0 or ball_x >= screen_width - ball_width:
        ball_dx = -ball_dx #공의 x방향을 반전

    if ball_y <= 0 or ball_y >= screen_height - ball_height:
        ball_dy = -ball_dy #공의 y방향을 반전


    screen.fill(bbeige_marke)

    pygame.draw.ellipse(screen, ford_dark_charcoal,(ball_x, ball_y, ball_width, ball_height)
                        )
    #패들 그리기

    paddle_rect = pygame.Rect (paddle_x, paddle_y, paddle_width, paddle_height)
    pygame.draw.rect(screen, black, paddle_rect)

    pygame.display.flip()
    clock.tick(60)
pygame.Quit()