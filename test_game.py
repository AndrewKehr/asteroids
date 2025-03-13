import pytest  # type: ignore
import time
import os
from unittest.mock import patch
from circleshape import CircleShape

### **TEST 1: Game Startup**
def test_game_launch():
    """Ensure the game starts without crashing."""
    process = os.system("python3 main.py &")  # Run in background
    time.sleep(10)  # Allow the game to start
    assert process == 0, "Game failed to launch"

### **TEST 2: Collision Detection (Bullets vs Asteroids)**
def test_collision():
    """Ensure bullets correctly hit asteroids."""
    asteroid = {"x": 100, "y": 100, "radius": 20}
    bullet = {"x": 105, "y": 105, "radius": 5}
    
    assert asteroid.collision(bullet) == True, "Collision detection failed"

### **TEST 3: Performance Check (FPS)**
def test_fps():
    """Check if FPS is stable above 30."""
    fps_log = "fps_log.txt"
    
    os.system("python3 main.py > " + fps_log + " &")  # Run game
    time.sleep(30)  # Let it run
    
    with open(fps_log, "r") as file:
        lines = file.readlines()
        fps_values = [float(line.split()[-1]) for line in lines if "Current FPS" in line]

    assert all(fps >= 30 for fps in fps_values), "FPS dropped below 30!"
