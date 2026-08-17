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

def main():
   
    name = input("Hva heter du? ")
    say_hello(name)

    print("1. Vanlig løpetur")
    print("2. Intervalløkt")
    workout_choice = int(input("velg økttype: "))
    

    if workout_choice == 1:
        print("Du valgte vanlig løpetur")

        distance = get_number("Hvor langt løp du? ")
        print("du løp", distance, "km")

        workout_type = classify_workout(distance)
        print(workout_type)

        time = get_number("Hvor lang tid brukte du? ")

        pace = calculate_pace(time, distance)

        formatted_pace = format_pace(pace)
        print(f"pace: {formatted_pace} min/km")

        
    elif workout_choice == 2:
        print("Du valgte intervalløkt")


        number_of_intervals = int(input("hvor mange drag løp du? "))

        interval_duration = float(input("Hvor mange minutter per drag? "))

        interval_distances = []


        
        for i in range(number_of_intervals):
            interval_distance = float(input(f"Hvor langt løp du på drag {i + 1}? "))
            interval_distances.append(interval_distance)

        for i, interval_distance in enumerate(interval_distances):
            interval_pace = calculate_pace(interval_duration, interval_distance)

            true_interval_pace = format_pace(interval_pace)
           
            print(f"Drag {i + 1}: {interval_distance} km - pace {true_interval_pace} min/km")
           

        

        # intervals = [4, 4, 4, 4, 4]
    
        # total_run_time = 0

        # for interval in intervals:
        #     print("Drag: ", interval, "min")
        #     total_run_time += interval 

        # print("Total terskeltid: ", total_run_time)

    

    
if __name__ == "__main__":
    main()
