import pygame

class Car:
    def __init__(self):
        # Car properties
        self.width = 40
        self.height = 60
        self.x = 400 - self.width // 2
        self.y = 500 - self.height // 2
        self.speed = 0
        self.max_speed = 5
        self.acceleration = 0.2
        self.deceleration = 0.1
        self.steering = 0.1
        self.fuel = 100
        self.fuel_consumption_rate = 0.1

        # Car state
        self.crashed = False

    def update(self):
        # Handle fuel consumption
        if self.speed > 0:
            self.fuel -= self.fuel_consumption_rate
            if self.fuel <= 0:
                self.fuel = 0
                self.speed = 0

        # Update position
        self.x += self.speed

    def handle_input(self, keys):
        if self.crashed:
            return

        # Acceleration and braking
        if keys[pygame.K_UP]:
            self.speed = min(self.speed + self.acceleration, self.max_speed)
        elif keys[pygame.K_DOWN]:
            self.speed = max(self.speed - self.deceleration, 0)

        # Steering
        if keys[pygame.K_LEFT]:
            self.x -= self.steering * self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.steering * self.speed

    def check_collision(self, track):
        # Check if car is out of track bounds
        if self.x < track.left_bound or self.x + self.width > track.right_bound:
            self.crashed = True

    def refuel(self, amount):
        self.fuel = min(self.fuel + amount, 100)

    def draw(self, screen):
        # Draw car body
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def reset(self):
        self.__init__()