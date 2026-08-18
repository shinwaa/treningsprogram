def say_hello(name):
    print("Hei!", name)

def classify_workout(distance):
    if distance < 5:
        return "kort økt, godt jobba!"
    elif distance < 10:
        return "medium økt, godt jobba!"
    else:
        return "lang økt, godt jobba!"

def calculate_pace(time, distance):
    return time / distance

def format_pace(pace):
    minutes = int(pace)
    seconds = round((pace - minutes) * 60)
    
    if seconds == 60:
        minutes += 1
        seconds = 0

    return f"{minutes}:{seconds:02d}"

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
           
            if number > 0:
                return number
        
            print("Tallet må være større enn 0.")

        except ValueError:
            print ("Du må skrive inn et gyldig tall.")

def get_integer(prompt):
    while True:
        try:
            number = int(input(prompt))

            if number > 0:
                return number
            
            print ("Tallet må være større enn 0.")

        except ValueError:
            print("Du må skrive inn et gyldig tall.")

def handle_normal_run():
    
    print("Du valgte vanlig løpetur")

    distance = get_number("Hvor langt løp du? ")
    print("du løp", distance, "km")

    workout_type = classify_workout(distance)
    print(workout_type)

    time = get_number("Hvor lang tid brukte du? ")

    pace = calculate_pace(time, distance)

    formatted_pace = format_pace(pace)
    print(f"pace: {formatted_pace} min/km")

def handle_interval_run():
    
    print("Du valgte intervalløkt")


    number_of_intervals = get_integer("hvor mange drag løp du? ")

    interval_duration = get_number("Hvor mange minutter per drag? ")

    pause_duration = get_number("Hvor mange minutter pause mellom dragene? ")

    number_of_pauses = number_of_intervals - 1

    total_pause_duration = number_of_pauses * pause_duration
        
    interval_distances = []


    for i in range(number_of_intervals):
        interval_distance = get_number(f"Hvor langt løp du på drag {i + 1}? ")
        interval_distances.append(interval_distance)

    for i, interval_distance in enumerate(interval_distances):
        interval_pace = calculate_pace(interval_duration, interval_distance)

        true_interval_pace = format_pace(interval_pace)
           
        print(f"Drag {i + 1}: {interval_distance} km - pace {true_interval_pace} min/km")
           
    total_distance = sum(interval_distances)
    print(f"Total distanse på dragene: {total_distance} km.")

    total_interval_duration = number_of_intervals * interval_duration
    average_interval_pace = calculate_pace(total_interval_duration, total_distance)
    true_average_pace = format_pace(average_interval_pace)

    print(f"Gjennomsnittspace på dragene: {true_average_pace} min/km")

    total_workout_duration = total_interval_duration + total_pause_duration

    print(f"Total arbeidstid: {total_interval_duration} min")
    print(f"Total pausetid: {total_pause_duration} min")
    print(f"Total tid: {total_workout_duration} min")

def main():
   
    name = input("Hva heter du? ")
    say_hello(name)

    print("1. Vanlig løpetur")
    print("2. Intervalløkt")
    
    while True:
        workout_choice = get_integer("velg økttype: ")

        if workout_choice == 1 or workout_choice == 2:
            break
        
        print("Ugyldig tall, velg 1 eller 2.")

    if workout_choice == 1:
        handle_normal_run()

    elif workout_choice == 2:    
        handle_interval_run()
    

if __name__ == "__main__":
    main()
