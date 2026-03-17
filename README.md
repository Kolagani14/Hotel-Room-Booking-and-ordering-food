**Hotel Room Booking and ordering food**

This project is a command-line based hotel management system that allows users to book rooms and order food items. 
It simulates a basic real-world hotel booking workflow with input validation, room selection, and billing.

**🔧 Features**
**🏨 Room Booking System**
1. Collects user details (name and phone number) with validation
2. Generates a random OTP for booking confirmation

Allows selection of:
1. Floor (1–3)
2. Room (predefined room numbers)
3. Validates time input in HH:MM format
4. Displays a booking receipt with all details

**🍽️ Food Ordering System**
Menu-driven interface with options:
1. Add food items
2. View ordered items
3. Delete items
4. Exit
Uses a list to manage ordered food items dynamically

**⏱️ Billing System**
1. First hour stay is free
2. Additional hours are charged ₹100 per hour
3. Calculates total bill based on user input

**🧠 Concepts Used**
1. Input validation (isalpha, isdigit)
2. Lists for data storage
3. Loops and condition handling
4. Random OTP generation (random, string)
5. Basic time validation
6. Menu-driven programming

**⚠️ Limitations**
1. Data is not stored permanently (no database/file handling)
2. OTP is generated but not actually verified
3. Room availability is not tracked (same room can be booked multiple times)
4. Billing and food ordering are not integrated
