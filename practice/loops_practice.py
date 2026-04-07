import random, time

class Solver:

    def numbertask(self):
        numbers = list(range(1,8))
        for n in numbers:
            print(n)
            if n == 5:
                break
    
    def wordstask(self):
        words = [f"str{i}" for i in range(10)]
        for word in words:
            print(word)

    def rostics_load(self):
        count = 0
        while count < 10:
            load = random.randint(0,100)
            
            if load > 85:
                print(f"Крылышки в опасности! Нагрузка - {load}")
            time.sleep(0.2)
            count += 1
                

practice = Solver()
practice.rostics_load()
