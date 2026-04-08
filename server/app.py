from openenv.core.env_server.app import OpenEnvServer
from .compiler_opt_env_environment import CompilerOptEnvironment
from ..models import CompilerOptAction, CompilerOptObservation
def env_factory():
    return CompilerOptEnvironment()
app = OpenEnvServer(
    env_class=env_factory,
    action_model=CompilerOptAction,
    observation_model=CompilerOptObservation,
)
if __name__ == "__main__":
    app.run(port=8000)
