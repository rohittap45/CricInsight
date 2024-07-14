## CricInsight

CricInsight is a comprehensive cricket web application built using Django, Bootstrap, JavaScript, and machine learning. It provides users with live match updates, detailed match information fetched from the CricAPI, and a powerful IPL victory predictor.

### Features

****Live Match Updates****
- Users can view live scores, match status, and other key details for ongoing cricket matches.
- The application fetches data from the CricAPI to ensure up-to-date information[1].

****Match Details****
- Detailed information about each match, including match name, date, time, venue, and scorecard, is fetched from the CricAPI[1].
- Users can access comprehensive statistics and insights for each match.

****IPL Victory Predictor****
- An advanced machine learning model, trained on historical IPL data using the Random Forest algorithm, predicts the winning probability of the batting and bowling teams.
- Users can input various parameters such as batting team, bowling team, venue, target, runs required, balls remaining, and wickets in hand to get the predicted outcome.

****User Authentication****
- Users can register, login, and logout of the application using Django's built-in authentication system.
- Registered users can access additional features and personalized experiences.

### Technical Details

The CricInsight application is built using the following technologies:

- **Front-end**: Django templates, Bootstrap 5, HTML, CSS, JavaScript
- **Back-end**: Django
- **Database**: SQLite (default Django database)
- **Machine Learning**: Python, Scikit-learn
- **Deployment**: Heroku

The key files and their descriptions are as follows:

1. `templates/live_matches.html`: Displays the live match updates fetched from the CricAPI using Django templates and JavaScript[1].
2. `templates/match_details.html`: Presents the detailed information about each match fetched from the CricAPI[1].
3. `templates/predict.html`: Implements the IPL victory prediction model and the user input interface using Django forms and Bootstrap 5.
4. `templates/registration/register.html` and `templates/registration/login.html`: Handle user registration and login functionality using Django's built-in authentication system.
5. `cricinsight/views.py`: The main Django views file that handles the logic for each page and API requests.
6. `cricinsight/models.py`: Defines the user model and any other necessary models for the application.
7. `cricinsight/forms.py`: Contains the Django forms used for user input and registration.
8. `cricinsight/predictor.py`: Contains the Python script that trains the Random Forest model and provides the prediction functionality.

### Getting Started

To run the CricInsight application locally, follow these steps:

1. Clone the repository: `git clone https://github.com/rohittap45/CricInsight.git`
2. Create and activate a virtual environment: `python -m venv env` and `source env/bin/activate`
3. Install the dependencies: `pip install -r requirements.txt`
4. Apply the database migrations: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`
6. Open the application in your browser: `http://localhost:8000`

### Contributions

We welcome contributions from the community. If you find any issues or have suggestions for improvements, please feel free to open a new issue or submit a pull request.
