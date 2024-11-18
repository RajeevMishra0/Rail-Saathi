from flask import Blueprint, flash, render_template, redirect, request, url_for

# Define blueprints for different sections
home_bp = Blueprint('home', __name__,template_folder="templates")  # Explicit template folder

@home_bp.route('/',method=['GET','POST'])
def home():
    print("Home route accessed")
    print("Template folder:", home_bp.template_folder)  # Debugging line
    
    if request.method == 'POST':
        # Extract form data
        departure_location = request.form.get('from')
        destination = request.form.get('to')
        travel_date = request.form.get('date')
        travel_class = request.form.get('class')

        # Validate form data
        if not departure_location or not destination or not travel_date or travel_class == 'class':
            flash('Please fill in all fields correctly.', 'danger')
            return redirect(url_for('home.home'))

        # Handle the form submission logic here (e.g., redirect to search results page)
        return redirect(url_for('search.search', 
                                from_station=departure_location, 
                                to_station=destination, 
                                date=travel_date, 
                                travel_class=travel_class))

    # Render the homepage
    return render_template('index.html',active_page='home.home')

register_bp = Blueprint('register', __name__,template_folder="templates")

@register_bp.route('/register')
def register():
    # Registration logic
    return render_template('register.html',active_page='register.register')

search_bp = Blueprint('search', __name__,template_folder="templates")

@search_bp.route('/search', methods=['GET'])
def search():
    # Train search logic
    # Get query parameters
    from_station = request.args.get('from_station')
    to_station = request.args.get('to_station')
    date = request.args.get('date')
    travel_class = request.args.get('travel_class')

    # Validate query parameters
    if not from_station or not to_station or not date or not travel_class:
        return render_template('error.html', message="Invalid search parameters.")

    # Fetch search results (mock data here, replace with actual DB query or API call)
    results = [
        {
            "train_name": "Rajdhani Express",
            "train_number": "12345",
            "departure_time": "08:00 AM",
            "arrival_time": "04:00 PM",
            "duration": "8h",
            "available_seats": 50,
            "travel_class": travel_class
        },
        {
            "train_name": "Shatabdi Express",
            "train_number": "54321",
            "departure_time": "09:00 AM",
            "arrival_time": "05:00 PM",
            "duration": "8h",
            "available_seats": 30,
            "travel_class": travel_class
        }
    ]

    # Filter results based on travel class if necessary (mock filtering shown)
    filtered_results = [result for result in results if result['travel_class'] == travel_class]

    # Render the search results page
    return render_template('search.html', 
                           from_station=from_station, 
                           to_station=to_station, 
                           date=date, 
                           travel_class=travel_class, 
                           results=filtered_results,active_page='search.search')

login_bp = Blueprint('login', __name__,template_folder="templates")

@login_bp.route('/login', endpoint='login')  # Rename the endpoint to avoid conflicts
def login_route():
    # Login functionality
    return render_template('login.html', active_page='login.login')

forgot_password_bp = Blueprint('forgot_password', __name__,template_folder="templates")

@forgot_password_bp.route('/forgot_password')
def forgot_password():
  # Forgot password functionality
  return render_template('forgot_password.html', active_page='forgot_password.forgot_password')

logout_bp=Blueprint('logout',__name__,template_folder="templates")
@logout_bp.route('/logout')
def logout():
    # Logout logic
    return redirect(url_for('home.home'))

contact_us_bp=Blueprint('contact_us',__name__,template_folder="templates")
@contact_us_bp.route('/contact_us')
def contact_us():
    # Contact us page
    return render_template('contact-us.html', active_page='contact_us.contact_us')

booking_bp=Blueprint('booking',__name__,template_folder="templates")
@booking_bp.route('/booking')
def booking():
    # Booking logic
    return render_template('booking.html', active_page='booking.booking')

history_bp=Blueprint('history',__name__,template_folder="templates")
@history_bp.route('/history')
def history():
    # History page logic
    return render_template('history.html', active_page='history.history')

dashboard_bp=Blueprint('dashboard',__name__,template_folder="templates")
@dashboard_bp.route('/dashboard')
def dashboard():
    # Dashboard logic
    return render_template('dashboard.html', active_page='dashboard.dashboard')

# Consolidate all blueprints into a list
all_blueprints = [
    home_bp,
    register_bp,
    search_bp,
    login_bp,
    forgot_password_bp,
    logout_bp,
    contact_us_bp,
    booking_bp,
    history_bp,
    dashboard_bp,
]
