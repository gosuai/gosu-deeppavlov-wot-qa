from django.shortcuts import render
import os
import pickle

#load all tank names
global all_tanks_html
with open ('homepage/data/info/tank_names.txt', 'rb') as fp:
    all_tanks = pickle.load(fp)
all_tanks_html = ''
for tank in all_tanks:
    all_tanks_html += f'<option value="{tank}"></option>'

#deeppvalov model
import deeppavlov
from deeppavlov import build_model, configs
global model_qa
model_qa = build_model(configs.squad.squad, download=True)



def index(request):
    question = ''
    answer = ''
    tank_info = ''
    global all_tanks_html
    tank_name = ''

    if request.method == 'POST':
        question = request.POST['question']
        tank_name = request.POST['tank_name']

        if tank_name not in question:
            question = tank_name + ' ' + question

        
        #make answer
        with open(f'homepage/data/all tanks/{tank_name}.txt', 'r') as file:
            tank_info = file.read().replace('\n', '. ')

        global model_qa
        answer = str(model_qa([tank_info],[question]))





    context = {

        'question': question,
        'tank_name': tank_name,
        'answer': answer,
        'all_tanks_html': all_tanks_html,
        'tank_info': tank_info,

    }
    return render(request, 'homepage/index.html', context)
