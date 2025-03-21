# Homework2

# Flask Web Application

## Overview
This is a simple Flask web application that serves multiple pages using HTML templates. It includes a `Makefile` for managing the virtual environment and running the application.

## Features
- Includes a `Makefile` for easy setup and running.
- Uses a virtual environment to manage dependencies.
- Runs on port **5001**.

## Project Structure
```
flask/
├── Makefile
├── README.md
├── app.py
├── requirements.txt
└── templates/
    ├── index.html
    ├── page1.html
    └── page2.html
```

## Installation & Setup
### 1. Clone the Repository
```bash
git clone <repository_url>
cd flask
```

### 2. Install Dependencies
Use the `Makefile` to set up the virtual environment and install dependencies:
```bash
make install
```

### 3. Run the Application
```bash
make run
```
The application will be accessible at: [http://localhost:5001](http://localhost:5001)

## Routes
| Route | Description |
|--------|-------------|
| `/` | Home Page |
| `/1` | Page 1 |
| `/2` | Page 2 |

## Cleaning Up
To remove the virtual environment and cached files:
```bash
make clean
```
