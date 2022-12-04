class Elf:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __str__(self):
        s = f"Elf name: {self.name}\nCalories: {self.calories}"
        return s
    
    def calculate_total_calories(self):
        return sum(self.calories)
    