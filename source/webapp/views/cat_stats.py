from random import randint

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


class Cat:
    def __init__(self, name: str ) -> str:
        self.name = name
        self.age = randint(1,4)
        self.fullness = 40
        self.mood = 10
        self.status = ''

    def feed(self):
        self.status = self.set_status()
        if self.status == 'awake':
            self.fullness += 15
            self.mood += 5
            self.status = 'happy'
        elif self.status == 'sleep':
            self.fullness += 0
            self.mood += 5
        elif self.status == 'angry':
            self.fullness += 15
            self.mood += 20
        elif self.status == 'sad':
            self.fullness += 15
            self.mood += 20
        elif self.status == 'happy':
            self.fullness += 15
            self.mood += 5
        return self.status

    def play(self):
        self.status = self.set_status()
        if self.status == 'awake':
            self.fullness -= 10
            self.mood += 5
            for i in range(3):
                self.status = 'angry'
        elif self.status == 'angry':
            self.mood = 0
            self.status = 'awake'
        elif self.status == 'sleep':
            self.status = 'awake'
            self.mood +=5
        elif self.status == 'happy':
            self.fullness -= 10
            self.mood += 5
        return self.status

    def sleep(self):
        self.status = 'sleep'
        return self.status

    def set_status(self):
        if self.status == '':
            self.status = 'awake'
        if self.fullness > 100:
            self.status = 'sad'
            self.mood -= 30
        if self.mood > 70:
            self.status = 'happy'
        return self.status


cats = []


def cat_stats(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        if len(cats) == 0:
            cat = Cat(request.POST.get('name'))
            cats.append(cat)
        cat = cats[0]
        action = request.POST.get('action')
        if action == 'play':
            cat.play()
        elif action == 'feed':
            cat.feed()
        elif action == 'sleep':
            cat.sleep()
        return render(request, 'cat_stats.html', context={
            'name': cat.name,
            'age': cat.age,
            'mood': cat.mood,
            'fullness': cat.fullness,
            'status': cat.status,
        })


