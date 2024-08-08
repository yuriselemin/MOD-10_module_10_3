import threading
import random
import time

# Домашнее задание по теме "Блокировки и обработка ошибок"
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()


    def deposit(self):
        for i in range(100):
            replenishment = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += replenishment
            print(f"Пополнение: {replenishment}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            request = random.randint(50, 500)
            print(f"Запрос на: {request}")
            if request <= self.balance:
                self.balance -= request
                print(f"Снятие: {request}. Баланс: {self.balance}")
            else:
                print("Запрос отклонен, недостаточно средств")
                self.lock.acquire()

bk = Bank()
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()

th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")


