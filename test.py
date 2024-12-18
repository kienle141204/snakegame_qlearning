from snake import SnackEnv
import pygame
import pickle


def test(env,n):
    with open(f"q_table_train_{n//2}_test.pkl", "rb") as f:
        env.q_table = pickle.load(f)
    
    epsilon = 0 # khong kham pha nua
    state = env.reset()
    done = False

    pygame.init()
    pygame.display.set_caption("")
    screen_size = 500
    block_size = screen_size // env.grid_size
    screen = pygame.display.set_mode((screen_size, screen_size))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36) 
    env.points = 0

    while not done:
        screen.fill((0,0,0))

        for x, y in env.snake:
            pygame.draw.rect(screen,(0, 255, 0), (y*block_size, x*block_size, block_size, block_size))
        food_x, food_y = env.food
        pygame.draw.rect(screen, (255, 0, 0), (food_y*block_size, food_x * block_size, block_size, block_size))

        # Hiển thị điểm số
        score_text = font.render(f"Score: {env.points}", True, (255, 255, 255))  # Màu trắng
        screen.blit(score_text, (10, 10))  # Vị trí hiển thị điểm số (góc trên bên trái)

        pygame.display.flip()  # Cập nhật màn hình

        action = env.choose_action(state, epsilon)
        state, _, done = env.step(action)

        clock.tick(90)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True


    print(env.points)
    pygame.quit()
    print("Test completed!")


#test
# env = SnackEnv(20)
# test(env)
