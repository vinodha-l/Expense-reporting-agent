import os
from models import Action
from env import ExpenseEnv

def main():
    # 1. Setup the Environment
    env = ExpenseEnv()
    observation = env.reset()
    
    print(f"Goal: {observation.text_content}")

    # 2. The Loop (Simulating the AI)
    for step_num in range(1, 4):
        if observation.done:
            print("--- TASK COMPLETE! ---")
            break

        print(f"\n[Step {step_num}]")
        # Instead of calling a real AI (which costs money/keys), 
        # we will simulate the AI's thought process.
        
        print("Robot is thinking...")
        
        # We 'hardcode' the correct answer for testing
        simulated_answer = "150.00" 
        
        # Tell the environment what we 'decided'
        action_to_take = Action(command="type", target="amount_field", value=simulated_answer)
        
        # This is the 'STEP' the judges want to see
        observation = env.step(action_to_take)
        
        print(f"Robot typed: {simulated_answer}")
        print(f"Result: {observation.text_content}")
        print(f"Reward: {observation.reward}")

if __name__ == "__main__":
    main()