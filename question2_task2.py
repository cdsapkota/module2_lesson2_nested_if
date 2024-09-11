attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
system = "audio system" if attendees < 100 else "projector"
print(venue, "and", system)