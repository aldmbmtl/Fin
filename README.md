<br />
<p align="center">
    <img src="https://avatars.githubusercontent.com/u/9037579?v=4"/>
    <h3 align="center">Fin</h3>
    <p align="center">
        Simple CLI chat bot that can interact with your source code.
    </p>
</p>

## Dependencies

- [Ollama API](https://github.com/ollama/ollama/tree/main)

## Installation

### Prerequisites

- [Python 3.9+](https://www.python.org/)
- [GNU Make](https://www.gnu.org/software/make/)
- [uv](https://github.com/astral-sh/uv)

### Setup

```bash
git clone https://github.com/aldmbmtl/Fin.git
cd Fin
make setup
make install
```

### Configuration

Fin uses a configuration file to store the settings for the Ollama API and the project. Much like a `.gitignore` or 
any other kind of `dot` file, you would create a `.fin.yaml` file in the root of your project.

```yaml
llm:
  server: https://ollama.example.com
  model: llama2

project:
  languages:
    - python
    - javascript
```

This allows you to specify what languages are used in your project so Fin can better help you. You can also specify the
Ollama server and model to use. For reference, you can look at the .fin.yaml.sample file.

## Usage

You have 2 options

* Try out fin directly off the source
* Install fin more permanently in your $HOME/.local/bin

To try out fin directly off the source, you can run the following command:
```bash
make run
```

This will launch the fin chat bot and you can start chatting with it.

To install fin more permanently in your $HOME/.local/bin, you can run the following command:
```bash
make install-cli
```

From here, you can type `fin` in your terminal and start chatting with the bot.
