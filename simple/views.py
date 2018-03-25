from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from urlparse import urlparse
import re
import os
import json

from collections import defaultdict

def parse(label):
    set_url=urlparse(label['set_url'])
    m = re.search(r"A fashion look from (.+) by (.+) featuring (.+)", label['desc'])
    return {
      'style': set_url.path.split('/')[1], 
      'image': label['image'],
      'items': label['items'],
      'name': '{}.{}'.format(m.group(1), m.group(2)) if m is not None else ''
    }

style = defaultdict(list)
label_path='/host/labels/'
for filename in os.listdir(label_path):
    with open(os.path.join(label_path, filename)) as file:
        labels = json.load(file)
        sets = [parse(label) for label in labels]
        for element in sets:
            style[element['style']].append(element)
popular=[(k,v) for k,v in style.items() if len(v) >= 10]
print popular[:10]

def index(request):
    context = {"name" : "wenke", "style" : popular[:10]}
    return render(request, 'simple/index.html', context)
    # return HttpResponse("Hello, world. You're at the polls index.")
