from datetime import datetime

import backend.models.investment as investment


class Portfolio:
    def __init__(self, name, id, value):
        self.name = name
        self.id = id
        self.value = value

    def __str__(self):
        return f'Portfolio: {self.name}, ID: {self.id}, Value: ${self.value}'
    
    #Conventional setters and getters
    @name.setter
    def name(self, name):
        self.name = name
    @value.setter
    def value(self, value):
        self.value = value
    @property
    def name(self):
        return self.name
    @property
    def value(self):
        return self.value
    @property
    def id(self):
        return self.id
    #Custom Method
