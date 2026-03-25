
# AI-Integration

A simple Python project that integrates a local AI model with both:

 - **FastAPI backend**

- **terminal-based guessing game**

This project uses **Ollama** to run a local LLM and powers an animal guessing game where the AI chooses a secret animal and the user tries to guess it through chat.

## Features

- Local AI integration with **Ollama**
- FastAPI server with chat endpoints
- Persistent chat memory using `memory.json`
- Simple project structure for learning Python + AI + APIs

## Project Structure

  

```bash
AI-Integration/
├──  api/
│  └──  ask.py
├──  model/
│  ├──  chat_request.py
│  └──  chat_response.py
├──  services/
│  ├──  ask.py
│  └──  history.py
├──  main.py
├──  memory.json
├──  requirements.txt
└──  .gitignore
```
## How  It  Works
The  AI  plays  a  game  with  the  user:
- The  AI  chooses  one  secret  animal
- The  user  asks  questions  or  makes  guesses
- The  AI  gives  hints  without  revealing  the  animal

If  the  user  guesses  correctly,  the  AI  responds  with:
```bash
YOU  WON!
```
The  conversation  history  is  saved  in  ```memory.json```  so  the  game  can  continue  across  sessions.

## Requirements
- Python  3.10+
- Ollama installed

A  local  Ollama  model  such  as:
- ollama  run  llama3

Install  Python  dependencies:

```pip  install  -r  requirements.txt```

## Setup

1.  Clone  the  repository

	```git  clone  https://github.com/Vlonetatii3/AI-Integration.git```
	
	```cd  AI-Integration```

2.  Install  dependencies

	```pip  install  -r  requirements.txt```

3.  Start  Ollama
| Make  sure  **Ollama**  is  running  locally  and  that  the  model  is  available: 
	```ollama  run  llama3```

## Run  the  API

  

Start  the  **FastAPI**  app  with:

	```uvicorn  main:app  --reload```
	
The  server  will  be  available  at:

```http://127.0.0.1:8000```

Interactive  API  docs:

```http://127.0.0.1:8000/docs```

## API  Endpoints

**GET  /**
Health  check  endpoint.

***Response***

```
{

"message":  "Chatbot API is running"

}
```
**POST  /chat**
Send  a  message  to  the  AI  game.

***Request***

```
{

"message":  "Is it a mammal?"

}
```
  
***Response***

```
{

"reply":  "Yes, it is a mammal."

}
```

**POST  /reset** 

Resets  the  game  and  starts  a  new  secret  animal.

***Response***

```
{

"message":  "Game reset successfully"

}
```
  

## Tech  Stack

- Python
- FastAPI
- Pydantic
- Requests
- Ollama
- JSON  file  storage

## Learning  Goals
 
### This  project  is  a  good  beginner-friendly  example  of:
 - List item
- building  APIs  with  FastAPI
- integrating  local  LLMs
- saving  simple  persistent  memory

## Future  Improvements
Possible  next  steps  for  this  project:
 - add  per-user  sessions
 - improve  prompt  consistency
 - add  better  error  handling
 - create  a  frontend  UI
 - store  memory  in  a  database  instead  of  JSON
 - support  multiple  games  or  modes

## Author
Created  by  **Vlonetatii3**