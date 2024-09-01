APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="John Doe", job="Admin"):
        self.name = name  # Use the property setter
        self.job = job    # Use the property setter

    # Name property
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()  # Convert to title case
        else:
            print("Name must be string between 1 and 25 characters.")

    # Job property
    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, job):
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")