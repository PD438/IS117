#Part 1 Lab: Movie Ticket Booking System
#Author: Paulo Duarte
#Date: 3/2/2025
#Purpose: To create a movie ticket booking system that allows the user to select a movie, time, and number of tickets. The program will then calculate the total cost of the tickets and display the information back to the user.

first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")

print("\n Welcome to the Movie Ticket Booking System, "+first_name+" "+last_name+"!")
print("\n Here are the movies currently playing:")
movies = [
    {"title": "The Lion King", "times": ["12:00pm", "3:00pm", "6:00pm", "9:00pm"], "price": 10.00, "Genre": "Animation"},
    {"title": "Avengers: Endgame", "times": ["12:30pm", "3:30pm", "6:30pm", "9:30pm"], "price": 12.00, "Genre": "Action"},
    {"title": "Toy Story 4", "times": ["1:00pm", "4:00pm", "7:00pm", "10:00pm"], "price": 8.00, "Genre": "Animation"},
    {"title": "Aladdin", "times": ["1:30pm", "4:30pm", "7:30pm", "10:30pm"], "price": 9.00, "Genre": "Adventure"},
    {"title": "The Devil Wears Prada", "times": ["2:00pm", "5:00pm", "8:00pm", "11:00pm"], "price": 7.00, "Genre": "Comedy"},
    {"title": "The Notebook", "times": ["2:30pm", "5:30pm", "8:30pm", "11:30pm"], "price": 7.00, "Genre": "Romance"}
]

print("Movies:")
for i, movie in enumerate(movies, start=1):
    print(f"{i}. {movie['title']} (Price: ${movie['price']}) (Times: {', '.join(movie['times'])})")

# user selects movie
selected_movie_index = int(input("Enter the number of the movie you would like to watch: ")) - 1

# check if movie is in the list
if 0 <= selected_movie_index < len(movies):
    selected_movie_obj = movies[selected_movie_index]
    print(f"You have selected {selected_movie_obj['title']} - ${selected_movie_obj['price']} - {selected_movie_obj['Genre']}")
else:
    selected_movie_obj = None
    print("Invalid selection, please try again.")

print("Movies:")
for movie in movies:
    print(f"{movie['title']}(Price: ${movie['price']}) (Times: {', '.join(movie['times'])}) ")

#user selects movie
if selected_movie_obj:
    selected_time = input("\n PauloEnter the time you would like to watch the movie: ")
    num_tickets = int(input("\n Enter the number of tickets you would like to purchase: "))
    total_cost = num_tickets * selected_movie_obj['price']
    inventory_of_tickets = 100
    if num_tickets > inventory_of_tickets:
        print(f"Sorry, there are not enough tickets available for {selected_movie_obj['title']} at {selected_time}.")
    else:
        inventory_of_tickets -= num_tickets
        print(f"Your tickets have been booked for {selected_movie_obj['title']} at {selected_time}.")
        print(f"Number of tickets remaining for {selected_movie_obj['title']} at {selected_time}: {inventory_of_tickets}")
    coupon_code = input("Do you have a coupon code? (yes/no): ")
    if coupon_code.lower() == "yes":
        coupon = input("Enter your coupon code: ")
        if coupon == "SAVE10":
            total_cost = total_cost - (total_cost * 0.10)
            print("You have received a 10% discount on your tickets.")
        elif coupon == "SAVE15":
            total_cost = total_cost - (total_cost * 0.15)
        elif coupon == "SAVE20":
            total_cost = total_cost - (total_cost * 0.20)
            print("You have received a 20% discount on your tickets.")    
        else:
            print("Invalid coupon code.")
    Review_Cart=input("Would you like to review your cart? (yes/no): ")
    if Review_Cart.lower() == "yes":
        print(f"Movie: {selected_movie_obj['title']}")
        print(f"Time: {selected_time}")
        print(f"Number of Tickets: {num_tickets}")
        print(f"Total Cost: ${total_cost:.2f}")
    else:
        print("You have not reviewed your cart.Please double check your cart before proceeding.")
    print(f"Your total cost is ${total_cost:.2f} for {num_tickets} tickets to {selected_movie_obj['title']} at {selected_time}.")



    #Thank You Message
    print(f"Thank you ({first_name} {last_name}) for using the Movie Ticket Booking System. Enjoy the movie!")