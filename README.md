# file-transfer-cli

A simple local host file transfer cli written in python.

## Usage

1. Run `python server.py [PORT]`.
2. Run `python client.py <hostname> <port> <put [filename]|get [filename]|list>`

## Commands

- `put`: Send file over the port.
- `get`: Requests a file from the server.
- `list`: Lists files on the server.
