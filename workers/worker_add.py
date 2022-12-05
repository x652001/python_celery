from celery import Task


class Add(Task):
    def add(self, x,y):
        
        return x * y
        pass
