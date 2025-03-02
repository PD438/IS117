#Part 1 Lab: Movie Ticket Booking System
#Author: Paulo Duarte
#Date: 3/2/2025
#Purpose: To create a movie ticket booking system that allows the user to select a movie, time, and number of tickets. The program will then calculate the total cost of the tickets and display the information back to the user.

first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")

print("Welcome to the Movie Ticket Booking System, "+first_name+" "+last_name+"!")
print("Here are the movies currently playing:")

movies = [
    {"title": "The Lion King", "times": ["12:00pm", "3:00pm", "6:00pm", "9:00pm"], "price": 10.00},
    {"title": "Avengers: Endgame", "times": ["12:30pm", "3:30pm", "6:30pm", "9:30pm"], "price": 12.00},
    {"title": "Toy Story 4", "times": ["1:00pm", "4:00pm", "7:00pm", "10:00pm"], "price": 8.00}
]

print("Movies:")
for movie in movies:
    print(f"{movie['title']}(Price: ${movie['price']}) (Times: {', '.join(movie['times'])}) ")

#user selects movie
selected_movie = input("Enter the movie you would like to watch: ")  

#check if movie is in the list
selected_movie_obj = None
for movie in movies:
    if movie['title'].lower() == selected_movie.lower():
        selected_movie_obj = movie
        print(f"You have selected {movie['title']} - ${movie['price']}")
        break
if selected_movie_obj is None:
    print("You have not selected a movie, please try to select a movie from the list below.")

if selected_movie_obj:
    selected_time = input("Enter the time you would like to watch the movie: ")
    num_tickets = int(input("Enter the number of tickets you would like to purchase: "))
    total_cost = num_tickets * selected_movie_obj['price']
    print(f"Your total cost is ${total_cost:.2f} for {num_tickets} tickets to {selected_movie_obj['title']} at {selected_time}.")

    #Thank You Message
    print(f"Thank you ({first_name} {last_name}) for using the Movie Ticket Booking System. Enjoy the movie!")