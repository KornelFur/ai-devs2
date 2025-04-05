from lib.handle_task import get_auth_token, get_task_details, send_answer
from openai import OpenAI
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
handlers = [
    logging.StreamHandler()
]

logger = logging.getLogger(__name__)

token = get_auth_token("blogger")
task_details = get_task_details(token)

messages = task_details["blog"]
logger.info("Task details retrieved successfully: \n%s", messages)

client = OpenAI()
results = []

try:
    for message in messages:
        logger.info("Generating content for chapter: %s", message)
        response = client.responses.create(
            model = "gpt-4o-mini",
            instructions = "Twoim zadaniem jest napisanie postów na podstawie podanych tematów. Każdy post powinien być krótki i zwięzły, nie przekraczający 50 słów. ",
            input = message,
            temperature = 0.1,
        )
        logger.info("Generated content: %s", response)
        for output_message in response.output:
            for content in output_message.content:
                results.append(content.text)
except Exception as e:
    logger.error("Error generating content: %s", e)

logger.info("Generated content for all chapters successfully: %s", results)

answer = results
send_answer(token, answer)