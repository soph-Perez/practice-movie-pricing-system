from enum import Enum, auto

class TicketType(Enum):
  CHILD = auto()
  ADULT = auto()
  SENIOR = auto()
  MEMBER_DISCOUNT = auto()

def get_age():
  while True:
    try:
      age = int(input("Enter age: "))
      if age <= 0:
        raise ValueError
      return age
    except ValueError:
      print("Invalid age input. Try again")

def get_membership_status():
  while True:
    try:
      membership_status = input("Are you a member (enter 'yes' or 'no')? ").strip().upper()
      if membership_status not in ('YES', "NO"):
        raise ValueError
      return membership_status
    except ValueError:
      print("Enter either yes or no.")

def ticket_type_pricing(status, age):
  if status == 'YES':
    return TicketType.MEMBER_DISCOUNT
  if age < 12:
    return TicketType.CHILD
  elif 12 <= age <= 59:
    return TicketType.ADULT
  else: 
    return TicketType.SENIOR

def display_result(pricing):
  if pricing == TicketType.MEMBER_DISCOUNT:
    print("Ticket Price for Member: $7")
  elif pricing == TicketType.CHILD:
    print("Ticket Price for Child: $5")
  elif pricing == TicketType.SENIOR:
    print("Ticket Price for Senior: $8")
  else:
    print("Ticket Price for Adult: $12")

def main():
  age = get_age()
  status = get_membership_status()
  pricing = ticket_type_pricing(status, age)
  display_result(pricing)

if __name__ == "__main__":
  main()