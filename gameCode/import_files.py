from os import walk
import pygame


def import_folder(path):
    surface_list = []
    for dontcare, stilldontcare, image_file in walk(path):
        for image in image_file:
            full_path = f"{path}/{image}"
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)

    return surface_list

