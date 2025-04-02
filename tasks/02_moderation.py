from lib.handle_task import get_auth_token, get_task_details, send_answer
from openai import OpenAI
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
handlers = [
    logging.StreamHandler()
]

logger = logging.getLogger(__name__)

token = get_auth_token("moderation")
task_details = get_task_details(token)

messages = task_details["input"]
logger.info("Task details retrieved successfully: \n%s", messages)

# call openai moderation API to verify if the messages are safe
client = OpenAI()
moderation_results=[]

for message in messages:
    try:
        logger.info("Calling OpenAI moderation API with message: %s", message)
        response = client.moderations.create(model="text-moderation-latest", input=message)
        logger.info("Moderation response: %s", response)
    except Exception as e:
        logger.error("Error calling OpenAI moderation API: %s", e)

    flagged = response.results[0].flagged
    logger.info("Flagged status: %s", flagged)
    if flagged:
        moderation_results.append(1)
    elif not flagged:
        moderation_results.append(0)

answer = moderation_results

send_answer(token, answer)