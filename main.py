import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class RobotSimulation:
    def __init__(self, arena_size=(10, 10), step_size=0.4, max_rotation=np.pi):
        self.arena_size = arena_size
        self.step_size = step_size
        self.max_rotation = max_rotation
        self.robot_pos = np.array(arena_size) / 2  
        self.robot_heading = np.random.uniform(0, 2*np.pi) 
        self.path = [self.robot_pos.copy()]

    def step(self):
        # Move the robot forward
        new_pos = self.robot_pos + self.step_size * np.array([np.cos(self.robot_heading), np.sin(self.robot_heading)])
        
        # Check for collision with boundaries
        if not (0 <= new_pos[0] < self.arena_size[0]) or not (0 <= new_pos[1] < self.arena_size[1]):
            # Collision detected, rotate the robot randomly
            rotation = np.random.uniform(-self.max_rotation, self.max_rotation)
            self.robot_heading += rotation
        else:
            # No collision, update position
            self.robot_pos = new_pos
        
        # Add current position to the path
        self.path.append(self.robot_pos.copy())

    def simulate(self, num_steps):
        for _ in range(num_steps):
            self.step()

def update(frame):
    sim.step()
    x, y = zip(*sim.path)
    robot.set_data(x, y)
    return robot,

def start_animation(event):
    ani.event_source.start()

def init():
    x, y = zip(*sim.path)
    robot.set_data(x, y)
    return robot,

if __name__ == "__main__":
    sim = RobotSimulation()
    
    fig, ax = plt.subplots()
    ax.set_xlim(0, sim.arena_size[0])
    ax.set_ylim(0, sim.arena_size[1])
    ax.set_title('Brownian Motion- Python Challenge')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    robot, = ax.plot([], [], marker='o')
    
    ani = FuncAnimation(fig, update, frames=range(1000), init_func=init, blit=True, interval=0)
    plt.show()