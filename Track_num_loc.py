from geopy import distance
from geopy.geocoders import Nominatim
from opencage.geocoder import OpenCageGeocode
import phonenumbers
import pyttsx3
from phonenumbers import geocoder, carrier
import folium

# from myNumber import number
from phonenumbers import geocoder

Key = '204d5c6afbcf4ae88df9e85903da9473'  ##Api key ,So what is an api?  opencage

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
outer_count = 100
while outer_count!=200:
    print("\n\n         PLEASE SELECT ONE OF THE SERVICE YOU WANT TO USE : \n\n  1> Location: \n  2> Map A Route Between Two Locations: \n  3> Distance Calculator : \n  4> Track A Phone Number :  \n  5> Exit :    ")
    speak("PLEASE SELECT ONE OF THE SERVICE YOU WANT TO USE  1  Location Details or 2 Map A Route Between Two Locations Or 3   Distance Calulator  Or 4 Track A Phone Number ")

    n = int(input("\n >>> "))

    # 1> Get Your Current Location:

    if n==1:
        # print('1')
        print("      1> Current Location Co-ordinates : \n      2> Destination Location Co-ordinates : \n      ") 
        speak( "     1   Get  Your  Current Location Coordinates       2    Get  Destination Location Coordinates ") 
        x= int(input(" \n>>> "))
        if x==1 :
            import requests
            res = requests.get('https://ipinfo.io/')
            data = res.json() ## ipinfo returns the data in a specific format, so we are converting it with the help of .json for custom look 
            # print(res.text)

            country =str(data['country'])
            region = str(data['region'])
            city = str( data['city'] )
            location = data['loc'].split(',')
            latitude = str( location[0] ) ## conversion to string for speech recognizition
            longitude = str( location[1] )

            
            print("Country   :" , country)
            speak(country+ ' is your country')    
            print("Region    :" , region)
            speak(region+ ' is your region')    
            print("City      :" , city)
            speak(city+ ' is your city')

            print("Latitude  : ",latitude)
            print("longitude : ",longitude)
            speak(latitude+' is the latitude')
            speak(longitude+' is the longitude')

            print("        \n 1> MAIN MENU\n 2> EXIT        ")
            speak("        1> for MAIN MENU      \n2> for EXIT        ")
            y = int(input("   >>> "))
            if y == 2:
                outer_count=200
                print('             THANK YOU FOR USING OUR SERVICES!\n             COMEBACK SOON.. 😀😄')
                speak('     THANK YOU FOR USING OUR SERVICES!\n        COMEBACK SOON.. ')
            else:    
                continue


        if x==2 :

            

            from geopy.geocoders import Nominatim

            Geolocator = Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36")

            adress = input("Enter the address : ")
            loc = Geolocator.geocode(adress)  # object
            print(loc)
            print("Destination : ")
            latitude = str(loc.latitude)
            longitude = str(loc.longitude)

            print("         Latitude  : "+latitude)
            print("         Longitude : "+longitude)
            speak(latitude+' is latitude'+longitude+' is longitude of your destination')
        
            print("        \n 1> MAIN MENU\n 2> EXIT        ")
            speak("        1> for MAIN MENU       \n2> for EXIT        ")
            y = int(input("   >>> "))
            if y == 2:
                outer_count=200
                print('             THANK YOU FOR USING OUR SERVICES!\n             COMEBACK SOON.. 😀😄')
                speak('     THANK YOU FOR USING OUR SERVICES!\n        COMEBACK SOON.. ')
            else:    
                continue

        

    if n==2:
        

        # initialize Nominatim API
        geolocator = Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36")

        # place input
        Input_place1 = str(input("  From :  "))
        Input_place2 = str(input("  To :  "))

        # Get location of the input strings
        place1 = geolocator.geocode(Input_place1)
        place2 = geolocator.geocode(Input_place2)

        print(place1)
        print(place2)

        # Get latitude and longitude
        Loc1_lat, Loc1_lon = (place1.latitude), (place1.longitude)
        Loc2_lat, Loc2_lon = (place2.latitude), (place2.longitude)

        location1 = (Loc1_lat, Loc1_lon)
        location2 = (Loc2_lat, Loc2_lon)

        print(location1[0],location1[1])

        import openrouteservice
        
        client=openrouteservice.Client(key='5b3ce3597851110001cf624823b437fa956f41608563b0a22108e3ae') # Specify your personal API key
        
        coordinates = [[location1[1], location1[0]], [location2[1], location2[0]]]  # lon , lat
        
        print("      \n** Please Select The Mode **\n    1> Driving :\n    2> Walking :  ")
        speak("  Please Select The      Mode ")
        speak("    1 Driving       2 Walking   ")
        
        r = int(input(" >>> "))
        mode = 'driving-car' 
        
        if r==1 :
            route = client.directions(coordinates=coordinates,profile='driving-car', format='geojson')
        if r==2 :
            route = client.directions(coordinates=coordinates,profile='foot-walking', format='geojson')
        
        map_directions = folium.Map(location=[float(location1[0] ), float( location1[1] )],zoom_start=9)
        folium.GeoJson(route, name='route').add_to(map_directions)

        folium.LayerControl().add_to(map_directions)

        folium.Marker([Loc1_lat, Loc1_lon], popup=place1).add_to(map_directions)
        folium.Marker([Loc2_lat, Loc2_lon], popup=place2).add_to(map_directions)


        map_directions.save("map_directions.html")
        
        print("      **   Your HTML file has been generated.   **  ")
        speak("      **   Your HTML file has been generated.   **  ")
        
        print("        \n 1> MAIN MENU\n 2> EXIT        ")
        speak("        1> for MAIN MENU      \n2> for EXIT        ")
        y = int(input("   >>> "))
        if y == 2:
                outer_count=200
                print('             THANK YOU FOR USING OUR SERVICES!\n             COMEBACK SOON.. 😀😄')
                speak('     THANK YOU FOR USING OUR SERVICES!\n        COMEBACK SOON.. ')
        else:    
                continue
        
    if n==3:
        # initialize Nominatim API
        geolocator = Nominatim(user_agent="geopiExercises")

        # place input
        Input_place1 = str(input(" From : "))
        Input_place2 = str(input(" To : "))

        # Get location of the input strings
        place1 = geolocator.geocode(Input_place1)
        place2 = geolocator.geocode(Input_place2)

        print(place1)
        print(place2)

        # Get latitude and longitude
        Loc1_lat, Loc1_lon = (place1.latitude), (place1.longitude)
        Loc2_lat, Loc2_lon = (place2.latitude), (place2.longitude)

        location1 = (Loc1_lat, Loc1_lon)
        location2 = (Loc2_lat, Loc2_lon)

        print(distance.distance(location1, location2).km, " Kms")
        dist = str(distance.distance(location1, location2).km)
        speak("Distance from "+Input_place1 + " to " +
            Input_place2 + " is "+dist + " kilometers")

        
        print("        \n 1> MAIN MENU\n 2> EXIT        ")
        speak("        1> MAIN MENU      \n2>EXIT        ")
        y = int(input("   >>> "))
        if y == 2:
                outer_count=200
                print('             THANK YOU FOR USING OUR SERVICES!\n             COMEBACK SOON.. 😀😄')
                speak('     THANK YOU FOR USING OUR SERVICES!\n        COMEBACK SOON.. ')
        else:    
                continue
        
        

    if n==4:
        print("Please enter the number along with country code :")
        speak('Please enter the number along with country code')
        number = input("\n  >>> ")


        some_Number = phonenumbers.parse(number) #prasing String to phone number  #split the phonenumber into two parts country code && the actual number
        
        country= str(geocoder.country_name_for_number(some_Number,'en') )
        your_Location = geocoder.description_for_number(some_Number, 'en')
        
        print("Country : "+country)
        speak("Country  is "+country)
        
        print(your_Location)
        speak(your_Location +'is your region')

        geocoder = OpenCageGeocode(Key)
        query = str(your_Location)
        results = geocoder.geocode(query)  # reurns multiple values

        

        print(some_Number)
        Carrier = carrier.name_for_number(some_Number, 'en')  # get service provider
        print(carrier.name_for_number(some_Number, 'en'))  
        speak('Your carrier name is'+Carrier)



        # print(results)

        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']

        latitude = str(lat)
        longitude = str(lng)

        print("Latidue :  "+latitude + "  Longitutde :  "+longitude)

        speak(latitude+' is the latitude')
        speak(longitude+' is the longitude')



        myMap = folium.Map(location=[lat, lng], zoom_start=9)

        folium.Marker([lat, lng], popup=your_Location).add_to(myMap)

        ## save map in html file

        myMap.save("phone_NumberLocation.html")
        print("      **   Your HTML file has been generated.   **  ")
        speak("      **   Your HTML file has been generated.   **  ")

        print("        \n 1> MAIN MENU\n 2> EXIT        ")
        speak("        1> for MAIN MENU      \n2> for EXIT        ")
        y = int(input("   >>> "))
        if y == 2:
                outer_count=200
                print('             THANK YOU FOR USING OUR SERVICES!\n             COMEBACK SOON.. 😀😄')
                speak('     THANK YOU FOR USING OUR SERVICES!\n        COMEBACK SOON.. ')
        else:    
                continue


    if n==5 :
        outer_count=200
        print('             THANK YOU FOR USING OUR SERVICES!\n             COMEBACK SOON.. 😀😄')
        speak('     THANK YOU FOR USING OUR SERVICES!\n        COMEBACK SOON.. ')

        
