from lib.handle_task import get_auth_token, get_task_details, send_answer

token = get_auth_token("helloapi")
task_details = get_task_details(token)

answer = task_details["cookie"]

send_answer(token, answer)