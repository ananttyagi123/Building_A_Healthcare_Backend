# Django Healthcare Backend Assignment
About the Project

This is a backend system for a healthcare application built with Django and Django REST Framework (DRF). The system allows users to register, log in, and manage patient and doctor records securely. It also supports assigning doctors to patients.

All data is stored in PostgreSQL, and authentication is handled with JWT tokens for security.


#Tech Stack

# Backend: Django & Django REST Framework

# Database: PostgreSQL (tested with pgAdmin/PostgreSQL Workbench)

# Authentication: JWT using djangorestframework-simplejwt

# Testing : POSTMAN API 


Features

# User Authentication

# Register a new account

# Log in and get a JWT token
# after that throught POSTMAN API do the CRUD operations 

# Patient Management

Add, view, update, and delete patient records

Only authenticated users can manage their patients

# Doctor Management

Add, view, update, and delete doctor records

# Patient-Doctor Mapping

Assign doctors to patients

View assigned doctors for a patient

Remove a doctor from a patient

