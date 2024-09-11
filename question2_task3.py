attendees = int(input("Enter number of attendees: "))
meal = input("Do you want vegetarian food? (yes or no) ")
venue = "large hall" if attendees > 100 else "conference room"
system = "audio system" if attendees < 100 else "projector"
caterer = "Veggie Delight Caterers" if meal == "yes" else "Gourmet Meals Caterers"
print(venue, "and", system)
print(caterer)