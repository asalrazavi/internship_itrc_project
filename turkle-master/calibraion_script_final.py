import json
import sys
import ast


def to_dict(string):
    formatted_string = string.replace("‘", '"').replace("’", '"').replace("'", '"')
    json_loaded = json.loads(formatted_string)
    return json_loaded


calib_answers = sys.argv[1]
user_answers = sys.argv[2]

# calib_answers = json.dumps(calib_answers)
calib_answers_dict = to_dict(calib_answers)
user_answers_dict = to_dict(user_answers)

score = 0

for key in calib_answers_dict.keys():
    if key in user_answers_dict:
        if calib_answers_dict[key] == user_answers_dict[key]:
            score += 1
    elif key not in user_answers_dict and calib_answers_dict[key] == '0':
        score += 1

score = score / len(calib_answers_dict)

sys.stdout.write(str(score))
sys.stdout.flush()
sys.exit()
