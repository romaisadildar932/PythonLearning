# Generator -> A special function that produces values one at a time using the yield keyword.

def my_generator(num):
    while num > 0:
        yield num
        num-=1

for n in my_generator(5):
    print(n)