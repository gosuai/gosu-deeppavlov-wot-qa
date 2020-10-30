import pickle
from functools import lru_cache

from deeppavlov import build_model, configs

from django.shortcuts import render

MODEL_CONFIG = configs.squad.squad


@lru_cache()
def get_all_tanks():
    with open('homepage/data/info/tank_names.txt', 'rb') as fp:
        all_tanks = pickle.load(fp)
    return ''.join(f'<option value="{tank}"></option>' for tank in all_tanks)


@lru_cache()
def get_model():
    return build_model(MODEL_CONFIG)


@lru_cache()
def get_tank(tank_name):
    with open(f'homepage/data/all tanks/{tank_name}.txt', 'r') as file:
        tank_info = file.read().replace('\n', '. ')
    return tank_info


def index(request):
    question = ''
    answer = ''
    tank_info = ''
    tank_name = ''

    if request.method == 'POST':
        question = request.POST['question']
        tank_name = request.POST['tank_name']

        if tank_name not in question:
            question = tank_name + ' ' + question

        #make answer
        tank_info = get_tank(tank_name)
        model_qa = get_model()
        answer = str(model_qa([tank_info], [question]))

    context = {
        'question': question,
        'tank_name': tank_name,
        'answer': answer,
        'all_tanks_html': get_all_tanks(),
        'tank_info': tank_info,
    }
    return render(request, 'homepage/index.html', context)
