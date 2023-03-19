import smtplib

from person import Person
import re
import email

class Employee(Person):
    moods = ('happy', 'tired', 'lazy')

    def __init__(self, name, money, mood, healthRate, id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def sleep(self, hours):
        if hours == 7:
            self.mood = 'happy'
        elif hours < 7:
            self.mood = 'tired'
        else:
            self.mood = 'lazy'

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 80
        elif meals == 1:
            self.healthRate = 30

    def buy(self, items):
        self.money -= 10

    def work(self, hours):
        if hours == 8:
            self.mood = 'happy'
        elif hours < 8:
            self.mood = 'tired'
        else:
            self.mood = 'lazy'

    def send_mail(self, to, subject, msg, receiver_name):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.email, 'your-password-here')
        message = f"Subject: {subject}\n\nDear {receiver_name},\n\n{msg}"
        server.sendmail(self.email, to, message)
        server.quit()

    def drive(self, distance):
        self.car.run(self.car.velocity, distance)

    def refuel(self, gasAmount=100):
        self.car.fuelRate += gasAmount

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 1000:
            raise ValueError('Salary must be 1000 or more.')
        self._salary = value

    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, car):
        self._car = car

    @property
    def email(self):
        return self._email

    @property
    def salary(self):
        return self.__salary

