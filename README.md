Deadline: The Infinite NPC (Gemini Hackathon Entry)
The train is moving at 110km/h. The bomb is active. And the bomber isn't following a script."**
Deadline is a survival visual novel built with **Ren'Py** where the antagonist is powered by Google's **Gemini 1.5 Flash API**. Unlike traditional games with pre-written dialogue trees, this NPC ("Sarkar") listens to your specific arguments, analyzes your logic in real-time, and decides whether to spare you or detonate the train.

Play the Game
Download the playable build here:
https://drive.google.com/drive/folders/1aWGvm4HhfralsRaA3y-78jLDSzO8C9vy?usp=sharing
(Instructions: Download the zip file, extract it, and run `Deadline.exe` on Windows or `Deadline.app` on Mac.)

The "Infinite NPC" Mechanic
Most visual novels use "If/Else" logic. *Deadline* uses a **Large Language Model (LLM)** as the game's brain.

How it works:
1. Real-Time Context:** The game feeds the AI current data (Train Speed: 110km/h, Vibration Level: High, Fear Level: Panic).
2. Dynamic Dialogue:** When you type a message to Sarkar, Gemini 1.5 Flash generates a response based on his "Terrified Bomber" persona.
3. Logic-Driven Endings:
The "Win" State:** If you use logic (e.g., mentioning "voltage," "wiring," or "stabilization") to calm him down, the AI triggers the `chapter_complete` label.
The "Fail" State:** If you are aggressive or rude, the AI triggers the `bad_ending` label (Detonation).

Tech Stack
Engine:[Ren'Py 8.3](https://www.renpy.org/) (Python-based Visual Novel Engine)
AI Model:[Google Gemini 1.5 Flash](https://deepmind.google/technologies/gemini/flash/) (via Google Generative AI API)
Integration:Python `urllib` & `json` for direct API calls.
Visuals:Custom parallax backgrounds and shake effects to simulate the moving train.

Installation (For Developers)
If you want to run the source code yourself:

1.  Clone this repository.
2.  Download the **Ren'Py SDK**.
3.  Open the project in Ren'Py.
4.  **Important:** You must add your own API Key.
    * Open `game/script.rpy`.
    * Find the line: `API_KEY = "PLACEHOLDER"`
    * Replace it with your actual Google Gemini API Key.
5.  Click **"Launch Project"**.

Hackathon Details
Submitted for the Gemini API Developer Competition.
Theme:Redefining NPCs with Generative AI.
Goal:To prove that LLMs can create high-stakes, consistent gameplay loops without breaking character.

Created by Curious-DevCode (Aditya Kulkarni0
Angad Dudhekar
Sanmay Magar
