def say_hello(name):
    print("Hei!", name)

name = input("Hva heter du?")

say_hello(name)

distance = float(input("Hvor langt løp du?"))
print("du løp", distance, "km")


if  distance < 5:
    print("kort økt")
elif 5 <= distance <= 10:
    print("middels økt")
else:
    print("lang økt")

time = float(input("Hvor lang tid brukte du?"))

def calculate_pace(time, distance):
    return time / distance
    

pace = calculate_pace(time, distance
)
minutes = int(pace)
seconds = round((pace - minutes) * 60)

if seconds == 60:
    minutes += 1
    seconds = 0

print(f"pace: {minutes}:{seconds:02d} min/km")

