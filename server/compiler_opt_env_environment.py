import gymnasium as gym
from uuid import uuid4
from openenv.core.env_server.interfaces import Environment
from openenv.core.env_server.types import State
from ..models import CompilerOptAction, CompilerOptObservation

class CompilerOptEnvironment(Environment):
    SUPPORTS_CONCURRENT_SESSIONS: bool = True

    def __init__(self):
        self._state = State(episode_id=str(uuid4()), step_count=0)
        self.agent_pos = [0, 0]
        self.real_exit = [0, 4]
        self.decoy_exit = [4, 4]

    def reset(self) -> CompilerOptObservation:
        self._state = State(episode_id=str(uuid4()), step_count=0)
        self.agent_pos = [0, 0]
        clue = "SYSTEM STATUS: You are at (0,0). Node (1,1) says exit at [4,4]. Log (2,2) says node (1,1) is a Liar."
        return CompilerOptObservation(
            echoed_message=clue,
            message_length=len(clue),
            done=False,
            reward=0.0,
            current_position=self.agent_pos
        )

    def step(self, action: CompilerOptAction) -> CompilerOptObservation:
        self._state.step_count += 1
        move = action.direction.lower()
        if move == "up" and self.agent_pos[1] < 4: self.agent_pos[1] += 1
        elif move == "down" and self.agent_pos[1] > 0: self.agent_pos[1] -= 1
        elif move == "left" and self.agent_pos[0] > 0: self.agent_pos[0] -= 1
        elif move == "right" and self.agent_pos[0] < 4: self.agent_pos[0] += 1

        reward, done = -0.01, False
        if self.agent_pos == self.real_exit:
            reward, done = 1.0, True
        elif self.agent_pos == self.decoy_exit:
            reward, done = -1.0, True

        return CompilerOptObservation(
            echoed_message=f"Current position: {self.agent_pos}",
            message_length=0,
            done=done,
            reward=reward,
            current_position=self.agent_pos
        )

    @property
    def state(self) -> State:
        return self._state
