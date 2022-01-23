# Booking App
## By Clayton File

![Am I Responsive](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/testing_results/responsive.png)
![BookingAppHomepage](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/homepage.png)

## Table Of Contents
1. [Intro](#intro)
2. [Structure](#structure)
3. [Skeleton](#skeleton)
4. [Surface](#surface)
5. [Technologies](#technologies)
6. [Bugs & Fixes](#bugs--fixes)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Credits](#credits)

## Intro
A Heroku based mobile phone / device repair slot booking app.

### Goals

- To enable the user to book their repair time slot without the need to call and arrange.
- To enable the admin / company employee to check booked appointments backend.

### Audience

- The application is aimed at potential customers needing to repair their device and book a time slot.

### User Stories
Using Github "Issues" and "Projects" User stories are created to get a basic understanding of different users needs.
- [Issues](https://github.com/TechCentreUK/Booking-System/issues)
![Issues](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/issues.png)

- [Projects](https://github.com/TechCentreUK/Booking-System/projects/1)
![Projects](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/projects.png)

- Customers / Site Users
* As a user, I am able to access the site on my mobile, tablet, and desktop which is adapted to provide the best experience.
* As a Customer i can log in so that I can edit or delete my booking.
* As a Customer i can make a booking so that i can book a time slot for getting my device repaired.
* As a Customer i can reset my password by email so that i can reset without the need to contact admin.
* As a user i can easily navigate through the website without too much thought so that i can find what I'm looking for quickly.
* As a user i can easily identify what the website is about so that i know what it has to offer.

- Admin
* As a Admin i can Sign in backend so that i can view, edit and delete customer bookings.
* As a Admin i can add new bookings backend so that telephone and walk in customers can get booked in.

### Features:

* Website information clearly relayed upon entering the home page.
* Responsive Design - Site should function on mobile, tablet and desktop/laptop devices.
* Mobile and desktop navigations.
* Create Bookings qith unique time slots.
* Manage, Edit and Delete Bookings.

## Structure
- User Story:
```
As a user i can easily identify what the website is about so that i know what it has to offer.
```

Acceptance Criteria:

Heading displayed on the main page with clear inforation on the sites purpose.

Implementation:

The Home Page will contain the main website title of "Phone Repair Booking Form".
The visitor will be met with the information on the general purpose of the site immediately.

- User Story:
'''
As a Customer i can log in so that I can edit or delete my booking.
'''

Acceptance Criteria:

The sites pages will be met with the need to login before any bookings can be made or seen.

Implementation:

The "Book Now" and "My Bookings" will be innaccessable without first logging in and will be met with a login page. Users will also be able to click the login page from the top bar.

## Skeleton

### Wireframes
I had a live version of a wireframe to use as the website was structured to fit in with the style and theme of Geco Tech Network website.
![Geco Tech Website](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/geco-tech.png)

### Homepage
![Homepage](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/wireframes/home-wireframe.png)
### Booking Form
![Booking Form](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/wireframes/book-a-repair-wireframe.png)
### My Bookings
![My Bookings](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/wireframes/my-bookings-wireframe.png)
### Login
![Login](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/wireframes/login-wireframe.png)
### Register
![Register](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/wireframes/register-wireframe.png)
### Reset Password
![Reset Password](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/wireframes/reset-password-wireframe.png)

### Database Design
![Database Diagran](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/database.png)

- Security
Using config variables in heroku, all SECRET access keys are stored safely to prevent unwanted connections to the database.

## Surface
Typography
The site is using font-family Roboto with a backup of sans serif.


### Design

The Design ideas are from the existing company Geco Tech Network ( With Permission ) and adapted the app to match their current layout and colour scheme.
Their website can be found here:
- [Geco Tech Network](https://geco-tech.net/)

### Colours
We maintained the same colour pallete throughout to maintain consistency and ensure the website was a matching colour scheme to the existing Geco Tech Website. The green throughout the website is:
```
#96C345
```

## Technologies

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
* This project was created using Python framework Django following Model-View-Template design
* Python Modules used (These can be found in the requirements.txt project file):
```
asgiref==3.4.1
boto3==1.20.24
botocore==1.23.24
cloudinary==1.28.0
dj-database-url==0.5.0
dj3-cloudinary-storage==0.0.6
Django==3.2.9
django-crispy-forms==1.13.0
django-phone-field==1.8.1
django-phonenumber-field==6.0.0
django-ses==2.3.1
future==0.18.2
gunicorn==20.1.0
jmespath==0.10.0
phonenumberslite==8.12.39
psycopg2==2.9.2
pytz==2021.3
s3transfer==0.5.0
sqlparse==0.4.2
whitenoise
```
- [HTML](https://en.wikipedia.org/wiki/HTML)
* This project uses HTML as the main language used to complete the structure of the Website.
- [CSS](https://en.wikipedia.org/wiki/CSS)
* This project uses custom written CSS to style the Website and some Bootstrap
- [Jquery](https://en.wikipedia.org/wiki/JQuery)
* Jquery was used to load the Modals.
- [Boostrap](https://getbootstrap.com/)
* The Bootstrap framework was used through the website for layout and responsiveness.
- [Django Web Framework](https://en.wikipedia.org/wiki/Django_(web_framework))
* The python web framework.
- [Heroku](https://en.wikipedia.org/wiki/Heroku)
* Heroku was used to deploy the live website.
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/)
* Google chromes built in developer tools are used to inspect page elements and help debug issues with the site layout and test different CSS styles.
- [Balsamiq](https://balsamiq.com/wireframes/)
* This was used to create wireframes for the 'Skeleton' Section above.
- [DBVisualizer](https://www.dbvis.com/)
* This was used to create the Database Diagram.
- [Cloudinary](https://cloudinary.com/)
* Used to store and style the site logo.
- [psycopg2](https://pypi.org/project/psycopg2/)
* Psycopg2 is a DB API 2.0 compliant PostgreSQL driver.
- [PostgreSQL](https://www.postgresql.org/)
* PostgreSQL was used to create the relational databases used as data storage for this project.
- [GitHub](https://github.com/)
* GitHub is the hosting site used to store the source code for the Website.
- [Google Fonts](https://fonts.google.com/specimen/Roboto?query=roboto#standard-styles)
* Google fonts are used throughout the project to import the Orbitron and Roboto fonts.

## Bugs & Fixes

- Given more time i would have greyed out unavailable date and times and came up with a cleaner solution.
- You cannot edit currently with the same time slot. This is to be fixed in the future.

## Testing

![Flow Chart](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/flowchart.png)
- [Flow Chart](https://lucid.app/)

![Lighthouse](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/testing_results/lighthouse.png)
- [Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse)
Lighthouse was used to ensure performance, best practices and colours didnt prevent readability. There was a few factors which doesnt allow the score to add up to 100% including no HTTPS connection with heroku.

During the build of my project i was testing code back and forth when making changes to ensure everything works as it should, for example i had to make sure a date and time could not be double booked and alerted the user with an error message if the date and time was already booked. Given more time i would have made some changes and removed time slots that was booked and refused older dates from being selected.
![Error Message](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/time-slot-error.png)

Another important piece of testing was to ensure a user cannot see other users bookings and vice versa and only the admin panel could see the full bookings. To test this i had to create a couple accounts and create bookings and then check the users 'my bookings' page and make sure i could only see the bookings dedicated to the signed in user. You can see below we passed the user foreign key in our model the related_name of 'hiuser' which allowed us to filter through in our views.py

## models.py
```
user = models.ForeignKey(User, default='', null=True, on_delete=models.CASCADE, related_name='hiuser')
```
## views.py
```
def my_bookings(request):
    """ My Bookings Page """
    if request.user.is_authenticated:
        bookings = request.user.hiuser.all()
        context = {
            'bookings': bookings
        }
        return render(request, 'booking_app/my-bookings.html', context)
    else:
        return redirect('/login/')
```

### HTML validator
HTML Validator was used to ensure best practices. I viewed the page source and copy and pasted into the HTML validator to confirm this.
![HTML Validator](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/testing_results/booking-html-validator.png)
[HTML Validator](https://validator.w3.org/#validate_by_input)

### CSS Validator
CSS Validator was used, by copying and pasting css into W3C CSS Validator / Jigsaw.
![CSS Validator](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/testing_results/css-validator.png)
[CSS Validator](https://jigsaw.w3.org/css-validator/validator)

### PEP8 validator
[PEP8 Online](http://pep8online.com/) was used to check if python was pep8 compliant.
![PEP8](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/testing_results/pep8.png)

[Am I Responsive](http://ami.responsivedesign.is/)
![Am I Responsive](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/testing_results/responsive.png)

### Assumptions and Dependencies
Testing is dependent on the website being deployed live on Heroku.

### Access Requirements
Tester must have access to the Django Admin panel in order to manually verify the insertion of records into the databases.

### Regression Testing
Features previously tested during development in a local environment must be regression tested in production on the live website.

## Deployment

### Heroku
This application will be deployed via [Heroku](https://heroku.com)
1. Ensure all code is ready for deployment. 
2. Log into or sign up to Heroku
3. From Dashboard click "New" and select "create new app" from the drop-down menu.
4. Choose a unique but available name for your app and select your region.
5. Click "Create App".
6. Navigate to "Settings" and scroll down to "build packs".
7. Click "build packs" and then click both "python" and "node.js". Please note node.js is needed for the mock terminal and must be BELOW python on the list.
   they can be clicked and dragged to move.
8. Click on the settings tab and then click reveal config vars. Add your Variables here.
9. Navigate to the "Deploy" section.
10. Scroll down to "Deployment Method" and select "GitHub".
11. Authorize the connection of Heroku to GitHub.
12. Search for your GitHub repository name, and select the correct repository.
13. For Deployment there are two options, Automatic Deployments or Manual.
    - Automatic Deployment: This will prompt Heroku to re-build your app each time you push your code to GitHub.
    - Manual Deployment: This will only prompt Heroku to build your app when you manually tell it to do so.
14. Ensure the correct branch is selected "master/Main", and select the deployment method which suites you.

### Forking
If you wish to edit and experiment with the code you can fork the repository.
Forking a repository allows you to experiment without the original project being affected.
1. Navigate to the repository.
2. In the top right of the page, below your profile you should see a "Fork" button. Simply click on this.
3. A copy of the forked repository will then be added to your own Repositories Page.

### Clone

1. Navigate to the Github Repository you want to clone.

2. Click the drop down menu labelled "Clone".

3. Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.

4. Open your developement editor and open a terminal window in a directory of your choice.

5. Use the 'git clone' command in terminal followed by the copied git URL.

6. A clone of the project will be created locally on your local machine.

## Credits

- [Whitenoise](https://devcenter.heroku.com/articles/django-assets)
For teaching me how to install whitenoise for my static assets.

- [Stack Overflow - Modals](https://stackoverflow.com/questions/6929416/custom-confirm-dialog-in-javascript)
For teaching me how to create effective confirmation modals.

- [Ordinary Coders - Login](https://ordinarycoders.com/blog/article/django-user-register-login-logout)
- [Ordinary Coders - Password Reset](https://ordinarycoders.com/blog/article/django-password-reset)
For Teaching me how to create front end user login / logout and registration.

### Acknowledgment
I'd like to thank my mentor [Daisy McGirr](https://github.com/Daisy-McG) for her continued guidance and support throughout my project.