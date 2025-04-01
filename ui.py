import pygame
import time

class UI:
    def __init__(self):
        # UI state
        self.score = 0
        self.start_time = time.time()
        self.font = pygame.font.Font(None, 36)

        # Colors
        self.text_color = (255, 255, 255)
        self.warning_color = (255, 0, 0)

    def update(self, car):
        # Update score based on time
        if not car.crashed and car.fuel > 0:
            self.score = int(time.time() - self.start_time)

    def draw(self, screen):
        # Draw score
        score_text = self.font.render(f'Score: {self.score}', True, self.text_color)
        screen.blit(score_text, (10, 10))

        # Draw fuel
        fuel_text = self.font.render(f'Fuel: {int(car.fuel)}', True, 
                                   self.warning_color if car.fuel < 20 else self.text_color)
        screen.blit(fuel_text, (10, 50))

        # Draw timer
        elapsed_time = int(time.time() - self.start_time)
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        timer_text = self.font.render(f'Time: {minutes:02}:{seconds:02}', True, self.text_color)
        screen.blit(timer_text, (10, 90))

        # Draw game state messages
        if car.crashed:
            crash_text = self.font.render('CRASHED! Press R to restart', True, self.warning_color)
            screen.blit(crash_text, (250, 250))
        elif car.fuel <= 0:
            fuel_text = self.font.render('OUT OF FUEL! Press R to restart', True, self.warning_color)
            screen.blit(fuel_text, (250, 250))

    def reset(self):
        self.__init__()