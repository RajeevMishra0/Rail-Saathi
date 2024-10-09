# RailSaathi - AI-Powered Railway Assistance System

## Project Overview

**RailSaathi** is an AI-powered railway assistance system that simplifies ticket booking for the Indian Railways. It features user authentication, train search, real-time seat booking, and AI-driven suggestions. Built with Flask, MySQL, and JavaScript, this project aims to enhance user experience and streamline railway operations. Deployable on Heroku.

## Features

- **User Authentication**: Secure login and registration processes.
- **Train Search Functionality**: Search for trains between specified source and destination stations.
- **Seat Booking**: Real-time seat booking with immediate confirmation.
- **AI-Powered Suggestions**: Intelligent recommendations for seat selection.
- **User Dashboard**: Manage bookings and view travel history.
- **Responsive Design**: Mobile-friendly interface for all devices.

## Technologies Used

- **Backend**: Flask (Python)
- **Database**: MySQL with SQLAlchemy ORM
- **Frontend**: HTML, CSS, JavaScript
- **AI Model**: Machine learning algorithms for seat suggestions
- **Deployment**: Heroku

### Python Version
This project uses **Python 3.12.6**. Please ensure that you are using this version when setting up the project locally or when deploying it. The `runtime.txt` file in the project specifies this version for deployment on Render.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/RailSaathi.git

2. Change into Porject Directory:
   ```bash
   cd RailSaathi

3. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    
4. Avtivate the Python Virtual Environment:
    ```bash
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   
6. Set up the MySQL database using the provided SQL script:
   ```bash
   -- railsaathi.sql
   
7. Run the Flask application:
   ```bash
   python app.py
   
8. Access the application in your web browser at
   ```bash
   http://127.0.0.1:5000.

## Future Work
- Implement real-time train updates and notifications.
- Expand the AI model for personalized recommendations.
- Add multi-language support.
- Integrate third-party APIs for food ordering.

# Team Members:
- **Ayush Goel** - Backend, Database Integration, AI Logic, Deployment
- **Meghna Singh** - Frontend UI/UX, CSS Design, Template Structure
- **Rajeev Mishra** - Frontend JavaScript & Dynamic Features
- **Azad Tiwari** - User Dashboard, Interactive Components

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any suggestions or improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


### Notes:
- Make sure to replace `yourusername` with your actual GitHub username in the clone link.
- You can add any additional sections or modify existing ones as per your project requirements!
