# GCC-UBS Mavericks
> Develop and Deploy a Web Application on Cloud using Python and Flask.

# Heroku 
Heroku is a web deployment service that basically allows you to develop web-apps 
in a few varieties; for our purposes, we are using Flask - a Python development framework.

Heroku is a little hard to wrap your mind around because it ~just works~.

Essentially how it is set up is that when code is merged to the development branch,
the staging app is updated. Once a pull request is made for the `main` branch, the
production app automatically updates.

Its really simple, but can be hard to grasp.

# Web Server Architecture

We have configured Heroku to use a Python runtime, which is what allows us to use Flask; luckily,
both Flask and Heroku allow us to use this as a fairly standard API endpoint. This is helpful because
we then can do the solution code in Python and the web protocols in Python too.

Flask is a Python library that allows its end users to unify the front-end and backend. This is
really helpful because then the code can live in the same place.

# Deployments

Deployments happen automagically when you commit code to the development branch. Git sends a hook to
Heroku, and the app updates the app in real time.

For production code, you need to merge your `development` changes to the `main` branch; in doing so, you'll
kick off an effectively CRON job which updates the app after a pull request has been cut.

# Working Locally

I am not 100% how to use it locally; most of the repo setup to support Heroku so that is why that there
some extra things