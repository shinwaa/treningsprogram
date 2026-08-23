def say_hello(name):
    print(f"Hei {name}!")


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

    print("Du valgte vanlig løpetur")

    distance = get_number("Hvor langt løp du? ", float)
    print(f"Du løp {distance} km")

    workout_type = classify_workout(distance)
    print(workout_type)

    time = get_number("Hvor lang tid brukte du? ", float)

    pace = calculate_pace(time, distance)

    formatted_pace = format_pace(pace)
    print(f"Pace: {formatted_pace} min/km")


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


def find_longest_interval(interval_distances):

    longest_interval = max(interval_distances)
    return longest_interval


def summarize_interval_workout(interval_data):

    interval_data["total_interval_duration"] = interval_data["number_of_intervals"] * interval_data["interval_duration"]

    interval_data["average_interval_pace"] = calculate_pace(
        interval_data["total_interval_duration"], sum(interval_data["interval_distances"])
    )
    interval_data["true_average_pace"] = format_pace(interval_data["average_interval_pace"])

    interval_data["total_distance"] = sum(interval_data["interval_distances"])

    interval_data["total_workout_duration"] = interval_data["total_interval_duration"] + interval_data["total_pause_duration"]

    interval_data["longest_interval"] = find_longest_interval(interval_data["interval_distances"])


    return interval_data


def print_interval_summary(interval_data):

    for i, interval_distance in enumerate(interval_data["interval_distances"]):
        interval_pace = calculate_pace(interval_data["interval_duration"], interval_distance)

        true_interval_pace = format_pace(interval_pace)

        print(
            f"Drag {i + 1}: {interval_distance} km - pace {true_interval_pace} min/km"
        )

    print(f"Lengste drag: {interval_data['longest_interval']} km")
    print(f"Gjennomsnittspace på dragene: {interval_data['true_average_pace']} min/km")
    print(f"Total distanse på dragene: {interval_data['total_distance']} km.")
    print(f"Total arbeidstid: {interval_data['total_interval_duration']} min")
    print(f"Total pausetid: {interval_data['total_pause_duration']} min")
    print(f"Total tid: {interval_data['total_workout_duration']} min")


def main():

    name = input("Hva heter du? ")
    say_hello(name)

    print("1. Vanlig løpetur")
    print("2. Intervalløkt")

    while True:
        workout_choice = get_number("Velg økttype: ", int)

        if workout_choice == 1 or workout_choice == 2:
            break

        print("Ugyldig tall, velg 1 eller 2.")

    if workout_choice == 1:
        handle_normal_run()

    elif workout_choice == 2:
        handle_interval_run()


if __name__ == "__main__":
    main()
