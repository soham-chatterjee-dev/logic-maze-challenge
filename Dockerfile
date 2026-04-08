FROM ghcr.io/meta-pytorch/openenv-base:latest
WORKDIR /app
COPY . /app/env
WORKDIR /app/env
RUN pip install gymnasium numpy pydantic openenv-core
ENV PYTHONPATH="/app/env:$PYTHONPATH"
CMD ["sh", "-c", "uvicorn server.app:app --host 0.0.0.0 --port 8000"]
