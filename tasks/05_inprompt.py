from lib.handle_task import get_auth_token, get_task_details, send_answer
from openai import OpenAI
import logging
import requests as request

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
handlers = [
    logging.StreamHandler()
]

logger = logging.getLogger(__name__)

token = get_auth_token("inprompt")
task_details = get_task_details(token)
 
 ## find person name in question
question = task_details["question"]
logger.info("Pytanie: %s", question)

client = OpenAI()

def find_person_name(question, client):
    prompt = (
        f"Question: {question}\n"
        "Which person is mentioned in the question? Respond with the person's name."
    )
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    name = response.choices[0].message.content.strip().upper()
    return name

def filter_information(input_list, person_name):
    context = [info for info in input_list if info.lower().startswith(person_name.lower())]
    return context

def generate_answer(question, context, client):
    prompt = (
        f"Question: {question}\n"
        f"Context: {context}\n"
        "Respond to the question based on the context provided."
    )
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response.choices[0].message.content
    return answer

person_name = find_person_name(question, client)
person_information = filter_information(task_details["input"], person_name)
#logger.info("Filtered information for %s: %s", person_name, person_information)
answer = generate_answer(question,person_information, client)
send_answer(token, answer)