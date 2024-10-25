# GeoLocation

# Overview
The Geolocation Tracker App is a versatile Python application for mobile geolocation and real-time location tracking using GPS. This app leverages multiple geolocation services to provide location-based functionalities like tracking mobile details, calculating distances, mapping routes, and more. It is a useful tool for users who want to interactively obtain location coordinates, track routes, calculate distances, and find details of any mobile number’s carrier and region.

# Features
Get Current Location: Display current location coordinates (latitude and longitude) using IP data.
Map Routes Between Two Locations: Plot and display a route between two input locations (driving or walking) on an interactive map.
Distance Calculator: Calculate the geographical distance between two input locations.
Phone Number Tracker: Track details of a mobile number, including carrier information, country, and region, along with mapping the location on an interactive map.
Voice Assistance: Each service is enhanced with voice feedback to guide users through each option and provide results.

# Installation
Prerequisites
Ensure you have the following installed:
Python 3.x
Geopy: For geolocation and distance calculation.
OpenCage Geocode: For geolocation services.
Phonenumbers: For parsing, formatting, and validating phone numbers.
Pyttsx3: For text-to-speech capabilities.
Folium: For interactive maps.

# API Keys
OpenCage API: Required for geolocation services. Obtain an API key from OpenCage Geocode.

# Setup
Clone this repository:
bash
git clone https://github.com/Kini7686/Geolocation-Tracker-App.git
Install dependencies:
bash
pip install -r requirements.txt
Run the application:
bash
python geolocation_app.py

# Usage Guide
Upon running the app, a main menu is displayed, offering the following options:

Current Location Coordinates: Fetch and display the latitude and longitude of your current location.
Destination Location Coordinates: Obtain the coordinates of a specific destination.
Map a Route Between Two Locations: Enter starting and destination locations to generate an interactive map displaying the route.
Distance Calculator: Calculate the distance between two input locations.
Phone Number Tracker: Input a phone number with its country code to get information such as carrier, country, and an approximate location on a map.
Output
HTML Map Files: Generated maps are saved as map_directions.html or phone_NumberLocation.html in the project directory.
Voice Feedback: All output details are read out loud to the user using pyttsx3.
Requirements
List of dependencies included in requirements.txt:

geopy
opencage
phonenumbers
pyttsx3
folium
requests
