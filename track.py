import pygame
import random

class Track:
    def __init__(self):
        # Track dimensions
        self.width = 800
        self.height = 600
        self.road_width = 400
        self.left_bound = (self.width - self.road_width) // 2
        self.right_bound = self.left_bound + self.road_width

        # Road properties
        self.road_color = (100, 100, 100)
        self.grass_color = (0, 150, 0)

        # Gas stations
        self.gas_stations = []
        self.generate_gas_stations()

    def generate_gas_stations(self):
        # Generate gas stations at random positions along the track
        num_stations = 3
        for _ in range(num_stations):
            x = random.randint(self.left_bound, self.right_bound - 50)
            y = random.randint(100, self.height - 100)
            self.gas_stations.append((x, y))

    def draw(self, screen):
        # Draw grass
        screen.fill(self.grass_color)

        # Draw road
        pygame.draw.rect(screen, self.road_color, 
                        (self.left_bound, 0, self.road_width, self.height))

        # Draw gas stations
        for station in self.gas_stations:
            pygame.draw.rect(screen, (255, 200, 0), (station[0], station[1], 50, 50))

    def check_gas_station_collision(self, car):
        # Check if car collides with any gas station
        for i, station in enumerate(self.gas_stations):
            if (car.x < station[0] + 50 and
                car.x + car.width > station[0] and
                car.y < station[1] + 50 and
                car.y + car.height > station[1]):
                return i
        return -1

    def reset(self):
        self.__init__()