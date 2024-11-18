from flask import Blueprint, render_template, redirect, url_for

# Define blueprints for different sections
home_bp = Blueprint('home', __name__,template_folder="templates")  # Explicit template folder

@home_bp.route('/')
def home():
    print("Home route accessed")
    print("Template folder:", home_bp.template_folder)  # Debugging line
    return render_template('index.html',active_page='home.home')

register_bp = Blueprint('register', __name__,template_folder="templates")

@register_bp.route('/register')
def register():
    # Registration logic
    return render_template('register.html',active_page='register.register')

search_bp = Blueprint('search', __name__,template_folder="templates")

@search_bp.route('/search')
def search():
    # Train search logic
    return render_template('search.html',active_page='search.search')

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
