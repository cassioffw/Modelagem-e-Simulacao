import queue
import random

from threading import Lock, Thread
import time

lock = Lock()

def simulation(cashierList):
  for n in range (1, 11):
    customer = {"ID": random.randint(1, 100), "QTD": random.randint(1, 20)}

    shortest_queue = min(cashierList, key=lambda x: x["Queue"].qsize())
    shortest_queue["Queue"].put(customer)
    with lock:
      print(f"Cliente {customer['ID']} com {customer['QTD']} itens entrou na fila do caixa {shortest_queue['Cashier']}.")
    time.sleep(customer["QTD"])
    print(f"Cliente {customer['ID']} passou no caixa {shortest_queue['Cashier']}")

q1 = queue.Queue()
q2 = queue.Queue()
q3 = queue.Queue()
cashierList = [{"Cashier": 1, "Queue": q1}, {"Cashier":2, "Queue": q2}, {"Cashier": 3, "Queue": q3}]
customers = []

for n in range(1, 11):
  customers.append({"ID": n, "QTD": random.randint(1, 20)})

for c in customers:
  cashierList[random.randint(0, 2)]["Queue"].put(c)

t1 = Thread(target=simulation, args=(cashierList,))
t2 = Thread(target=simulation, args=(cashierList,))
t3 = Thread(target=simulation, args=(cashierList,))

t1.start()
t2.start()
t3.start()