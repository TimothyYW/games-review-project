# Game review website

![Website logo](../games-review-project/static/images/Logo.png)

Welcome to the game review website where user could review their favorite or least favorite game, The app design to allowed user to leave review of their game of choice depending on title, type of game, and developer

![Mock test](../games-review-project/static/images/Mock-up-test.png)

[Link for Heroku](https://game-review-d934f4a1894a.herokuapp.com/)
[Link for gitpod](https://8000-timothyyw-gamesreviewpr-vtsz4t7mvui.ws-eu110.gitpod.io/)

# Table of Content


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