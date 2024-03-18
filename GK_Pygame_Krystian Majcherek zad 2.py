import pygame

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna
window_size = (600, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Zielony prostokąt z trójkątami")

# Kolory
black = (0, 0, 0)
green = (0, 255, 0)

# Zmienna do kontroli pętli gry
running = True

# Główna pętla gry
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(black)  # Czyszczenie ekranu

    # Wymiary i położenie prostokąta
    rect_width = window_size[0]
    rect_height = 200
    rect_x = 0
    rect_y = (window_size[1] / 2) - (rect_height / 2)

    # Rysowanie prostokąta
    pygame.draw.rect(window, green, (rect_x, rect_y, rect_width, rect_height))

    # Wymiary i położenie trójkątów
    triangle_height = rect_height
    triangle_base = rect_width

    # Rysowanie lewego trójkąta (o 90 stopni w prawo)
    left_triangle = [(rect_x, rect_y + rect_height),
                     (rect_x + triangle_base / 2, rect_y + rect_height),
                     (rect_x, rect_y + rect_height + triangle_height)]
    pygame.draw.polygon(window, green, left_triangle)

    # Rysowanie prawego trójkąta (o 90 stopni w lewo)
    right_triangle = [(rect_x + rect_width, rect_y + rect_height),
                      (rect_x + rect_width - triangle_base / 2, rect_y + rect_height),
                      (rect_x + rect_width, rect_y + rect_height + triangle_height)]
    pygame.draw.polygon(window, green, right_triangle)

    pygame.display.update()  # Odświeżenie ekranu

pygame.quit()

