# gui.py or main.py
from tkinter import ttk
import tkinter as tk
from predictor import predict_match
from api_handler import get_teams

class PredictorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("College Football Predictor")

        # Get teams from API (cached)
        teams = get_teams()

        # Dropdowns
        self.team1_var = tk.StringVar()
        self.team2_var = tk.StringVar()

        ttk.Label(root, text="Team 1:").grid(row=0, column=0)
        self.team1_dropdown = ttk.Combobox(root, textvariable=self.team1_var, values=teams, width=30)
        self.team1_dropdown.grid(row=0, column=1)

        ttk.Label(root, text="Team 2:").grid(row=1, column=0)
        self.team2_dropdown = ttk.Combobox(root, textvariable=self.team2_var, values=teams, width=30)
        self.team2_dropdown.grid(row=1, column=1)

        # Predict button
        predict_button = ttk.Button(root, text="Predict", command=self.run_prediction)
        predict_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Output
        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2)

    def run_prediction(self):
        team1 = self.team1_var.get()
        team2 = self.team2_var.get()
        if not team1 or not team2:
            self.result_label.config(text="Please select both teams.")
            return
        result = predict_match(team1, team2)
        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    app = PredictorApp(root)
    root.mainloop()
