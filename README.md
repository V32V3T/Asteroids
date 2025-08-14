# Asteroids Game


A classic Asteroids arcade game implementation built with Python and Pygame. Navigate through space, destroy asteroids, and avoid collisions to survive!
Play it yourself by downloading the main.exe file from : https://drive.google.com/drive/folders/1KTxmI7f_ncApamF9ioS5KLvlTJVWYxzw?usp=sharing

## 🎮 Game Features

- **Classic Asteroids gameplay** - Navigate a triangular spaceship through space
- **Dynamic asteroid spawning** - Asteroids spawn from screen edges at regular intervals
- **Asteroid splitting** - Large asteroids break into smaller pieces when shot
- **Collision detection** - Realistic circular collision detection between all game objects
- **Smooth controls** - Responsive keyboard controls for movement and shooting
- **60 FPS gameplay** - Smooth, consistent frame rate

## 🎯 How to Play

### Controls
- **W** - Move forward
- **S** - Move backward  
- **A** - Rotate left
- **D** - Rotate right
- **SPACE** - Shoot
- **ESC** or **X** - Quit game

### Objective
- Destroy asteroids by shooting them
- Avoid colliding with asteroids
- Large asteroids split into smaller pieces when hit
- Game ends when you collide with an asteroid

## 🚀 Installation & Setup

### Prerequisites
- Python 3.12 or higher
- uv package manager (recommended) or pip

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd bootdevasteroids/asteroods
   ```

2. **Install dependencies using uv**
   ```bash
   uv sync
   ```

3. **Run the game**
   ```bash
   uv run main.py
   ```

### Alternative Installation (using pip)
```bash
pip install pygame==2.6.1
python main.py
```

## 🏗️ Project Structure

```
asteroods/
├── main.py              # Main game loop and initialization
├── constants.py         # Game configuration constants
├── player.py           # Player ship and shot classes
├── asteroid.py         # Asteroid class with splitting logic
├── asteroidfield.py    # Asteroid spawning system
├── circleshape.py      # Base class for circular game objects
├── pyproject.toml      # Project dependencies and metadata
└── README.md           # This file
```

## 🧩 Code Architecture

### Core Classes

#### `CircleShape` (circleshape.py)
Base class for all circular game objects with:
- Position and velocity management
- Collision detection
- Sprite group integration

#### `Player` (player.py)
Player-controlled spaceship with:
- Triangular visual representation
- Movement and rotation controls
- Shooting mechanics with cooldown
- Keyboard input handling

#### `Shot` (player.py)
Projectiles fired by the player:
- Fast-moving circular projectiles
- Automatic cleanup when hitting asteroids

#### `Asteroid` (asteroid.py)
Destructible space rocks with:
- Circular visual representation
- Splitting behavior when hit
- Velocity-based movement

#### `AsteroidField` (asteroidfield.py)
Manages asteroid spawning:
- Edge-based spawning system
- Configurable spawn rates
- Random velocity and size generation

### Game Loop (main.py)
The main game loop handles:
- Event processing (quit, input)
- Rendering all game objects
- Collision detection
- Game state updates
- Frame rate control

## ⚙️ Configuration

Game parameters can be adjusted in `constants.py`:

```python
SCREEN_WIDTH = 1280          # Game window width
SCREEN_HEIGHT = 720          # Game window height
ASTEROID_MIN_RADIUS = 20     # Smallest asteroid size
ASTEROID_KINDS = 3           # Number of asteroid size types
ASTEROID_SPAWN_RATE = 0.8    # Seconds between spawns
PLAYER_RADIUS = 20           # Player ship size
PLAYER_TURN_SPEED = 300      # Rotation speed (degrees/sec)
PLAYER_SPEED = 200           # Movement speed (pixels/sec)
SHOT_RADIUS = 5              # Projectile size
PLAYER_SHOOT_SPEED = 500     # Projectile speed
PLAYER_SHOOT_COOLDOWN = 0.3  # Seconds between shots
```

## 🎨 Technical Details

### Rendering
- All objects are rendered using Pygame's drawing functions
- Player ship is drawn as a white triangle
- Asteroids and shots are drawn as white circles
- Black background for space aesthetic

### Physics
- Position-based movement using Pygame Vector2
- Delta-time based updates for consistent speed across frame rates
- Circular collision detection using distance calculations

### Performance
- Sprite groups for efficient object management
- 60 FPS target with frame rate limiting
- Automatic cleanup of destroyed objects

## 🐛 Troubleshooting

### Common Issues

1. **Import errors**: Make sure you're running from the correct directory
2. **Display issues**: Ensure your system supports the specified resolution
3. **Performance issues**: Close other applications to free up resources

### Debug Mode
Add debug prints to track game state:
```python
print(f"Player position: {player.position}")
print(f"Asteroid count: {len(asteroids)}")
```

## 🤝 Contributing

Feel free to contribute improvements:
- Bug fixes
- New features
- Performance optimizations
- Code documentation

## 📄 License

This project is open source. Feel free to use and modify as needed.

## 🎯 Future Enhancements

Potential improvements:
- Sound effects and music
- Score system
- Multiple lives
- Power-ups
- Different asteroid types
- Particle effects
- High score tracking
- Menu system

---

**Enjoy playing Asteroids!** 🚀💫
