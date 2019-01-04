import pygame
import numpy as np

#One pixel per billion meters
default_pix_per_m = 10**9

class Planet():
    def __init__(self, mass = 0, radius = 0, position = (0,0), color=(0,0,0),speed = 0 , velocity = 0,pos = (0,0), *args):
        self.mass = mass
        self.radius = radius
        self.position = position
        self.color = color
        self.speed = speed
        self.velocity = velocity
        self.pos = self.position


    def initial_velocity(self, sun, real_time_per_frame, ratio = 1.0):
        """
        * Sets velocity direction perpendicular to position vector from the sun
        * i.e Velocity unit vector = direction
        * Velocity magnitude = speed
        """
        sun_vec = np.array(sun.position)
        self_vec = np.array(self.position)
        vector = self_vec-sun_vec
        perp_matrix = [[0,-1], [1,0]]
        direction = np.dot(perp_matrix,vector)/np.sqrt(np.sum(vector**2))
        self.velocity = self.speed*direction/ratio

    def update_vel_pos(self,real_time_per_frame,g_const, *mass, pix_dist_ratio = 1.0, dist_rat=default_pix_per_m):
       """
       *Updates the velocity and position of the planets using their velocities
       * Newtons Equations F=GMm/(r^2), F=ma
       * acceleration direction is towards mass pulling the planet
       """
       for i in mass:
          disp =  np.array(i.pos)- np.array(self.pos)
          acc_direc = disp/np.sqrt(np.sum(disp**2))
          r_squared = (np.linalg.norm(disp)*dist_rat)**2
          del_vel = (real_time_per_frame*g_const*i.mass*acc_direc)/(r_squared*pix_dist_ratio)
       self.velocity = (self.velocity + del_vel)
       add = real_time_per_frame*self.velocity/(default_pix_per_m)
       self.pos = self.pos + add
       self.position = self.pos.astype(np.int64)
