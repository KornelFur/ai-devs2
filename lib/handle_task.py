import os
import requests
import logging
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
handlers = [
    logging.StreamHandler()
]

logger = logging.getLogger(__name__)

AIDEVS_APIKEY = os.getenv("AIDEVS_APIKEY")
AIDEVS_PREFIX = os.getenv("AIDEVS_PREFIX", "https://tasks.aidevs.pl/")
URL_TOKEN_PREFIX = urljoin(AIDEVS_PREFIX, "token/")
URL_TASK_PREFIX = urljoin(AIDEVS_PREFIX, "task/")
URL_ANSWER_PREFIX = urljoin(AIDEVS_PREFIX, "answer/")
URL_HINT_PREFIX = urljoin(AIDEVS_PREFIX, "hint/")

#authorization
def get_auth_token(task_id):
    # check if AIDEVS_APIKEY is set in the environment
    if not AIDEVS_APIKEY:
        logger.error("AIDEVS_APIKEY is not set in the environment")
        return None
    
    # prepare url for token retrieval
    token_url = urljoin(URL_TOKEN_PREFIX, task_id)
    logger.info("Fetching auth token from %s", token_url)
    payload = {"apikey":AIDEVS_APIKEY}

    try:
        response = requests.post(url=token_url, json=payload)
        response_data = response.json()

        # check if the response contains an error
        if response_data["code"] == 0:
            logger.info("Token retrieved successfully: %s", response_data.get("token", ""))
            return response_data["token"]
        else:
            logger.error("Error fetching token: %s", response_data.get("msg", ""))
            return None
    except ValueError as e:
        logger.error(f"Token retrieval failed: {e}")

#task details
def get_task_details(token):
    if not token:
        logger.error("No token provided")
        return None
    #prepare url for fetching task details
    task_url = urljoin(URL_TASK_PREFIX, token)

    try:
        response = requests.get(url=task_url)
        response_data = response.json()
    
        # check if the response contains an error
        if response_data["code"] == 0:
            logger.info("Task details retrieved successfully: \n%s", response_data)
            return response_data
        else:
            logger.error("Error fetching task details: %s", response_data)
            return None
    except ValueError as e:
        logger.error(f"Task details retrieval failed: %s", e)
        return None
    
#submit answer
def send_answer(token, answer):
    answer_url = urljoin(URL_ANSWER_PREFIX, token)
    payload = {"answer": answer}

    try:
        response = requests.post(url=answer_url, json=payload)
        response_data = response.json()
        logger.info("Task answer submitted successfully: %s", response_data)

        if response_data["code"] == 0:
            logger.info("Answer submitted successfully: %s", response_data)
            return response_data
        else:
            logger.error("Error submitting answer: %s", response_data)
            return response_data
    except ValueError as e:
        logger.error(f"Answer submission failed: %s", e)