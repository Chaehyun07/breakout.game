import  pygame

pygame.init()

#컬러코드 rgb
bbeige_marke = (250, 237, 201)

#화면 크기 설정
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width,screen_height))
#게임 표시 제목
pygame.display.set_caption("벽돌 깨기 게임")

#메인 반복구간
running = True

while running:
    for event in pygame.event.get():
        if event in  pygame.event.get() :
         if event.type == pygame.Quit :
            running = False

    screen.fill(bbeige_marke)

    pygame.display.flip()

pygame.Quit()