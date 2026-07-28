# ==========================================
# STARHUB
# Main Application
# ==========================================

try:
    from database import create_database
    from dashboard import Dashboard
except ModuleNotFoundError:
    from .database import create_database
    from .dashboard import Dashboard


# Create the database if it doesn't exist
create_database()

# Start the dashboard
app = Dashboard()

app.run()