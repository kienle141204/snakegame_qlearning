from snake import SnackEnv
import pygame
import pickle

def test(env):
    with open("q_table_train.pkl", "rb") as f:
        env.q_table = pickle.load(f)
    
    epsilon = 0 # khong kham pha nua
    state = env.reset()
    done = False

    pygame.init()
    pygame.display.set_caption("AKYE")
    screen_size = 500
    block_size = screen_size // env.grid_size
    screen = pygame.display.set_mode((screen_size, screen_size))
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        screen.fill((0,0,0))
        for x, y in env.snake:
            pygame.draw.rect(screen,(0, 255, 0), (y*block_size, x*block_size, block_size, block_size))
        food_x, food_y = env.food
        pygame.draw.rect(screen, (255, 0, 0), (food_y*block_size, food_x * block_size, block_size, block_size))
        pygame.display.flip()

        action = env.choose_action(state, epsilon)
        state, _, done = env.step(action)

        clock.tick(20)
    
    print(env.points)
    pygame.quit()
    print("Test completed!")


#test
env = SnackEnv()
test(env)
