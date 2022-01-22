# Booking App
## By Clayton File

![BookingAppHomepage](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/homepage.png)

## Table Of Contents
1. [Intro](#intro)
2. [Structure](#structure)
3. [Technologies](#technologies)
4. [Bugs & Fixes](#bugs--fixes)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)

## Intro
A Heroku based mobile phone / device repair slot booking app.

### Design

The Design ideas are from the existing company Geco Tech Network ( With Permission ) and adapted the app to match their current layout and colour scheme.
Their website can be found here:
- [Geco Tech Network](https://geco-tech.net/)

### Colours
We maintained the same colour pallete throughout to maintain consistency and ensure the website was a matching colour scheme to the existing Geco Tech Website. The green throughout the website is:
```
#96C345
```

## Structure

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

### Goals

- To enable the user to book their repair time slot without the need to call and arrange.
- To enable the admin / company employee to check booked appointments backend.

### Audience

- The application is aimed at potential customers needing to repair their device and book a time slot.

## Technologies

### Languages

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [Jquery](https://en.wikipedia.org/wiki/JQuery)

### Other

- [Django Web Framework](https://en.wikipedia.org/wiki/Django_(web_framework))
- [Heroku](https://en.wikipedia.org/wiki/Heroku)
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/)
- [Cloudinary](https://cloudinary.com/)
- [psycopg2](https://pypi.org/project/psycopg2/)
- [PostgreSQL](https://www.postgresql.org/)

## Bugs & Fixes

- Given more time i would have greyed out unavailable date and times and came up with a cleaner solution.

## Testing

![Flow Chart](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/flowchart.png)
- [Flow Chart](https://lucid.app/)

![Lighthouse](https://github.com/TechCentreUK/Booking-System/blob/main/readme_images/testing_results/lighthouse.png)
- [Google Chrome Lighthouse](https://developers.google.com/web/tools/lighthouse)
Lighthouse was used to ensure performance, best practices and colours didnt prevent readability. There was a few factors which doesnt allow the score to add up to 100% including no HTTPS connection with heroku.

During the build of my project i was testing code back and forth when making changes to ensure everything works as it should, for example i had to make sure a date and time could not be double booked and alerted the user with an error message if the date and time was already booked. Given more time i would have made some changes and removed time slots that was booked and refused older dates from being selected.
![Error Message](https://github.com/TechCentreUK/Booking-System/blob/main/booking_app/readme_images/time-slot-error.png)

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
![HTML Validator](https://github.com/TechCentreUK/Booking-System/blob/main/testing-results/booking-html-validator.png)
[HTML Validator](https://validator.w3.org/#validate_by_input)

### CSS Validator
CSS Validator was used, by copying and pasting css into W3C CSS Validator / Jigsaw.
![CSS Validator](https://github.com/TechCentreUK/Booking-System/blob/main/testing-results/css-validator.png)
[CSS Validator](https://jigsaw.w3.org/css-validator/validator)

### PEP8 validator
[PEP8 Online](http://pep8online.com/) was used to check if python was pep8 compliant.
![PEP8](https://github.com/TechCentreUK/Booking-System/blob/main/testing-results/pep8.png)

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
8. Navigate to the "Deploy" section.
9. Scroll down to "Deployment Method" and select "GitHub".
10. Authorize the connection of Heroku to GitHub.
11. Search for your GitHub repository name, and select the correct repository.
12. For Deployment there are two options, Automatic Deployments or Manual.
    - Automatic Deployment: This will prompt Heroku to re-build your app each time you push your code to GitHub.
    - Manual Deployment: This will only prompt Heroku to build your app when you manually tell it to do so.
13. Ensure the correct branch is selected "master/Main", and select the deployment method which suites you.

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