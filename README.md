# Portfolio-project4-restaurant-booking
Le fleur fictive restaurant website with booking system.
 
## Table of contents

* [About this project](https://github.com/jossansik/Portfolio-project4-restaurant-booking#About-this-project)
* [Technology](https://github.com/jossansik/Portfolio-project4-restaurant-booking#Technology)
* [Setup](https://github.com/jossansik/Portfolio-project4-restaurant-booking#Setup)
* [UX design](https://github.com/jossansik/Portfolio-project4-restaurant-booking#UX-design)
* [Features](https://github.com/jossansik/Portfolio-project4-restaurant-booking#Features)
* [Site owners goals](https://github.com/jossansik/Portfolio-project4-restaurant-booking#Site-owner-goals)
* [User goals](https://github.com/jossansik/Portfolio-project4-restaurant-booking#User-goals)
* [User experience](https://github.com/jossansik/Portfolio-project4-restaurant-booking#User-experience)
* [Testing](https://github.com/jossansik/Portfolio-project4-restaurant-booking#Testing)
* [Bugs](https://github.com/jossansik/Portfolio-project4-restaurant-booking#Bugs)
* [Validator testing](https://github.com/jossansik/Portfolio-project4-restaurant-booking#Validator-testing)
* [Accessibility](https://github.com/jossansik/Portfolio-project4-restaurant-booking#Accessibility)
* [Deployment](https://github.com/jossansik/Portfolio-project4-restaurant-booking#Deployment)
* [Credits](https://github.com/jossansik/Portfolio-project4-restaurant-booking#Credits)

## About this project

This project is a "Full-Stack Toolkit"-site based on business logic used to control a centrally owned dataset. Authentication mechanisms and role-based access determine admin handling of the site's data or provided activites for the users.

For this project I have designed and built a website for a fictive restaurant with it’s own booking system. The user gets to interact and register for the service of booking a table and can also cancel their reservation. Tables as well as the menus are handled within the database which provides staff with the abitily to organize their activities in a flexible way.

The Restaurant's home page is created as a sort of landing page with a single call to action and the ambition to make people book tables and visit the restaurant. It has been customized for the user experience in regards to content, design, structure and copy, and feature a fully functional Python+Django based booking system with admin site.

## Technology

This project is built with Python+Django, JavaScript (Jest as testing library), HTML & CSS (with Bootstrap 5), using [Heroku Postgres](https://www.heroku.com/postgres) as relational database. The application is run, operated and deployed through Heroku.

Images and media are uploaded and stored through [Cloudinary](https://cloudinary.com). 

## Setup
The project is deployed through [Heroku](https://heroku.com) and accessed at https://restaurant-lefleur.herokuapp.com/.

## UX design

A thorough compilation of the UX design work process for this project, from research materials to design, is found in [this](https://www.figma.com/file/vUAdTR0Jn5mYmqFcJwIQYa/RESTAURANT-BOOKING-SYSTEM?node-id=0%3A1) FigJam file.

All wireframes, design specs & images can be found in [this](https://www.figma.com/file/MRf2HQrf1NJxT0Mxkty4Xj/Restaurant-booking-system?node-id=0%3A1) Figma file

Link to Figma booking flow prototype is found [here](https://www.figma.com/proto/MRf2HQrf1NJxT0Mxkty4Xj/Restaurant-booking-system?node-id=20%3A238&scaling=scale-down&page-id=0%3A1&starting-point-node-id=20%3A238)

![first_sketches](https://user-images.githubusercontent.com/92020968/181245006-a37a1891-585e-4b4d-95ae-06292d6e29b1.png)

The wireframes below show the start page design throughout different devices (responsivity with mobile first design).

![wireframes_devices](https://user-images.githubusercontent.com/92020968/181277225-5ca1ed31-32df-4a60-90ea-ca659779d90a.png)

The flowchart below show the booking process

![booking_flowchart](https://user-images.githubusercontent.com/92020968/181629154-87f7b84f-e9b4-405e-8cea-b2267c8afda6.png)

The mockups below show the booking flow design

![booking_flow](https://user-images.githubusercontent.com/92020968/181254576-1bf3fe52-99f4-477b-93df-84f370703570.png)

The mockups below show the menu pages designs

![menu_mockups](https://user-images.githubusercontent.com/92020968/181278758-71ca3a3f-2e72-4297-b035-fcb259cb118e.png)

Business Vision:

Description: The vision is to create a restaurant booking platform for restaurant guests as well as owners to simplify the process for booking tables. In the impact map and flow chart below, I have described the goals, actions & impacts for two different target groups for this app. The goal applies to both groups, ie increased number of tables booked. 

Target Groups: restaurant guests / restaurant owners & staff.

Needs: simple booking & finding info / easy management.

Business goals: helping people make and manage bookings / increase number of booked tables & visitor rates.

Product: restaurant booking app/plattform.

The impact map below is based on the Business Vision
![impact map](https://user-images.githubusercontent.com/92020968/181255327-e329e546-adfe-4727-9445-b1038eff087c.png) 

The chart below show outcome, action & result and is based on the Business Vision
![booking_system_flowchart1](https://user-images.githubusercontent.com/92020968/181255488-80750f1f-cb7c-4aed-ba13-1200961c7168.png)

## Features

Features for [website](https://restaurant-lefleur.herokuapp.com/):
- Guests can register for an account to reserve tables
- Guests can see food & drinks menus
- Logged in guests can make time/date-based reservation
- Logged in guests can view their reservation
- Logged in guests can cancel their reservation

Features for (staff) [adminwebsite](https://restaurant-lefleur.herokuapp.com/admin)
- Can manage tables
- Can manage reservations (CRUD + confirm reservation)
- Can manage menus
- Can manage menu items

Features for (superadmin) [adminwebsite](https://restaurant-lefleur.herokuapp.com/admin)
- Has full access to system and can therefore manage staff.
- Can manage groups for staff with restrictions for tables/reservations/menus/menu items

## Site owners goals

### Super admin goals

- Create staff member as super administrator:

![Create staff member](https://user-images.githubusercontent.com/92020968/181730923-cb622079-5468-4817-a10c-34b84e77bf45.png)

- Create a group (staff) with restrictions for tables/reservations/menus/menu items:

![Create staff group](https://user-images.githubusercontent.com/92020968/181730866-c56ae405-ee0b-469a-8e7e-b1609269a2b0.png)

- Add staff member to group (staff):

![Add staff member to group](https://user-images.githubusercontent.com/92020968/181731210-29579afc-cff0-44e6-9508-184f95d53b4a.png)

### Staff goals
- Manage tables:

![Tables](https://user-images.githubusercontent.com/92020968/181730089-a2febf21-1974-4911-9acc-d5491631203e.png)

![Change table](https://user-images.githubusercontent.com/92020968/181730298-4072e727-3830-48f6-b156-173ab312a680.png)

- Manage reservations (Confirm booking):

![List reservations](https://user-images.githubusercontent.com/92020968/181732517-009e0f03-29f0-4abe-9fad-a3870813c0ae.png)

![Reservations](https://user-images.githubusercontent.com/92020968/181730173-4525cf82-1276-4569-b943-18de9168e96e.png)

- Manage menus:

![List filer menus](https://user-images.githubusercontent.com/92020968/181732024-aea7b99f-6a48-4d3f-9e8e-6a0b95e9694d.png)

![Add menu](https://user-images.githubusercontent.com/92020968/181731621-e94b4bad-1bc9-45f3-883b-d9285e1a78ba.png)

- Manage menu items:

![List filter menu items](https://user-images.githubusercontent.com/92020968/181732203-3e1e6400-acfe-42c6-903b-55a804bc2be6.png)

![Add menu item](https://user-images.githubusercontent.com/92020968/181731685-bc7e0bf1-2d37-4018-9607-9eb6f693b487.png)

## User experience

- First page:

![First page](https://user-images.githubusercontent.com/92020968/181742483-00149986-d6ae-4ad5-b478-deb476844e61.png)

- Navigation menu in logged in state:

![Header logged in](https://user-images.githubusercontent.com/92020968/181748737-38d839bf-8591-4481-a42e-d915cbe5bbcc.png)

- Navigation menu when not logged in:

![Header not logged in](https://user-images.githubusercontent.com/92020968/181748863-89955f79-7293-47b1-989a-c639f74b3899.png)

- Logout confirmation:

![Logout confirmation](https://user-images.githubusercontent.com/92020968/181749220-a4f964b5-02e1-415e-ba12-c59b9cdf00d7.png)

- Drinks menu:

![Drinks menu](https://user-images.githubusercontent.com/92020968/181749476-f4b13b4f-f5f9-4677-bdeb-db2896cde509.png)

- Food menu:

![Food menu](https://user-images.githubusercontent.com/92020968/181749595-41c9a90c-2438-4e36-8e55-935bbfbd77e4.png)

### Reservation flow

- 'Book a table' takes the guest to log in page and in case they don't have an accout they will have to register:

![Book_table_login_register](https://user-images.githubusercontent.com/92020968/181743347-c3033d7a-cba4-47b4-aa5f-ffbd86b153c7.png)

- 'Book a table' register page will redirect the guest to booking page after registration:

![Booking register](https://user-images.githubusercontent.com/92020968/181743502-1e343f2c-bce5-4836-a8d8-5f7817f0f6e1.png)

- Pick date and number of guests to get available times:

![Book a table step 1](https://user-images.githubusercontent.com/92020968/181743943-4f2e7407-14fb-4dce-b652-d10fec7fa130.png)

Datepicker:

![Book a table step 1 datepicker](https://user-images.githubusercontent.com/92020968/181744121-63dc5004-7c66-4cbe-8e1b-74af96b13ab7.png)

Number of guests dropdown:

![Book a table step 1 select guest count](https://user-images.githubusercontent.com/92020968/181744215-82a1e8d7-bbc3-434d-a8e9-a757a5655efe.png)

- Guest can pick a time or repick date and number of guests and can see if certain times are fully booked:

![Book a table step 1 pick time booked](https://user-images.githubusercontent.com/92020968/181745819-cb8fe399-5d8e-4e84-b7a0-b18aaa54be98.png)

- Guest views details and fills in the name that will be on the reservation:

![Book a table step 2 name and view details](https://user-images.githubusercontent.com/92020968/181744846-61fa9b58-a7be-4a59-8636-a003f27252f5.png)

If the guest already has made a reservation it is not possible to make another one without cancelling the first:
![Book a table step 2 user already has a reservation](https://user-images.githubusercontent.com/92020968/181745989-1a5c3630-eff5-4d8f-9443-ed408c6b058c.png)

If a table is beeing booked before user place their reservation this message will show (it is also not possible to tinker with the url to bypass it if the table is already booked):

![Book a table step 2 alread reserved](https://user-images.githubusercontent.com/92020968/181747163-d57ae2de-1c67-478e-a7a9-9d8ddca2d629.png)

- Upon clicking on place reservation the guest gets redirected to this page:

![Book a table step 3 success](https://user-images.githubusercontent.com/92020968/181745351-17af209c-e6c8-4fd6-9998-e6d43d11e745.png)

- Guest can view their reservation:

No active reservation:

![No active reservation](https://user-images.githubusercontent.com/92020968/181746846-755fc507-b592-40c1-8785-3e52e30edf53.png)

Active reservation:

![View my reservation](https://user-images.githubusercontent.com/92020968/181746341-1c2005dc-c73f-4bbd-a457-73ecda0b8db6.png)

- Guest gets a confirmation message upon clicking cancel reservation:

![Cancel reservation confirmation](https://user-images.githubusercontent.com/92020968/181746490-7382a3f3-9679-4fd0-9a13-81f13e048ba3.png)

- Guests gets a message when the cancellation is completed:

![Cancelled reservation](https://user-images.githubusercontent.com/92020968/181746619-8637cc53-0153-4499-a209-16ddc661918b.png)

## Testing

Python tests is located in restaurant_app/tests.py and tests mostly functions in services.py.

Tests for table reservations is located in: ReserveTableTest.
1. test_guest_can_reserve_available_table
  This tests that a guest can reserve an available table with allowed capacity in specified date and time.
2. test_guest_cannot_reserve_booked_table_at_fully_booked_time
  This tests that a guest cannot reserve a table which is fully booked at specific date and time.
3. test_guest_cannot_reserve_table_without_capacity
  This tests that user cannot reserve a table which does not fullfil the capacity of the guest count.
4. test_guest_cannot_have_multiple_active_reservations
  This tests that a user cannot have multiple reservations in future date and time.
5. test_guest_can_have_a_previous_reservation_and_make_a_new
  This tests that a user can reserve a table even though he/she got a reservation in previous date and time.

Tests for reservation timeslots can be found in: ReservationTimesTest.
1. test_guest_can_list_reservations
  This tests that a guest can receive a list of reservation timeslots.
2. test_guest_can_view_available_table_for_timeslots
  When there are multiple tables with requested capacities,
  Only one table is reserved by a guest,
  Guest should be able to reserve available table.
3. test_guest_can_view_reserved_timeslots
  This tests that a guest can see reserved and available tables.

Tests for menu and menu items can be found in: MenusTests.
1. test_get_menu_with_items_in_position
  This tests that the created menu and the menu items is received as expected.
  With a connection between menu and menu item and with the correct position ordering.

Javascript tests is located in static/scripts/__tests__/.

Tests for booking cancellation is located in: myreservation.test.js.
Cancel reservation tests/
1. Click on cancel reservation/Expects confirmation modal to show
  This tests that jquery is triggering a confirmation dialog to open.
2. Click on 'Yes' in confirmation modal/Expects modal to show
  This tests that jquery is triggering a form submit action and closing modal dialog.
3. Click on 'No' in confirmation modal
  This tests that jquery is triggering a close of confirmation dialog.

## Bugs

## Validator testing


## Accessibility


## Deployment




## Credits
Wireframes and mockups, as well as images and vectors used on the website were made using [Figma](https://figma.com/)

Flowcharts were made using [FigJam](https://figma.com/figjam)

The menu page icons are from [The Noun Project](https://thenounproject.com/)
