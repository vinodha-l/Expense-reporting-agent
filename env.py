import random
from models import Action, Observation

class ExpenseEnv:
    def __init__(self):
        # This is our fake "Database" of receipts
        self.data = [
            {"id": "R1", "amount": "150.00", "vendor": "Starbucks"},
            {"id": "R2", "amount": "45.20", "vendor": "Uber"},
            {"id": "R3", "amount": "900.00", "vendor": "Apple Store"}
        ]
        self.current_step = 0
        self.max_steps = 5
        self.score = 0.0

    def reset(self):
        """Starts a new task for the robot."""
        self.current_step = 0
        self.score = 0.0
        print("--- Environment Reset: New Expense Report Started ---")
        
        # We give the robot the first "look" at the task
        return Observation(
            screenshot="https://example.com/receipt_page.png",
            text_content=f"Task: Verify the amount for {self.data[0]['vendor']}",
            reward=0.0,
            done=False
        )

    def step(self, action: Action):
        """The robot takes a turn."""
        self.current_step += 1
        
        # Check if the robot typed the correct amount for Starbucks
        # Logic: If robot types '150.00', they get points!
        if action.command == "type" and action.value == "150.00":
            self.score = 1.0
            message = "Correct! Amount verified."
        else:
            self.score = 0.0
            message = "Incorrect. Try looking at the receipt again."

        # Check if we should stop
        is_finished = self.current_step >= self.max_steps or self.score == 1.0

        return Observation(
            screenshot="https://example.com/current_ui.png",
            text_content=message,
            reward=self.score,
            done=is_finished
        )

# Simple test to see if it works
if __name__ == "__main__":
    env = ExpenseEnv()
    first_look = env.reset()
    print(f"Robot sees: {first_look.text_content}")