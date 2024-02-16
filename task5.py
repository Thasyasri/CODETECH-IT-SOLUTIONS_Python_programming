import tkinter as tk
from tkinter import messagebox
import time

class AdventureGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("The Lost Temple Adventure")
        self.geometry("800x600")
        self.current_scene = None
        self.inventory = []

        # Define scenes
        self.scenes = {
            "entrance": {
                "text": "Welcome to The Lost Temple!\nYou find yourself at the entrance of an ancient temple.\nAs you step forward, the heavy stone doors creak open, revealing a dimly lit corridor.\nYour heart races with excitement and trepidation.\nWhat will you do?",
                "options": [("Enter the temple cautiously", "corridor"), ("Explore the surrounding jungle", "jungle")]
            },
            "jungle": {
                "text": "You decide to explore the surrounding jungle.\nYou wander through the dense foliage, but find nothing of interest.\nFeeling disappointed, you return to the entrance of the temple.",
                "options": [("Enter the temple", "corridor"), ("Quit", "quit")]
            },
            "corridor": {
                "text": "You enter the temple and find yourself in a dimly lit corridor.\nAs you venture deeper, you come across a fork in the path.\nWhich path will you choose?",
                "options": [("Take the left path", "left_path"), ("Take the right path", "right_path")]
            },
            "left_path": {
                "text": "You choose the left path and proceed cautiously.\nYou encounter a locked door. It seems you need a key to proceed.\nWhat will you do?",
                "options": [("Search for the key", "search_key"), ("Return to the corridor", "corridor")]
            },
            "search_key": {
                "text": "You search the area and find the key hidden under a pile of rubble.\nYou unlock the door and continue deeper into the temple.\nCongratulations! You've found a valuable artifact and completed your quest!",
                "options": [("Restart", "entrance"), ("Quit", "quit")]
            },
            "right_path": {
                "text": "You choose the right path and proceed cautiously.\nSuddenly, you trigger a trap and fall into a dark pit.\nWhat will you do?",
                "options": [("Try to climb out of the pit", "climb_out"), ("Look for another way out", "another_way_out")]
            },
            "climb_out": {
                "text": "You attempt to climb out of the pit, but the walls are too slippery.\nYou notice a narrow ledge along the side of the pit and manage to escape.\nYou continue your journey through the temple.\nCongratulations! You've overcome the obstacle and completed your quest!",
                "options": [("Restart", "entrance"), ("Quit", "quit")]
            },
            "another_way_out": {
                "text": "You explore the pit and discover a hidden passage.\nYou follow the passage and find yourself back in the temple corridor.\nYou continue your journey through the temple.\nCongratulations! You've found a valuable artifact and completed your quest!",
                "options": [("Restart", "entrance"), ("Quit", "quit")]
            }
        }

        # Start the game
        self.load_scene("entrance")

    def load_scene(self, scene_name):
        self.clear_widgets()

        # Update current scene
        self.current_scene = scene_name

        # Display scene text
        scene_info = self.scenes[scene_name]
        text = scene_info["text"]
        self.label = tk.Label(self, text=text, wraplength=600)
        self.label.pack()

        # Display scene options
        for option_text, next_scene in scene_info["options"]:
            button = tk.Button(self, text=option_text, command=lambda next_scene=next_scene: self.load_scene(next_scene))
            button.pack()

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = AdventureGame()
    app.mainloop()
