# step01/error_demo.py
def get_last_content(conversation):
    return conversation[-1]["content"]


conversation = []
print(get_last_content(conversation))