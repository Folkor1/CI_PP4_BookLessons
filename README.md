# Booking Piano

**Developer: Igor Vasiljev**

[Link to the live project](https://booking-app-pp4.herokuapp.com/)

![logo](static/images/all-devices-black.png)

## About

The app represents a booking system for piano and theory lessons with online or offline options. Features include booking, amending and cancelling booked lessons, as well as keeping record of all past lessons.
It's also possible for admin user to access bookings stats.

## Table of Contents

  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Manual](#user-manual)
  - [User Stories](#user-stories)
    - [Users](#users)
    - [Site Owner](#site-owner)
  - [Technical Design](#technical-design)
    - [Flowchart](#flowchart)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks & Tools](#frameworks--tools)
    - [Libraries](#libraries)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Automation Testing](#automation-testing)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals

- Ability to book a lesson.
- Amend lesson date and type.
- Cancel booked lesson.
- Access information of all past bookings.

### Site Owner Goals

- Be able to keep track of all upcoming lessons.
- Access information of all past bookings using filter.

## User Experience

### Target Audience

- Beginner or experienced musicians of all age levels.
- Everyone who's interested in theory of music and learning piano playing.
- Who require flexibility of online/offline lesson types.

### User Requirements and Expectations

- Intuitive navigation.
- Responsive design.
- Easy way to book, amend and cancel booking.
- Access records associated with the account.

## User Stories

### Users

1. As a user I can access the home page so that general site information can be viewed.
2. As a user I can use navigation so that site pages can be viewed.
3. As a user I can navigate to About page so that useful information can be viewed.
4. As a user I can access Sign Up menu so that it's possible to create an account.
5. As a user I can access the login menu so that it's possible to log in to the site.
6. As a user I can view the social media links so that social media can be accessed.
7. As a user I can see the lesson options so that piano or theory lesson can be selected.
8. As a user I can see the lesson types so that online or offline type can be selected.
9. As a user I can access the date and time picker so that time & date can be selected.
10. As a user I can access bookings management page.
11. As a user I can click Change date & time button so that new date & time can be selected.
12. As a user I can use Change type menu so that lesson and its type can be changed.
13. As a user I can click Cancel button so that booked lesson can be cancelled.
14. As a user I can access upcoming bookings section so that upcoming bookings can be viewed.
15. As a user I can access View my past bookings button so that past bookings can be viewed.

### Site Owner

16. As an admin I can access Admin button so that admin information can be viewed.
17. As an admin I can view the admin panel.
18. As an admin I can view the completed lessons page so that completed lessons search can be used.
19. As an admin I can access the upcoming lessons page so that the upcoming lessons can be viewed.

[Back to Table Of Contents](#table-of-contents)

## Technical Design

### Structure

The app has the following structure: navigation bar on top, footer on bottom - visible accross all app pages, and the content/functionality are in between.

Common app's pages:
- Home: contact details, location, schedule, general information and link to Bookings page.
- About: just some useful information about what to expect from lessons.
- Bookings: option to select piano/theory lessons, option to select online/offline, select date and time. Upcoming bookings and Manage bookings link are available on this page.
- Manage bookings: change date, change type or cancel lessons are available on this page, and also link to Past bookings section.
- Past bookings: list of all past bookings with details (date, time, lesson, type).
- Login: login input fields.
- Sign Up: sign up input fields.
- Pages 400, 403, 404, 500

Admin only pages:
- Admin panel: booking stats, links to completed and upcoming lessons:
- Completed lessons: list of all completed lessons for all students, filter is used.
- Upcoming lessons: list of all upcoming lessons for all students.

### Database

- Database consists of 3 models - User, Bookings and About.
- PostgreSQL is used as a database management system.
- Models were built using Django framework. 

<details><summary>Database</summary>

![Database](static/images/str.JPG)

</details>

### User model
Contains user-related data: 
- Nickname 
- Email
- Password

### Bookings model
This model contains: 
- Lesson
- Lesson type
- Date
- Time
- Lesson status
- User as a foreign key

### About model
Contains:
- Title
- Text
- Image

## Technologies Used

### Languages

- HTML
- CSS
- JavaScript
- Python

### Frameworks

- Django

### Libraries and Tools

- [Bootstrap 5.1](https://getbootstrap.com/) was used as CSS framework
- [Claudinary](https://cloudinary.com/) as static files management system
- [dbdiagram.io](https://dbdiagram.io/) as database diagram design tool
- [Font Awesome](https://fontawesome.com/) as a toolkit for icons
- [GitHub](https://github.com/) as a repository for the project code
- [Heroku](https://www.heroku.com/) to deploy the project
- [jQuery](https://jquery.com/) as a JS library was used to manipulate the DOM
- [PostgreSQL](https://www.postgresql.org/) as a database management system


