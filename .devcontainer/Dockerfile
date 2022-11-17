FROM mcr.microsoft.com/vscode/devcontainers/python:0-3.11

RUN apt-get update && \
    apt-get install -y festival && \
    rm -rf /var/lib/apt/lists/* && \
    pipx install poetry

USER vscode
