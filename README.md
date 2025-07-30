# ai-devs2
Python code for the AI-devs2 


### To prepare environment: 
1. Add your API_KEYS to ~/.bashrc or ~/.zshrc if you're using mac
2. Prepare venv and install requirements
```bash
    virtualenv venv
    pip3 install -r requirements.txt
    source venv/bin/activate
```

To run tasks:
```bash
    python3 -m tasks.$task_name
```

### Task details

1. helloapi
    
2. moderation  
    The task is to receive an array of sentences (4 pieces), and then return an array with information about which sentences did not pass moderation. If the first and last sentence did not pass moderation, the answer should be [1,0,0,1]. Remember to return an array in JSON in the ‘answer’ field, not a plain string.

3. blogger  
    Write a blog post (in Polish) about making a Margherita pizza. As input you will receive a list of 4 chapters that must appear in the post (must be written by LLM). As response you must return an array (in JSON format) of 4 fields representing the four written chapters, e.g.: {“answer”:[“text 1”,“text 2”,“text 3”,“text 4”]}

4. liar  
    Your task is to send your question in English (any question, e.g., "What is the capital of Poland?") to the /task/ endpoint in a field called 'question' (POST method, as a regular form field, NOT JSON). The API system will either answer this question (in the 'answer' field) or start talking about something completely different, changing the subject. Your task is to write a filtering system (Guardrails) that will determine (YES/NO) whether the answer is on-topic. Then, return your verdict to the checking system as a single word YES/NO. If you retrieve the task content through the API without sending any additional parameters, you will receive a complete set of suggestions. How do you know if the answer is on-topic? If your question was about the capital of Poland and you receive a list of monuments in Rome in response, the answer you should send to the API is NO.