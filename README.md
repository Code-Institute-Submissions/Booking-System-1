# Booking App
## By Clayton File

![BookingAppHomepage](https://github.com/TechCentreUK/Booking-System/tree/main/booking_app/templates/booking_app/images/homepage.png)

## Table Of Contents
1. [Intro](#intro)
2. [Technologies](#technologies)
3. [Bugs & Fixes](#bugs--fixes)
4. [Testing](#testing)
5. [Deployment](#deployment)
6. [Credits](#credits)

## Intro
A Heroku based mobile phone / device repair slot booking app.

### Design

-[Flow Chart]() 

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

## Bugs & Fixes

- If i had more time i would come up with a solution to not allow "expired" dates to be booked.

## Testing

- [Flow Chart](https://lucid.app/lucidchart/863b97f9-4b87-4309-9976-a84d70c8212e/edit?invitationId=inv_f650388a-840e-40cc-bb39-51531df06026)

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