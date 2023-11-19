# Dojo and Ninja Management

## Overview

This Flask web application allows you to manage dojos and ninjas. You can create, view, and associate dojos with ninjas. The project uses a MySQL database for data storage.

## Features

- Create new dojos.
- View a list of all dojos.
- Create new ninjas and associate them with specific dojos.
- View a list of ninjas for a selected dojo.

## Setup

To get a local copy up and running, follow these simple steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/GavinEwart/Counter.git

2. Add clone into your VScode and open in an integrated terminal

3. Install the required dependencies by running the following command in your project directory:
   ```sh
   pipenv install

4. Start your shell
   ```sh
   pipenv shell

5. Start the Flask application:
   ```sh
   python server.py
  
6. Open your web browser and navigate to http://localhost:5000.

## What I Learned.

- This project demonstrates how to create a web application using Flask and MySQL.
- It showcases one-to-many database relationships by associating ninjas with specific dojos.
- The use of the `url_for` function to construct URLs and pass parameters in routes.
- Integration of static files (CSS and JavaScript) with Flask templates.
- Handling form submissions and displaying data using HTML templates.

Feel free to explore and modify the code as needed for your own projects.
