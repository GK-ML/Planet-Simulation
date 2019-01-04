import game_gui as gg
import space
import pygame
import numpy as np
#screen = gg.Display()

#gravitational constant using kilometers and 10^24kg
grav_const = 6.6740800*(10**(-11))
unscaled_pix_per_m = 10**9
#Planet Colors
red_mars = (255, 0, 0)
white_m = (255,255,255)
orange = (255,245,0)
orange_v = (230,200, 0)
grey_m = (192,192,192)
blue = (0,0,150)
brown_jupiter = (180, 92, 61)
gold_saturn = (204,170,0)
uranus_c = (103,155,124)
neptune_c = (113,173,174)

#Some planets neet distance rescaling in order to fit into the simulation
#Default scale is 1 pix = 10^9m
jup_pix_scale = 3.0
sat_pix_scale = 4.0
ura_pix_scale = 6.0
nep_pix_scale = 8.5
#scaling of meters per pixel
jup_dist_scale = jup_pix_scale*unscaled_pix_per_m
sat_dist_scale = sat_pix_scale*unscaled_pix_per_m
ura_dist_scale = ura_pix_scale*unscaled_pix_per_m
nep_dist_scale = nep_pix_scale*unscaled_pix_per_m
#display size in pixels
width = 1200
height = 700

#Planet_Mass's
sun_mass = 1.988435*(10**30)
mercury_mass = 0.330*(10**24)
venus_mass = 4.87*(10**24)
earth_mass = 5.97*(10**24)
mars_mass = 0.642*(10**24)
jupiter_mass =  1898*(10**24)
saturn_mass = 568*(10**24)
uranus_mass = 86.8*(10**24)
neptune_mass = 102*(10**24)

#Planet postions in display
sun_x = int(width/2)
sun_y = int(height/2)
earth_x = int((width/2) + (149.6))
earth_y = int((height/2))
mars_x = int((width/2) + (227.9))
mars_y= int((height/2))
merc_x = int((width/2) + 57.9)
merc_y = int((height/2))
venus_x = int((width/2) + 108.2)
venus_y = int((height/2))
jupiter_x = int((width/2) + (778.6/jup_pix_scale))
jupiter_y = int(height/2)
saturn_x = int((width/2) + (1433.5/sat_pix_scale))
saturn_y = int(height/2)
uranus_x = int((width/2) + (2872.5/ura_pix_scale))
uranus_y = int(height/2)
neptune_x = int((width/2) + (4495.1/nep_pix_scale))
neptune_y = int(height/2)

fps = 30
T_earth = 365.2
T_real = (T_earth/40.)*60*60*24

#speeds m/s
earth_m_per_sec = 29800
merc_m_per_sec = 47400
venus_m_per_sec = 35000
mars_m_per_sec = 24100
jupiter_m_per_sec = 13100
saturn_m_per_sec = 9700
uranus_m_per_sec = 6800
neptune_m_per_sec = 5400


#real time passed for one second of running the simulation real_to_sim_t
real_to_sim_time = T_real
real_time_per_frame = real_to_sim_time/fps

pygame.display.init()
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('Caption')

mercury = space.Planet(mercury_mass, 4, (merc_x,merc_y),grey_m, speed=merc_m_per_sec)
venus = space.Planet(venus_mass, 9, (venus_x,venus_y), orange_v, speed = venus_m_per_sec)
earth = space.Planet(earth_mass , 10, (earth_x,earth_y),blue,speed = earth_m_per_sec)
sun = space.Planet(sun_mass , 40, (sun_x,sun_y), color = orange)
mars = space.Planet(mars_mass , 5, (mars_x,mars_y),color = red_mars, speed = mars_m_per_sec )
jupiter = space.Planet(jupiter_mass,15, (jupiter_x,jupiter_y), color = brown_jupiter, speed = jupiter_m_per_sec)
saturn = space.Planet(saturn_mass, 13,(saturn_x, saturn_y), color = gold_saturn, speed= saturn_m_per_sec)
uranus = space.Planet(uranus_mass , 6,(uranus_x,uranus_y),color =  uranus_c, speed = uranus_m_per_sec)
neptune = space.Planet(neptune_mass, 6, (neptune_x,neptune_y), color = neptune_c, speed = neptune_m_per_sec )

earth.initial_velocity(sun, real_time_per_frame)
mercury.initial_velocity(sun, real_time_per_frame)
venus.initial_velocity(sun, real_time_per_frame)
mars.initial_velocity(sun, real_time_per_frame)
jupiter.initial_velocity(sun,real_time_per_frame, ratio = jup_pix_scale)
saturn.initial_velocity(sun, real_time_per_frame, ratio = sat_pix_scale)
uranus.initial_velocity(sun, real_time_per_frame, ratio = ura_pix_scale)
neptune.initial_velocity(sun, real_time_per_frame, ratio = nep_pix_scale)

loop = False

while not loop:
    gameDisplay.fill((0, 0, 0))
    #draws planets to screen
    venus_d = pygame.draw.circle(gameDisplay, venus.color, venus.position, venus.radius,0)
    earth_d = pygame.draw.circle(gameDisplay, earth.color, earth.position, earth.radius, 0)
    mercury_d = pygame.draw.circle(gameDisplay, mercury.color, mercury.position, mercury.radius, 0)
    sun_d = pygame.draw.circle(gameDisplay, sun.color,sun.position, sun.radius, 0)
    mars_d = pygame.draw.circle(gameDisplay, mars.color, mars.position, mars.radius, 0)
    jupiter_d = pygame.draw.circle(gameDisplay,jupiter.color,jupiter.position, jupiter.radius,0)
    saturn_d = pygame.draw.circle(gameDisplay,saturn.color,saturn.position, saturn.radius,0)
    uranus_d = pygame.draw.circle(gameDisplay, uranus_c, uranus.position, uranus.radius,0)
    neptune_d = pygame.draw.circle(gameDisplay, neptune_c, neptune.position, neptune.radius, 0 )

    #update planet attributes
    mars.update_vel_pos(real_time_per_frame,grav_const,sun)
    earth.update_vel_pos(real_time_per_frame,grav_const, sun)
    mercury.update_vel_pos(real_time_per_frame, grav_const, sun)
    venus.update_vel_pos(real_time_per_frame,grav_const, sun)
    jupiter.update_vel_pos(real_time_per_frame, grav_const, sun, pix_dist_ratio = jup_pix_scale, dist_rat = jup_dist_scale)
    saturn.update_vel_pos(real_time_per_frame, grav_const, sun, pix_dist_ratio = sat_pix_scale, dist_rat = sat_dist_scale )
    uranus.update_vel_pos(real_time_per_frame, grav_const, sun, pix_dist_ratio = ura_pix_scale, dist_rat = ura_dist_scale)
    neptune.update_vel_pos(real_time_per_frame, grav_const, sun, pix_dist_ratio = nep_pix_scale, dist_rat = nep_dist_scale)
    pygame.display.update()

    #loop = True
