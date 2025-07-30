from lib.handle_task import get_auth_token, get_task_details, send_answer
from openai import OpenAI
import logging
import requests as request

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
handlers = [
    logging.StreamHandler()
]

logger = logging.getLogger(__name__)

token = get_auth_token("liar")
task_details = get_task_details(token)

#set a question
payload = {"question": "What is the capital of Poland?"}

task_url = f"https://tasks.aidevs.pl/task/{token}"

response= request.post(task_url, data=payload)

logger.info("Answer: %s", response.json()["answer"])
client = OpenAI()

def is_answer_true(question, answer, client):
    prompt = (
        f"Question: {question}\n"
        f"Answer: {answer}\n"
        "Is the answer true? Respond with YES or NO."
    )
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    verdict = response.choices[0].message.content.strip().upper()
    logger.info("Verdict: %s", verdict)
    return verdict

answer = is_answer_true(payload["question"], response.json()["answer"], client)

send_answer(token, answer)

