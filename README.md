IranBNB
IranBNB is a web platform that allows Iranian users to search and book accommodations worldwide using Airbnb data, all while offering a localized experience. Built with Django for the backend and HTMX for the frontend, this platform allows users to find and reserve properties across the globe, directly integrating with Airbnb's listings.

Features:
Global Property Listings: Search Airbnb properties from around the world, tailored for Iranian users.
Real-Time Search & Reservation: Use live Airbnb data to search for available accommodations and make bookings directly.
Localized User Interface: Designed with Persian language support and Iranian preferences in mind.
User-Friendly Frontend: The platform uses HTMX for fast and dynamic updates without full page reloads, ensuring a smooth user experience.
Booking Management: Ability for users to manage their reservations and track booking details.
Secure Payment Gateway: Integration with a local payment system for Iranians to book global accommodations seamlessly.
Ratings and Reviews: See Airbnb reviews to help users make informed decisions.
Tech Stack:
Backend: Django (Python)
Frontend: HTMX, HTML, CSS (Responsive design)
Database: PostgreSQL
External Data: Integrated with Airbnb's public APIs for real-time accommodation data.
Payment System: Local Iranian payment gateway integration.
Getting Started:
To set up the project locally, follow these steps:

Clone the repository.
Install dependencies by running pip install -r requirements.txt.
Set up the database and configure API keys for Airbnb.
Run the app locally using Django’s development server: python manage.py runserver.
Contributing:
We welcome contributions to IranBNB! Whether you’re adding features, fixing bugs, or improving documentation, your help is appreciated. Please fork the repository and submit pull requests with your changes.


Task List
Setup & Project Initialization
-[x] Set up a new Django project.
-[x] Initialize a GitHub repository for the project.
-[x] Create a virtual environment for development.
-[x] Install necessary Django packages and dependencies.
-[x] Set up version control with Git.
Backend Development (Django)
-[x] Set up Django models for users, bookings.
-[ ] Integrate Airbnb API to fetch accommodation data.
-[ ] Create views and APIs for searching properties (location, price, etc.).
-[ ] Implement user authentication (sign-up, login, password reset).
-[ ] Set up a booking system allowing users to reserve accommodations.
-[ ] Create a reservation management system (view, edit, cancel bookings).
-[ ] Implement secure payment integration for Iranian users.
-[ ] Set up Django Admin for managing accommodation listings and bookings.
Frontend Development (HTMX)
-[ ] Create a responsive design for the frontend using HTML/CSS.
-[ ] Integrate HTMX for dynamic content loading (e.g., search results, filters).
-[ ] Design and implement the homepage, property search page, and booking page.
-[ ] Add Persian language support for the user interface.
-[ ] Implement real-time search filters for property listings (e.g., location, price, amenities).
-[ ] Implement user dashboard for managing bookings and profile.
Integration & Testing
-[ ] Test Airbnb API integration for retrieving accommodation data.
-[ ] Test booking functionality and reservation management system.
-[ ] Test the user authentication flow (sign-up, login, password reset).
-[ ] Ensure mobile responsiveness and compatibility.
-[ ] Write unit and integration tests for key features.
-[ ] Set up Continuous Integration (CI) for automated testing.
Deployment & Launch
-[ ] Set up a production environment (e.g., deploy on Heroku, AWS).
-[ ] Configure domain and hosting.
-[ ] Implement error logging and monitoring.
-[ ] Deploy the application and ensure smooth functionality.
-[ ] Promote the launch of the platform to potential users.
Documentation & Contribution
-[ ] Update GitHub README with project description, setup instructions, and task list.
-[ ] Create contribution guidelines for developers interested in contributing.
-[ ] Document the API endpoints and their usage.
-[ ] Write a detailed user guide for navigating the platform.