import pygame
from Settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    
    pygame.init() 
    #turns on pygame functions
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), pygame.FULLSCREEN)
    #display.set_mode shows the screen 
    pygame.display.set_caption("Alien Attack!")
    play_button = Button(ai_settings, screen, "Start Game")
    # title of the screen
    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # instance of the ship to be presented on the created screen
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #creates a group of sprites for managing all objects
    bg = pygame.image.load('bg.bmp')
    while True:
        screen.blit(bg,(0,0))
        gf.check_events(ship, screen, ai_settings, bullets, stats, play_button, aliens, sb)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(bullets, aliens, ai_settings, ship, screen, sb, stats)
            gf.update_aliens(ai_settings, aliens, ship, stats, screen, bullets, sb)
        
            print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stats, sb, play_button)



run_game() #launch the game
































