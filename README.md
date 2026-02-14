Drag-and-Throw Ball Simulation

A simple physics-based project using Pygame and Pymunk that lets you click, drag, and throw a ball across the screen. The ball’s velocity is determined by the direction and speed of your drag.

Features

Click and hold the mouse to pick up the ball.

Drag in any direction to aim your throw.

Release the mouse to throw the ball, with velocity based on drag distance and time.

Realistic 2D physics using Pymunk.

Requirements

Python 3.10+

Pygame (pip install pygame)

Pymunk (pip install pymunk)

NumPy (pip install numpy)

How to Run

Clone this repository:

git clone <your-repo-url>
cd <repo-folder>


Install dependencies:

pip install pygame pymunk numpy


Run the main script:

python main.py

Controls

Mouse Click & Hold: Grab the ball

Drag: Aim the throw

Release Mouse Button: Throw the ball

How It Works

On MOUSEBUTTONDOWN, the program records the initial mouse position and starts a timer.

While holding the mouse, the timer counts the duration.

On MOUSEBUTTONUP, the final position is recorded, and the velocity vector is calculated:

velocity = (final_position - initial_position) / drag_time


The calculated velocity is assigned to the ball using Pymunk’s physics engine.

Project Structure
/project-folder
│
├─ main.py          # Main game loop and logic
├─ README.md        # This file
└─ assets/          # Optional images, sprites, or sounds

Notes

Pygame’s y-axis points down, so dragging upward produces negative y velocities.

The velocity is automatically a float vector for smooth physics simulation.

Adjust gravity, friction, or mass in Pymunk for different throwing behaviors.

License

This project is free to use for educational purposes.

