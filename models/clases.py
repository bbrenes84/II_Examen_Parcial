class City:
    def __init__(self, id=0, name="", status=1):
        self.id = id
        self.name = name
        self.status = status

    def __str__(self):
        return self.name
    
class Job:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return self.name
    
class Employee:
    def __init__(self, first_name, last_name, city, job, salary, status):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.job = job
        self.salary = salary
        self.status = status
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def get_city(self):
        return self.city.name
    
    def get_job(self):
        return self.job.name
    
    def get_salary(self):
        return self.salary
    
    def get_status(self):
        return self.status
    
    def set_status(self, status):
        self.status = status

    
