# Celestial Body Motion Simulation with Pygame
#
# Learning Objective:
# This tutorial will teach you how to simulate basic celestial body motion,
# focusing on gravitational attraction, and visualize it using the Pygame library.
# We will cover:
# 1. Representing celestial bodies with properties like mass, position, and velocity.
# 2. Calculating the gravitational force between two bodies.
# 3. Updating a body's velocity and position based on calculated forces.
# 4. Using Pygame to draw these bodies and animate their movement.

import pygame
import math

# --- Constants ---
# These are fixed values that won't change during the simulation.
WIDTH, HEIGHT = 800, 600  # Screen dimensions for our Pygame window.
WHITE = (255, 255, 255)   # RGB color tuple for white.
BLACK = (0, 0, 0)         # RGB color tuple for black.
GRAVITATIONAL_CONSTANT = 0.1 # A scaled-down gravitational constant for easier simulation.
                              # Real G is very small, so we use a larger number for visible effects.
                                # This is a simplification for educational purposes.

# --- Celestial Body Class ---
# This class will represent each object in our simulation (planets, stars, etc.).
class CelestialBody:
    def __init__(self, name, mass, x, y, vx, vy, radius, color):
        # 'name': A string identifier for the body (e.g., "Sun", "Earth").
        self.name = name
        # 'mass': The mass of the celestial body. More mass means stronger gravity.
        self.mass = mass
        # 'x', 'y': The current position of the body on the screen (in pixels).
        self.x = x
        self.y = y
        # 'vx', 'vy': The current velocity of the body in the x and y directions.
        # Velocity determines how the position changes each frame.
        self.vx = vx
        self.vy = vy
        # 'radius': The visual size of the body on the screen.
        self.radius = radius
        # 'color': The color to draw the body in Pygame.
        self.color = color

    def draw(self, screen):
        # Draw the celestial body as a circle on the Pygame screen.
        # We cast position to int because Pygame drawing functions expect integers.
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def calculate_gravity(self, other_body):
        # This method calculates the gravitational force exerted by 'other_body' on 'self'.
        # The core of our simulation is Newton's Law of Universal Gravitation.

        # Calculate the difference in x and y coordinates between this body and the other body.
        dx = other_body.x - self.x
        dy = other_body.y - self.y

        # Calculate the distance between the two bodies using the Pythagorean theorem.
        # We add a small epsilon (1e-3) to avoid division by zero if bodies are at the exact same position.
        distance = math.sqrt(dx**2 + dy**2) + 1e-3

        # Calculate the magnitude of the gravitational force.
        # Formula: F = G * (m1 * m2) / r^2
        # G: Gravitational Constant
        # m1: Mass of 'self'
        # m2: Mass of 'other_body'
        # r: Distance between them
        force_magnitude = (GRAVITATIONAL_CONSTANT * self.mass * other_body.mass) / (distance**2)

        # Calculate the direction of the force.
        # We use the normalized vector (dx/distance, dy/distance) to represent the direction.
        # This gives us a unit vector pointing from 'self' towards 'other_body'.
        force_x = force_magnitude * (dx / distance)
        force_y = force_magnitude * (dy / distance)

        # The force exerted on 'self' by 'other_body' is in the direction of 'other_body'.
        return force_x, force_y

    def update_velocity(self, total_force_x, total_force_y, dt):
        # Update the velocity of this body based on the total force acting on it.
        # This uses Newton's Second Law of Motion: F = ma, so a = F/m.
        # The acceleration is the change in velocity per unit time (dt).
        # Therefore, change in velocity (dv) = acceleration * dt = (F/m) * dt.

        # Calculate acceleration in x and y directions.
        acceleration_x = total_force_x / self.mass
        acceleration_y = total_force_y / self.mass

        # Update velocity by adding the change in velocity.
        self.vx += acceleration_x * dt
        self.vy += acceleration_y * dt

    def update_position(self, dt):
        # Update the position of this body based on its current velocity.
        # Position change = velocity * time (dt).
        self.x += self.vx * dt
        self.y += self.vy * dt

# --- Simulation Setup ---
def run_simulation():
    # Initialize Pygame. This is required to use Pygame functionalities.
    pygame.init()

    # Create the game window (screen).
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # Set the title of the window.
    pygame.display.set_caption("Celestial Body Simulation")

    # Create instances of our celestial bodies.
    # Parameters: name, mass, initial_x, initial_y, initial_vx, initial_vy, radius, color
    sun = CelestialBody("Sun", 10000, WIDTH // 2, HEIGHT // 2, 0, 0, 20, (255, 255, 0)) # Yellow
    earth = CelestialBody("Earth", 100, 300, HEIGHT // 2, 0, 0.5, 8, (0, 0, 255))     # Blue
    moon = CelestialBody("Moon", 1, earth.x + 40, earth.y, 0, 1.5, 3, (150, 150, 150)) # Grey

    # List to hold all celestial bodies in the simulation.
    bodies = [sun, earth, moon]

    # Time step for the simulation. A smaller dt leads to more accuracy but slower simulation.
    # A larger dt can lead to unstable simulations.
    dt = 1.0

    # Game loop: This loop runs continuously until the user quits.
    running = True
    while running:
        # Event handling: Process all events that have occurred since the last frame.
        for event in pygame.event.get():
            # If the user clicks the close button, set running to False to exit the loop.
            if event.type == pygame.QUIT:
                running = False

        # --- Physics Update ---
        # For each body, calculate the total gravitational force acting on it.
        for body in bodies:
            total_force_x = 0
            total_force_y = 0
            # Iterate through all other bodies to sum up their gravitational influence.
            for other_body in bodies:
                # A body doesn't exert gravity on itself.
                if body != other_body:
                    # Calculate the force exerted by 'other_body' on 'body'.
                    force_x, force_y = body.calculate_gravity(other_body)
                    # Add this force to the total force acting on 'body'.
                    total_force_x += force_x
                    total_force_y += force_y

            # After summing all forces, update the velocity of the body.
            body.update_velocity(total_force_x, total_force_y, dt)
            # Then, update the position of the body based on its new velocity.
            body.update_position(dt)

        # --- Drawing ---
        # Fill the screen with a background color (black in this case) to clear the previous frame.
        screen.fill(BLACK)

        # Draw each celestial body on the screen.
        for body in bodies:
            body.draw(screen)

        # Update the display to show everything that has been drawn.
        pygame.display.flip()

    # Once the game loop ends, quit Pygame.
    pygame.quit()

# --- Example Usage ---
# This block ensures that run_simulation() is called only when the script is executed directly.
if __name__ == "__main__":
    run_simulation()