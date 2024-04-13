# Game review website

![Website logo](../games-review-project/static/images/Logo.png)

Welcome to the game review website where user could review their favorite or least favorite game, The app design to allowed user to leave review of their game of choice depending on title, type of game, and developer

![Mock test](../games-review-project/static/images/Mock-up-test.png)

[Link for Heroku](https://game-review-d934f4a1894a.herokuapp.com/)
[Link for gitpod](https://8000-timothyyw-gamesreviewpr-vtsz4t7mvui.ws-eu110.gitpod.io/)

# User-experience-design

## Site goals

The site is aimed to let share their option about certain games, while at the same time give information about the game that they are reviewing.

On the other hands, this site could also help developer to gain fame about their games.

## Agile planning

This site developed by the agle planning based on 3 catagories, those are Priority alpha(Must have), Priority beta(should have), and Priority charlie(could have).

Game review project was utilzing the backlog project from github which can be viewed [here](https://github.com/users/TimothyYW/projects/4/views/1). Every task has been label, with criteria that is help decided if the task is finished or undone.

![Backlog](../games-review-project/static/images/backlog.png)

## Epics 

The project had 4 main Epics (milestone):

### Epic 1 Base setup

Without the base setup the app would not existed, so the foundation of the app is really important to provide feature. From the base setup the app could expand to the intended design.

### Epic 2 Authentification 

This epic will be focusing more on the login, sign-up, and logout. User will be able to leave their review, but they are able to save the review and let others users to see the reviews.

### Epic 3 Reviewing

As the main purpose of this app is to let user to leave their review about their game of choice, whetever is it good or bad review.

### Epic 4 Deployment 

This epic will be focusing more on the deployment of the app, what feature that is provided and what are could be provided.

## User story

### Epic 1 Base setup

As a developer, I have to setup base.html as front of the app.

As a developer, I need to add navbar to showcase features of the app.

As a developer, I need to create static for the styling such as CSS and Images.

As a developer, I need to create footer to provide social media link.

### Epic 2 Authentification 

As a user, I want to be able to input my review.

As a user, I want to be able to save my review.

As a developer, I want the user who input review, provide information about who are they in term of nickname (real name is not essential).

As a developer, I want to know when do they post the review.

### Epic 3 Reviewing

As a developer, I want to know what information that user can give about the game that they reviewed.

As a developer, I want to give user freedom to write what they want about the game postive or negative.

As a user, I want to able to see other review about other games.

As a user, I want to able to add image of the game that I am reviewing.

### Epic 4 Deployment 

As a developer, I need to set up whitenoise so that my static files are served in deployment.

As a developer, I need to deploy the project to heroku so that it is available for gamers who wants to review games.

As a developer, I have to ensure all link that is provided is functional.

# Feature

## Navbar

User story: as a developer, I need to create navbar so user can navigate easily.

- Home: bringing user back to the first page.
- Reviews: allowing user to see the latest reviews.
- Input review: allosing user to input their review, but they must login or sign-up first.
- Register: allowing user to sign-up to leave their review.
- Login: if user already have account they can just login.
- Search bar: allwoing user to find specific reviews.
![Navbar](../games-review-project/static/images/navbar.png)

## Footer

User story: as a developer, I need to create a footer which include two of the famouse social media among gamers.

- Common social media = working as shortcut to the social media link.

- Gamer social media = Steam is one of the famous games ditributor, while discord is well-known as voice chat social media among gamers. Hence why it is in footer.

![Footer](../games-review-project/static/images/footer.png)

## Home page

User story: As a developer, I want user to feel welcome and know that this is the app where they can leave their review about the game.

The home page has the function from navbar with logo on the top left and description of the app.

![Home page](../games-review-project/static/images/home.png)

## Review page

User story: As a user, I want to be able to see reviews of my games or other games.

The Reviews page can be seen first just picture of the games and the name of the game.

![Review page 1](../games-review-project/static/images/Review-list.png)

The Review page can be expand as seen below allowing user to find more info about the game. This is also review from user itself.

![Review page 2 ](../games-review-project/static/images/example_review.png)

## Input/Login page

User story: As a developer, I want user to leave their reviews to be registered and listed based on the date they posted it.

The input page required user to login or register, and allowing them to save their review of the game.

![Input or login page](../games-review-project/static/images/input_option.png)

## Input Review page

User story: As a developer, I want user to be able to input their review as it is the main purpose of the app and give them option to give more information of the game.

Finally, this page is allowing the user to leave their review and give them an option to give information about the game.

![Input Review page](../games-review-project/static/images/input_review_schematic.png)

## Error page or 403 page

User story: As a developer, I want user to know if they are trying to access the page that is not available.

The error page or 403 page as mention the function to warns user that the page is not available.

# Future Feature

- Give more option than just horro, aciton, and story telling.
- Add more type of game besides single and multiplayer.
- Provide rating system up to 5 stars

# Bug

- Favicon did not show up in Heroku app

# Testing

# PEP8

## manage.py
Result:
![Manage.py test result](../games-review-project/static/images/manage.py.png)

## env.py
Result:
![env.py test result](../games-review-project/static/images/env.py.png)

## Home

### view.py
Result:
![home-view.py test result](../games-review-project/static/images/home-view.py.png)

## Profile

### models.py
Result:
![profile-models.py test result](../games-review-project/static/images/profile-models.py.png)

### admin.py
Result:
![profile-admin.py test result](../games-review-project/static/images/profile-admin.py.png)

## urls.py
Result:
![profile-urls.py test result](../games-review-project/static/images/profile-urls.py.png)

## Review

### View.py
Result:
![view.py test result](../games-review-project/static/images/view.py.reviews.png)

### urls.py
Result:
![urls.py test result](../games-review-project/static/images/urls.py.png)

### models.py
Result:
![models.py test result](../games-review-project/static/images/models.py.png)

### app.py
Result:
![app.py test result](../games-review-project/static/images/app.py.png)

### admin.py
Result:
![admin.py test result](../games-review-project/static/images/admin.py.png)

## CSS testing result:

![Testing CSS](../games-review-project/static/images/CSS_Testing.JPG)

## Technologies

- Python
- Django
- HTML/CSS
- Bootstrap
- Google Cloud Platform
- Cloudinary
- Favicon.io
- balsamiq


## Link to the website and video

- https://cdnjs.com/libraries/bootstrap - CDN for bootstrap links
- https://getbootstrap.com/docs/5.2/getting-started/introduction - Bootstrap documentation
- https://uxwing.com/ - UX Wing icons
- https://django-allauth.readthedocs.io/en/latest/installation.html - Django-Allauth
- https://django-crispy-forms.readthedocs.io/en/latest/install.html - Crispy Forms
- https://pypi.org/project/django-reorder/ - Django Reordered
- https://docs.djangoproject.com/en/4.1/topics/class-based-views/mixins/ - Django Mixins
- https://cloudinary.com/ - Cloudinary
- https://django-ckeditor.readthedocs.io/en/latest/ - CKEditor
- https://books.agiliq.com/projects/django-orm-cookbook/en/latest/query_relatedtool.html - Q Objects
- https://www.w3schools.com/howto/howto_css_modals.asp - CSS Modal
- https://www.design.com/ Logo for the website 
To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:


# Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
    - SECRET_KEY: (Your secret key)
    - DATABASE_URL: (This should already exist with add on of postgres)
    - CLOUNDINARY_URL: (cloudinary api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repositoy you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy
The app should now be deployed.