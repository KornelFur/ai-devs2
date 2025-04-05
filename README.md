# ai-devs2
Python code for the AI-devs2 


### To prepare environment: 
1. Add your API_KEYS to ~/.bashrc
2. Prepare venv and install requirements
```bash
    virtualenv venv
    pip3 install -r requirements.txt
    source venv/bin/activate
```

To run tasks:
```bash
    python -m tasks.$task_name
```

### Task details

1. helloapi
    
2. moderation  
    The task is to receive an array of sentences (4 pieces), and then return an array with information about which sentences did not pass moderation. If the first and last sentence did not pass moderation, the answer should be [1,0,0,1]. Remember to return an array in JSON in the ‘answer’ field, not a plain string.

3. blogger  
    Write a blog post (in Polish) about making a Margherita pizza. As input you will receive a list of 4 chapters that must appear in the post (must be written by LLM). As response you must return an array (in JSON format) of 4 fields representing the four written chapters, e.g.: {“answer”:[“text 1”,“text 2”,“text 3”,“text 4”]}