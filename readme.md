
![Logo](https://i.postimg.cc/9M1CyM4n/Screenshot-2022-08-17-at-9-39-10-PM.png)


# 
Assignments, previous year quies, exam papers and everything that you will need to master your college courses uploaded to one place!



# Demo

Watch this video for a quick demo:

**Highly recomended to watch this before going through the documentation.**
# Tech Stack

**Server:** Django 4.0.1, SQLite3

**Client:** BootStrap5, HTML, CSS, JS 




# Documentation

**1)Run Locally**

**2)Basic structure and URL paths**

**3)Database**

**4)Forms**

**5)Views**

**6)Static and Templates**

## 1)Run Locally

**Make sure that computer has Python 3.8 or higher version and Django 4.0.1 or higher version** 

Clone the project

```bash
  git clone https://github.com/nitheezkant/iiitbONE.git

```
Create Superuser
```bash
  python3 manage.py createsuperuser  
```
Database Migrations
```bash
  python3 manage.py makemigrations    
```

```bash
  python3 manage.py migrate        
```
Start the server

```bash
  python3 manage.py runserver
```


## 2)Basic structure 
```iiitbOne``` is the project file that contains the settings.py. 

```core``` is the core app of the whole website. 

```static``` contains all the static files.

```media/rc``` stores all the user uploaded files.

```templates``` contains the main templete that is extended to all the pages.


## 3)URL structure
urls.py in iiitbOne directly points to urls.py inside the core directory. 

If you use /admin, you can access the Django admin panel.

All the URLs in core/urls.py has been listed below.

| URL   | Use                                                             |
| ----------------- | ------------------------------------------------------------------ |
| /| Landing page |
| login/ | Login page|
| signup/ | Sign up page|
| home/| Home page after signup/signin |
| upload/| Upload form page |
| clist/| List of courses |
| semc/< str:pk>/| Change semester of user to pk |
| tlist/< str:pk>/| List of Types of Resourses, pk is course name |
| lisst/< str:pk>/< str:pkk>|List of resourses of course pk and type pkk |
| info/< str:pk>/| Information page of resourse with id pk |
| srh/| Search engine page |
| atf/| Add to favourites|
| fav/| Favourites list page |
| logout/| Logout |


## 4)Database
There are 6 models, location of python code: ```core/models.py```

**1)Django USER Model**

This model stores 

- Roll number in ```username``` field 

- Password in ```password``` field

**2)Profile Model**

This model has a one one relation to USER model, through ```user``` field.

This model stores 
- Name of user in ```name``` field 
- currrent semester of user in ```csem``` field 
- Favourite resourses in the many to many ```fav``` field 

**3)Course model**

This model stores 

- Course name in ```cname``` field 

- Link to display image in ```img``` field

- Semester to which the Course belongs in ```sem``` field
**4)Typee model**

This model stores 

- Type of resourse name in ```tname``` field 

- Link to display image in ```img``` field

**5)rc model**

This model is the model that stores all the resourses

This model stores 

-  User who posted in foreign ```cname``` field 

- Semester of the resourse in ```sem``` field

- Course in foreign ```course``` field

- Type of resourse in foreign ```typee``` field

- Description in ```des``` field

- Resourse file in ```pdf``` field


**6)Message field**

This model stores comments

This model stores 

-  User who posted in foreign ```user``` field 

- Resourse under which it was commented in ```rrc``` field

- Body of comment in ```body``` field

- Time of creation in ```created``` field

- Time of Updation in ```updated``` field









## 5)Forms

There are 2 forms, python code in location ```core/forms.py```

**1)rcf form**

This form is used to upload a resourse, it contains all the fields of ```rc``` model, except for ```poster```.

**2)SignUpForm form**

This form is used to signup a user, and contains ```username```, ```password1```, and ```password2```(confirm password) for the ```USER``` model. ```csem``` and ```name``` for profile model.


## 6)Views

There are 14 views in total in the ```core/views.py```

In most cases, views have been given the same name as the corresponding URL that refers to it.

The views are simple and easy to understand on glancing through the code. 

Refer to the documentation of ```models```, ```urls``` and ```forms``` whenever needed.

Note: decorator ```login_required``` imported from ```django.contrib.auth.decorators``` has been used to restrict the pages that are meant for logged in users only.

## 7)Static and Templetes

Static files are stored in the directory ```static``` present in the main directory. 

```static/img``` contains images used throughout the website. 

```static/styles``` contains the css files.
#
```templates``` directory of the main directory contains main.html that is extended at all pages using Django templating engine. 

All the other HTML files are stored in ```core/templetes/core```.

Templates use Bootstrap5, given below is the GitHub repo for the same

https://github.com/twbs/bootstrap

Templates are inspired by the following template

https://startbootstrap.com/theme/creative




# A Project from Zense Club IIITB

**Contributions**:

- [@nitheezkant](https://github.com/nitheezkant)

More contributions are most welcome
#

# The End

