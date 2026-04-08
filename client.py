import time
from models import CompilerOptAction, CompilerOptObservation
from server.compiler_opt_env_environment import CompilerOptEnvironment

def test_local_env():
    # 1. Initialize the environment locally
    env = CompilerOptEnvironment()
    
    print("--- Resetting Environment ---")
    obs = env.reset()
    print(f"Initial Observation: {obs.echoed_message}")
    print(f"Current Position: {obs.current_position}")

    # 2. Simulate a reasoning step
    print("\n--- Taking a Step ---")
    action = CompilerOptAction(
        direction="up",
        reasoning="I am moving up to explore the grid and find the clues mentioned in the logs."
    )
    
    new_obs, reward, done, truncated, info = env.step(action)
    
    print(f"Status: {new_obs.echoed_message}")
    print(f"New Position: {new_obs.current_position}")
    print(f"Reward Received: {reward}")
    print(f"Is Episode Done? {done}")

if __name__ == "__main__":
    test_local_env()
