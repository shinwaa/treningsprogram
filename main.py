import json

def say_hello(name):
    print(f"Hei {name}!")

def save_workout(workout_data):
        try:
            with open("treningshistorikk.json", "r") as f:
                existing_data = json.load(f)


        except: 
            existing_data = []

        existing_data.append(workout_data)

        with open("treningshistorikk.json", "w") as f:
            json.dump(existing_data, f)

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


def get_number(prompt, number_type):
    while True:
        try:
            number = number_type(input(prompt))

            if number > 0:
                return number

            print("Tallet må være større enn 0.")

        except ValueError:
            print("Du må skrive inn et gyldig tall.")



def handle_normal_run():

    run_data = {}

    print("Du valgte vanlig løpetur")

    run_data["distance"] = get_number("Hvor langt løp du? ", float)
    print(f"Du løp {run_data['distance']} km")

    run_data["workout_type"] = classify_workout(run_data["distance"])
    print(run_data["workout_type"])

    run_data["time"] = get_number("Hvor lang tid brukte du? ", float)

    run_data["pace"] = calculate_pace(run_data["time"], run_data["distance"])

    run_data["formatted_pace"] = format_pace(run_data["pace"])
    print(f"Pace: {run_data['formatted_pace']} min/km")

    save_workout(run_data)

def handle_interval_run():

    interval_data = {}

    print("Du valgte intervalløkt")

    interval_data["number_of_intervals"] = get_number("Hvor mange drag løp du? ", int)

    interval_data["interval_duration"] = get_number("Hvor mange minutter per drag? ", float)

    interval_data["pause_duration"] = get_number("Hvor mange minutter pause mellom dragene? ", float)

    interval_data["number_of_pauses"] = interval_data["number_of_intervals"] - 1

    interval_data["total_pause_duration"] = interval_data["number_of_pauses"] * interval_data["pause_duration"]

    interval_distances = []

    for i in range(interval_data["number_of_intervals"]):
        interval_distance = get_number(f"Hvor langt løp du på drag {i + 1}? ", float)
        interval_distances.append(interval_distance)

    interval_data["interval_distances"] = interval_distances
 


    
    interval_data = summarize_interval_workout(interval_data)

    print_interval_summary(interval_data)

    save_workout(interval_data)

def find_longest_interval(interval_distances):

    longest_interval = max(interval_distances)
    return longest_interval


def summarize_interval_workout(interval_data):

    pace_per_interval = []
        

    interval_data["total_interval_duration"] = interval_data["number_of_intervals"] * interval_data["interval_duration"]

    interval_data["average_interval_pace"] = calculate_pace(
        interval_data["total_interval_duration"], sum(interval_data["interval_distances"])
    )
    interval_data["true_average_pace"] = format_pace(interval_data["average_interval_pace"])

    interval_data["total_distance"] = sum(interval_data["interval_distances"])

    interval_data["total_workout_duration"] = interval_data["total_interval_duration"] + interval_data["total_pause_duration"]

    interval_data["longest_interval"] = find_longest_interval(interval_data["interval_distances"])

    for i, interval_distance in enumerate(interval_data["interval_distances"]):
        interval_pace = calculate_pace(interval_data["interval_duration"], interval_distance)
        true_interval_pace = format_pace(interval_pace)
        pace_per_interval.append(true_interval_pace)

    interval_data["pace_per_interval"] = pace_per_interval

    return interval_data


def print_interval_summary(interval_data):

    for i, interval_distance in enumerate(interval_data["interval_distances"]):
        pace = interval_data["pace_per_interval"][i]
        print(
            f"Drag {i + 1}: {interval_distance} km - pace {pace} min/km"
        )

    print(f"Lengste drag: {interval_data['longest_interval']} km")
    print(f"Gjennomsnittspace på dragene: {interval_data['true_average_pace']} min/km")
    print(f"Total distanse på dragene: {interval_data['total_distance']} km.")
    print(f"Total arbeidstid: {interval_data['total_interval_duration']} min")
    print(f"Total pausetid: {interval_data['total_pause_duration']} min")
    print(f"Total tid: {interval_data['total_workout_duration']} min")


def show_history():
    try:
        with open("treningshistorikk.json", "r") as f:
            history_data = json.load(f)

    except:
        print("Du har ikke noe treningsdata enda.")
        return

    for i, workout in enumerate(history_data):
        if "number_of_intervals" in workout:
            print(f"{i + 1}. Interval økt: {workout['number_of_intervals']} drag, gjennomsnittspace:{workout['true_average_pace']} min/km, distanse løpt: {workout['total_distance']} km.")

        else:
            print(f"{i + 1}. Normal økt: Distanse: {workout['distance']} km, pace: {workout['formatted_pace']} min/km")
        
        

def main():

    name = input("Hva heter du? ")
    say_hello(name)

    print("1. Vanlig løpetur")
    print("2. Intervalløkt")
    print("3. Historik/statestikk")

    while True:
        workout_choice = get_number("Velg økttype: ", int)

        if workout_choice == 1 or workout_choice == 2 or workout_choice == 3:
            break

        print("Ugyldig tall, velg 1 eller 2.")

    if workout_choice == 1:
        handle_normal_run()

    elif workout_choice == 2:
        handle_interval_run()

    elif workout_choice == 3:
        show_history()

if __name__ == "__main__":
    main()
