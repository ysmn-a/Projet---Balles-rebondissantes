import pygame
import random
import sys
import time

# Initialisation de la fenêtre pygame
LARGEUR = 640
HAUTEUR = 480

pygame.display.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
fenetre.fill([255, 255, 255])

class Balle:
    def __init__(self, rayon, couleur):
        self.rayon = rayon
        self.x = random.randint(rayon, LARGEUR - rayon)
        self.y = random.randint(rayon, HAUTEUR - rayon)
        self.couleur = couleur
        self.dx = random.choice([-4, -3, 3, 4])
        self.dy = random.choice([-4, -3, 3, 4])

    def dessiner(self, fenetre):
        pygame.draw.circle(fenetre, self.couleur, (self.x, self.y), self.rayon)

    def bouger(self):
        self.x += self.dx
        self.y += self.dy

    def rebondir(self):
        if self.x - self.rayon < 0 or self.x + self.rayon > LARGEUR:
            self.dx = -self.dx
        if self.y - self.rayon < 0 or self.y + self.rayon > HAUTEUR:
            self.dy = -self.dy

# Création de 10 balles avec des couleurs pastel différentes 
mes_balles = [
    Balle(20,(255, 192, 203)),  # Rose pastel
    Balle(20,(255, 165, 0)),     # Orange pastel
    Balle(20,(144, 238, 144)),   # Vert pastel
    Balle(20, (221, 160, 221)),  # Violet pastel
    Balle(20, (255, 182, 193)),  # Saumon pastel
    Balle(20, (255, 228, 181)),  # Jaune pastel
    Balle(20, (175, 238, 238)),  # Turquoise pastel
    Balle(20, (221, 160, 221)),  # Lavande pastel
    Balle(20, (240, 128, 128)),  # Corail pastel
    Balle(20, (175, 238, 238))   # Cyan pastel
]

# Boucle infinie pour afficher la fenêtre et son contenu
continuer = True 
while continuer:
    # couleur du fond réinitialisée
    fenetre.fill([255, 255, 255]) # Blanc

    # Affichage et animation des balles
    for balle in mes_balles:
        balle.dessiner(fenetre)
        balle.bouger()
        balle.rebondir()

    # mise à jour de la fenêtre 
    pygame.display.update()

    # routine pour pouvoir quitter la boucle while
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False 

    # temps de pause
    time.sleep(0.04)

# Fermeture de la fenêtre 
pygame.quit()
sys.exit()
