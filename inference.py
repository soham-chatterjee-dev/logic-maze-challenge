from server.compiler_opt_env_environment import CompilerOptEnvironment
from models import CompilerOptAction

def main():
    env = CompilerOptEnvironment()
    obs = env.reset()
    print("Environment reset successful")

if __name__ == "__main__":
    main()
