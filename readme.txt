Solent trip system demonstrates ICONIX process for software design and object-oriented design.

Solent trip is a dektop application using Python and Tkinter for GUI

The program run 'run.bat' file or 'system.py' file (enter 'admin' for admin menu, 'man1' for the manager menu, 'coo' for the coodinator menu).

The system has the following features and users:
(a) Trip
A trip has a name, a start date and consists of multiple travellers and trip legs. Each trip will always have a contact, the trip coordinator, who is in-charge and manages the trip. Depending on the number of travellers, the trip may also have multiple support staff to assist with the trip. In terms of duration, a trip may be a one-day trip, a weekend (Friday evening to Sunday evening) trip, or a fortnight trip.
(b) Traveller
A traveller has a name, an address, date of birth, and an emergency contact. Each traveller will have at least one valid form of government id (a passport, driving license, national identity card, etc.) with details of the id stored in the system.
(c) Trip Leg
A trip leg is a part of the trip and will have a starting location, a destination, a transport provider, and a mode of transport. The starting location and destination can be a place to stay (e.g., a hotel, bed & breakfast, etc.), a point of interest (such as a museum, historical site, etc.) or a transfer point (e.g., an airport, a ferry port, etc.). The mode of transport will be a plane, ferry, coach, or taxi.
(d) System Users
Users are the system actors who will carry out different activities using the system. The system users are considered in three categories as follows:
1. Trip Coordinator
A trip coordinator is associated with a trip and will be able to carry out basic functionalities in the system. These include:
i. Create, view, and update the passengers for a trip.
ii. Create, view, and update the trips legs for a trip.
iii. Generate an itinerary for the trip.
iv. Take payments on behalf of passengers and generate a receipt
v. Print invoices and receipts for any payments that have been made.
2. Trip Manager
A trip manager will be able to complete all user tasks as stated above and, 
