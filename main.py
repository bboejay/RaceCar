import pygame
import sys
from car import Car
from track import Track
from ui import UI

# Initialize Pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Sound effects
pygame.mixer.init()
crash_sound = pygame.mixer.Sound('assets/sounds/crash.wav')
refuel_sound = pygame.mixer.Sound('assets/sounds/refuel.wav')

class Game:
    def __init__(self):
        # Set up display
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Race Car Game')
        self.clock = pygame.time.Clock()

        # Initialize game components
        self.track = Track()
        self.car = Car()
        self.ui = UI()

        # Game state
        self.running = True
        self.paused = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Pause game
                    self.paused = not self.paused
                elif event.key == pygame.K_r:  # Restart game
                    self.reset_game()

    def update(self):
        if not self.paused:
            # Handle car input
            keys = pygame.key.get_pressed()
            self.car.handle_input(keys)

            # Update game components
            self.car.update()
            self.car.check_collision(self.track)
            self.ui.update(self.car)

            # Check for gas station collision
            station_index = self.track.check_gas_station_collision(self.car)
            if station_index != -1:
                self.car.refuel(50)
                self.track.gas_stations.pop(station_index)
                refuel_sound.play()

            # Check game over conditions
            if self.car.crashed or self.car.fuel <= 0:
                if not self.car.crashed:
                    self.car.crashed = True
                crash_sound.play()

    def render(self):
        self.screen.fill(WHITE)
        self.track.draw(self.screen)
        self.car.draw(self.screen)
        self.ui.draw(self.screen)
        pygame.display.flip()

    def reset_game(self):
        self.car.reset()
        self.track.reset()
        self.ui.reset()
        self.paused = False

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = Game()
    game.run()