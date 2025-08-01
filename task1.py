"""
Task 1: Music Concert Ticketing System
During the Jos Summer Music Concert, ticket sales were recorded as follows:

tickets = {"VIP": 50, "Regular": 150, "Student": 75}

Later in the day:
- A new "Backstage" experience with 10 tickets was introduced.
- The "Student" category sold out completely.
- The team wanted to keep a record of the day’s sales before preparing for next week’s concert.
"""
record = []
tickets = {"VIP": 50, "Regular": 150, "Student": 75}
new_ticket = {"backstage":10}
tickets.update(new_ticket)
print("Tickets before popping:", tickets)
tickets.pop("Student")
print("When students category sold out: ", tickets)
record.append(tickets)
print(record)
print(tickets)
