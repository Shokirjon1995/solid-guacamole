class Worker:
    def __init__(self, name, job):
        self.name = name
        self.job = job

class Moderator(Worker):
    def __init__(self,name,job):
        super().__init__(self,name, job)


    def show_job(self, name):
        return name.jobs

