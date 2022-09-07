from cmath import sqrt


x = 9.1

sum1 = 3 * x - 1
sum2 = sqrt(sum1)
sum3 = (1 + x) ** 2
y = sum2 + sum3

print(f"De waarde van y = {y} als x = {x}")

a = 0.87
b = 2.7
c = 5.03

sum1 = (b ** 2) - (4 * a * c)
sum2 = sqrt(sum1)
sum3 = -b + sum2
y = sum3 / (2 * a)

print(f"De waarde van y = {y} als a = {a}, b = {b} en c = {c}")

unloaded_containers = 331
unloading_time = 441

loaded_containers = 287
load_time = 295

average_unload_time = unloaded_containers / unloading_time
average_load_time = loaded_containers / load_time

print(f"De gemiddelde tijd voor het lossen per container = {average_unload_time} minuten.")
print(f"De gemiddelde tijd voor het laden per container = {average_load_time} minuten.")

t = 4
v = 179_875_474.8
c = 299_792_458

sum1 = (v ** 2) / (c ** 2)
sum2 = 1 / (v * (1 - sum1))
delta = t * sum2

print(f"Vanaf een komeet gezien zit u {delta} uur op de tuinstoel.")