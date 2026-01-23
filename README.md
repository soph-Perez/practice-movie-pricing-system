**Objective:** 
Write a Python program that calculates the price of a movie ticket based on a customer’s age and membership status. Use Enum to represent ticket categories or pricing tiers to prevent invalid states. Include input validation for age and membership status. 

**Requirements:** 
1. **Enum Definition:**
   * Create an Enum called TicketType with these members: * CHILD * ADULT * SENIOR * MEMBER_DISCOUNT
2. **Input Validation:**
   * Function get_age() that asks the user for their age and ensures it’s a positive integer.
   * Function get_membership_status() that asks if the user is a member (yes/no) and validates the input.
3. **Ticket Pricing Logic:**
   * Age < 12 → CHILD ticket
   * Age 12–59 → ADULT ticket
   * Age ≥ 60 → SENIOR ticket
   * If the user is a member, they automatically get MEMBER_DISCOUNT (overrides age category).
4. **Display Results:**
   * Show the ticket type and corresponding price:
   * CHILD → $5
   * ADULT → $12 '
   * SENIOR → $8
   * MEMBER_DISCOUNT → $7 5.

   **Program Structure:**
   * Use separate functions for input, determining ticket type, and displaying results.
   * Use Enum for ticket types to avoid illegal states. * Include a main() function that ties everything together. 
