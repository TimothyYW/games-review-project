# Games Review Website

A comprehensive platform for gamers to share and discover game reviews.

![Website logo](static/images/Logo.png)

## Table of Contents
1. [Project Overview](#project-overview)
2. [UX Design](#ux-design)
3. [Agile Development](#agile-development)
4. [Features](#features)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)

## Project Overview

Games Review is a platform where users can:
- Share detailed reviews of games they've played
- Browse reviews from other gamers
- Manage their profile and review history
- Search for specific games or reviews

[Live Site](https://game-review-d934f4a1894a.herokuapp.com/)

## UX Design

### Color Scheme
- Primary Color (#6872ff): Used for buttons and important actions
- Secondary Color (#3d3d3d): Used for secondary elements
- Background Color (#000000): Main background
- Text Color (#ffffff): Main text color
- Accent Colors:
  - Success (#198754)
  - Danger (#dc3545)

### Typography
- Headings: 'Shadows Into Light', serif
- Body Text: 'Noto Serif Display', serif

### Wireframes

#### Desktop Views
![Home Page Desktop](static/images/wireframes/home-desktop.png)
![Reviews Page Desktop](static/images/wireframes/reviews-desktop.png)
![Profile Page Desktop](static/images/wireframes/profile-desktop.png)

#### Mobile Views
![Home Page Mobile](static/images/wireframes/home-mobile.png)
![Reviews Page Mobile](static/images/wireframes/reviews-mobile.png)

### Database Schema
![Database Schema](static/images/database-schema.png)

## Agile Development

### Project Goals
1. Create a user-friendly platform for game reviews
2. Implement secure user authentication
3. Enable CRUD operations for reviews
4. Provide search functionality
5. Implement responsive design

### User Stories

#### Must Have (Priority Alpha)
- As a user, I want to create an account
- As a user, I want to write and publish game reviews
- As a user, I want to view reviews from other users
- As a user, I want to search for specific games

#### Should Have (Priority Beta)
- As a user, I want to edit my profile
- As a user, I want to edit/delete my reviews
- As a user, I want to see my review history
- As a user, I want to filter reviews by genre

#### Could Have (Priority Charlie)
- As a user, I want to rate other reviews
- As a user, I want to follow other reviewers
- As a user, I want to receive notifications

[View Project Board](https://github.com/users/TimothyYW/projects/4/views/1)

## Features

### Existing Features
1. User Authentication
   - Registration
   - Login/Logout
   - Password Reset

2. Review Management
   - Create Reviews
   - Edit Reviews
   - Delete Reviews
   - View Reviews

3. Profile Management
   - Update Profile
   - View Review History
   - Profile Picture Upload

4. Search Functionality
   - Search by Game Name
   - Search by Genre
   - Search by Developer

### Future Features
1. Rating System
2. Comment System
3. Social Features
4. Advanced Search Filters

## Technologies Used

### Languages
- HTML5
- CSS3
- JavaScript
- Python 3.8

### Frameworks & Libraries
- Django 4.2
- Bootstrap 5
- Cloudinary
- PostgreSQL
- AllAuth
- Crispy Forms

## Testing

### Automated Testing
- Unit Tests: [View Results](static/images/test-results.png)
- Python Validation: [View Results](static/images/pep8-results.png)
- CSS Validation: [View Results](static/images/css-validation.png)

### Manual Testing
Detailed test cases and results are available in [TESTING.md](TESTING.md)

## Deployment

### Prerequisites
- Python 3.8+
- PostgreSQL
- Cloudinary Account
- Heroku Account

### Local Deployment
1. Clone the repository:

