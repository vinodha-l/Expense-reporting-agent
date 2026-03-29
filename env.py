import json
from models import Action, Observation

class ExpenseEnv:
    def __init__(self):
        self.data = [
            {"id": "T1", "amount": "150.00", "vendor": "Starbucks", "diff": "easy"},
            {"id": "T2", "amount": "45.20", "vendor": "Uber", "diff": "medium"},
            {"id": "T3", "amount": "900.00", "vendor": "Apple Store", "diff": "hard"}
        ]
        self.current_task_idx = 0
        self.done = False

    def reset(self):
        self.current_task_idx = 0
        self.done = False
        task = self.data[self.current_task_idx]
        return Observation(text_content=f"Verify the amount for {task['vendor']}", done=False, reward=0.0)

    def step(self, action: Action):
        task = self.data[self.current_task_idx]
        if action.value == task['amount']:
            reward = 1.0
            self.done = True
            return Observation(text_content="Correct! Amount verified.", done=True, reward=reward)
        else:
            return Observation(text_content="Incorrect amount.", done=False, reward=0.0)
