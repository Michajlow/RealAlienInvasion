import sys
import pygame
from alien import Alien
from bullet1 import Bullet as bullet1
from bullet2 import Bullet as bullet2
from time import sleep

def check_keydown_events(event, ship, ai_settings, screen, bullets, stats):
    if event.key == pygame.K_d:
            ship.moving_right = True
    elif event.key == pygame.K_a:
            ship.moving_left = True
    elif event.key == pygame.K_w:
            ship.moving_up = True
    elif event.key == pygame.K_s:
            ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        if stats.game_active == True:
            stats.game_active = False
        elif stats.game_active == False:
            stats.game_active = True
            pygame.mouse.set_visible(False)
    elif event.key == pygame.K_ESCAPE:
            sys.exit(1)
    elif event.key == pygame.K_p:
        new_bullet = [bullet1(ai_settings,screen,ship), bullet2(ai_settings,screen,ship)]
        bullets.add(new_bullet)

def ship_hit(ai_settings, aliens, ship, stats, screen, bullets, sb):
    if stats.ships_left > 0:
        stats.ships_left -=1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


            
def check_keyup_events(event, ship):
    if event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False 
    elif event.key == pygame.K_w:
         ship.moving_up = False
    elif event.key == pygame.K_s:
         ship.moving_down = False


def check_events(ship, screen, ai_settings, bullets, stats, play_button, aliens, sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, sb)

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y, sb):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)
        
        ai_settings.initialize_dynamic_settings()
        sb.prep_high_score()
        stats.reset_stats()
        stats.game_active = True
        sb.prep_score()
        sb.prep_level()
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()



def get_alien_number(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x /(2.2*alien_width))
    return number_aliens_x


def get_row_number(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height -(3*alien_height) - ship_height)
    number_rows = int(available_space_y / (3*alien_height))
    return number_rows


def create_alien(aliens, alien_number, ai_settings, screen, row_number):
     alien = Alien(ai_settings, screen)
     alien_width = alien.rect.width
     alien.x = alien_width + 2*alien_width*alien_number
     alien.rect.x = alien.x
     alien.rect.y = alien.rect.height +2*alien.rect.height*row_number
     aliens.add(alien)



def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_alien_number(ai_settings,alien.rect.width)
    number_rows = get_row_number(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(aliens, alien_number,ai_settings, screen, row_number)
        


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, aliens, ship, stats, screen, bullets, sb):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, aliens, ship, stats, screen, bullets, sb)
    check_aliens_bottom(ai_settings, aliens, ship, stats, screen, bullets, sb)


def update_bullets(bullets, aliens, ai_settings, ship, screen, sb, stats):
    for bullet in bullets.copy():
            if bullet.rect.bottom <=0:
                bullets.remove(bullet)
                

    check_collision(ai_settings, ship, screen, aliens, bullets, sb, stats)
    
def check_collision(ai_settings, ship, screen, aliens, bullets, sb, stats):
        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                stats.score += ai_settings.alien_points * len(aliens)
                sb.prep_score()
            check_high_score(stats,sb)
        if len(aliens) ==0:
            bullets.empty()
            ai_settings.increase_speed()
            stats.level +=1
            sb.prep_level()
            create_fleet(ai_settings, screen, ship, aliens)

def check_high_score(stats, sb):
        if stats.score > stats.high_score:
            stats.high_score = stats.score
            sb.prep_high_score()

def update_screen(ai_settings, screen, ship, bullets, aliens, stats, sb, play_button):
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
    # refresh the screen


def check_aliens_bottom(ai_settings, aliens, ship, stats, screen, bullets, sb):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, aliens, ship, stats, screen, bullets, sb)


