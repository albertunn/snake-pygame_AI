import random
from tensorflow import keras
import numpy as np
from tensorflow.python.keras import layers

x_i = 3
x_h1 = 16
x_h2 = 32
x_o = 4
pop_size = 50


def calculate_Manhattan_dist(grid, snake,food):
    return

def calculate_direction(snake, food_location):
    
    return random.choice(['UP','DOWN','LEFT','RIGHT'])

def fitness_calculation(chromosome):

    return 

def init_population(pop_size, x_i, x_h1, x_h2, x_o):
    models = []
    for i in range(pop_size): 
        models.append(keras.Sequential())
        models[i].add(keras.layers.Input(shape=(x_i,)))
        models[i].add(keras.layers.Dense(x_h1, activation='relu'))
        models[i].add(keras.layers.Dense(x_h2, activation='relu'))
        models[i].add(keras.layers.Dense(x_o, activation='softmax'))
    #model.layers[0].set_weights(np.array([0.0005,0.0004]))
    return models

def train_pop(pop_size, x_i, x_h1, x_h2, x_o):
    population = init_population(pop_size,x_i, x_h1, x_h2, x_o)
    pop_fitness = []
    for i in range(len(population)):
        pop_fitness.append(fitness_calculation(population[i]))
