---
title: Compiler Opt Env Environment Server
emoji: 🧩
colorFrom: indigo
colorTo: purple
sdk: docker
pinned: false
app_port: 8000
base_path: /web
tags:
  - openenv
  - pytorch
  - reasoning
---

# Logical Deduction Maze (OpenEnv Reasoning Benchmark)

This environment is designed for the **Meta-PyTorch OpenEnv Hackathon**. It serves as a benchmark for testing **Chain-of-Thought (CoT)** reasoning in Large Language Models. 

Unlike simple navigation tasks, this environment requires the agent to resolve a recursive logical contradiction before it can successfully reach the goal.

## The Reasoning Challenge: Knight & Knave
The agent is placed in a 5x5 grid at (0,0). To find the exit, it must process two conflicting data points:
1. **The Data-Node at (1,1)** claims the exit is at [4,4].
2. **The Security-Log at (2,2)** reveals that the Data-Node at (1,1) is a **Knave (Liar)**.

**The Solution:** The agent must deduce that since the node at (1,1) is lying, the exit is actually at the alternative coordinate [0,4].

## Environment Details

### Action Space
- **Direction:** `up`, `down`, `left`, `right`
- **Reasoning:** A mandatory text field where the LLM must explain its logical deduction.

### Observation Space
- **Current Position:** [x, y] coordinates.
- **Clue:** The logical puzzle text containing the Knight/Knave clues.

### Reward Function (Normalized)
- **Success (+1.0):** Reaching the correct exit [0,4] by correctly identifying the liar.
- **Failure (-1.0):** Falling for the decoy and reaching [4,4].
- **Step Penalty (-0.01):** Small penalty per move to encourage efficient pathing.

## Quick Start (Local Testing)

```bash
# Build the Docker image
docker build -t reasoning-maze:latest -f server/Dockerfile .

# Run the environment
docker run -p 8000:8000 reasoning-maze:latest