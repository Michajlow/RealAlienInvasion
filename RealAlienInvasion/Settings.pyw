import pygame

class Settings():
    #create an object for all settings
    
    def __init__(self):
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = 0,0,0
        self.ship_limit = 3
        self.fleet_drop_speed = 15
        self.bullet_width = 2
        self.bullet_height = 60
        self.bullets_allowed = 2
        self.bullet_color = 255, 0, 0
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        self.alien_speed_factor = 5
        self.bullet_speed_factor = 35
        self.ship_speed = 25
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *=self.speedup_scale
        self.bullet_speed_factor *=self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points*self.score_scale)
        
		
