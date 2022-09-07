people = 7861304740
print(people)
people = 7_861_304_740
print(people)

meals = 3
people_eat = people * meals
print(people_eat)

days = 365
meals_per_year = people_eat * days
print(meals_per_year)

print(type(meals_per_year))

ethernet_speed_mbps = 1000
efficiency = 0.7
maximum_capacity = ethernet_speed_mbps * efficiency
print(maximum_capacity)

download_speed_average = 96.25
usage = ethernet_speed_mbps / download_speed_average
print(usage)

speed_of_light = 299_792_458

distance_Rotterdam_NewYork = 5_862.03
time_to_reach_NYC = (distance_Rotterdam_NewYork * 1000) / speed_of_light
print(time_to_reach_NYC)

print(type(time_to_reach_NYC))

ship = 'Titanic'

sentence = "He doesn't think it's a good idea to spend all his money on video games."
print(sentence)

paragraph = """Computer Technology means all designs, drawings, procedures
(including design, manufacturing, test and maintenance procedures),
specifications, software (other than as described within the meaning of the term
"Software" defined elsewhere herein), printed circuit board art work, integrated
circuit masks, test equipment, tools, fixtures, documentation, training materials,
and information, in whatever form, related to, useful, utilizable or necessary in
the design, manufacture, test and/or maintenance of the computer system, or relate
to any Technology Licenses."""
print(paragraph)

characters_in_paragraph = len(paragraph)
print(f"{paragraph}\n\nThe paragraph has {characters_in_paragraph} characters.")

year = 1936
inventor = "Alan Turing"
name_of_machine = "automatic machine"

invention = f'The Turing machine was invented in {year} by {inventor}, who called it an "a-machine" ({name_of_machine}).'
print(invention)

print(type(invention))

logged_in = False
print(logged_in)

netwerk_aactivity = True
print(netwerk_aactivity)

user_name = "Sebastiaan van der Weel"
entered_name = input("Enter your user name, please: ")
size_user_name = len(user_name)
size_entered_name = len(entered_name)
user_name_is_bigger = size_user_name > size_entered_name
entered_name_is_bigger = size_entered_name > size_user_name

print(f"The user name {user_name} has more characters then the entered name {entered_name} is: {user_name_is_bigger}")

print(f"The entered name {entered_name} has more characters then the user name {user_name} is: {entered_name_is_bigger}")

lights_on = False
lock_closed = True

alarm_activated = not lights_on and lock_closed
print(f"The alarm is activated, is: {alarm_activated}")