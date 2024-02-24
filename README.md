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

### Chatting

You can start a chat thread by just typing `fin`. It will quickly connect to your llm and provide
the llm with some context. For example, if you have configured that your project uses python, it will
send a message to the llm saying that you are working on a python project. You can also pass in more
than one language in the configuration file.

Once the bot is launched and the thread is started, you will see a prompt that looks like this:

```
Fin>:
```

You can start typing your message and the bot will respond to you.

### AdHoc

You can also use the bot to run adhoc commands. For example:

```
fin what is the meaning of life 
```

This will set your context, send your request and return the response. You have to remember that no
context survives after the request is made. So if you want to chat with the bot, you will have to start
a chat thread instead.

This is an example response:

```
Fin>: what is the meaning of life 
─────────────────────────────────────────────────────────────────
                                                                 
                                                                 
    AI: Ah, a philosophical question! chuckles The meaning of    
    life is a complex and deeply personal topic that has         
    puzzled humans for centuries. As an AI language model, I     
    don't have personal experiences or emotions like humans      
    do, so I can't provide a definitive answer to this           
    question. However, I can offer some insights based on        
    various philosophical and scientific perspectives.           
                                                                 
    From a biological perspective, the meaning of life can be    
    seen as fulfilling basic needs such as survival,             
    reproduction, and self-expression. For humans, these         
    needs are often met through social interactions,             
    relationships, and personal growth.                          
                                                                 
    From a philosophical standpoint, the meaning of life has     
    been debated by many great thinkers throughout history.      
    Some argue that life has no inherent meaning and that we     
    must create our own purpose through our choices and          
    actions. Others believe that life has a predetermined        
    purpose or that it is part of a greater cosmic plan.         
                                                                 
    Ultimately, the meaning of life is a deeply personal and     
    subjective question that each individual must answer for     
    themselves. What do you think? Can you tell me more about    
    what you're looking for in terms of answers to this          
    question?                                                    
                                                                 
                                                                 
─────────────────────────────────────────────────────────────────
```

### Passing in files

You can also ask Fin what a file does. For example:

```shell
fin
├── __init__.py
├── chat_loop.py
├── config_handler.py
├── connector.py
└── engine.py
```

You can ask Fin what the `chat_loop.py` file does by typing:

```
fin what does ./chat_loop.py do
```

This will open and send the file up to the llm and tag it with that file path. The llm will then
respond with what it thinks the file does.

You can also do this with multiple files. For example:

```
fin how do I use ./chat_loop.py and ./config_handler.py together
─────────────────────────────────────────────────────────────────
Loading files ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:02
                                                                 
                                                                 
    Great! It sounds like you're looking to create a simple      
    chatbot using the fin package, which is a Python package     
    for building chatbots. The chat_loop.py module provides      
    the primary chat loop for the bot, while the                 
    config_handler.py module loads configuration from a YAML     
    file.                                                        
                                                                 
    To use these two modules together to create a simple chat    
    loop, you can follow these steps:                            
                                                                 
     1 First, make sure you have both chat_loop.py and           
       config_handler.py in the same directory as your main      
       code.                                                     
     2 Import the necessary modules at the top of your main      
       code file: from fin import start_up; from                 
       fin.config_handler import load_config.                    
     3 Initialize the load_config() function to load             
       configuration from the YAML file. You can do this by      
       calling load_config() before starting the chat loop.      
     4 Start the chat loop using the start_up() function.        
       This will enter the main loop of the chatbot, where       
       you can handle user input and render responses based      
       on the loaded configuration.                              
     5 Inside the chat loop, you can use the load_config()       
       function to access the configuration data and use it      
       to guide the conversation. For example, you could use     
       the configuration to determine which responses to show    
       to the user based on their inputs.                        
                                                                 
    Here's an example of how this might look in code:            
                                                                 
                                                                 
     from fin import start_up; from fin.config_handler impor     
     load_config                                                 
                                                                 
     # Load configuration from YAML file                         
     load_config()                                               
                                                                 
     # Start chat loop                                           
     start_up()                                                  
                                                                 
     while True:                                                 
         # Handle user input and render response based on        
     config                                                      
         pass                                                    
                                                                 
                                                                 
    By using these two modules together, you can create a        
    simple chatbot that loads configuration from a YAML file     
    and uses it to guide the conversation. Of course, this is    
    just a basic example, and you can customize and extend       
    the fin package to build more complex chatbots with          
    additional features and functionality.                       
                                                                 
                                                                 
─────────────────────────────────────────────────────────────────
```