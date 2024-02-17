import phonenumbers
import opencage
import folium

from adnum import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print("Phone Number is: ",number)
print("Country: ",location)

OperatorName = phonenumbers.parse(number)
NameOfSimP = carrier.name_for_number(OperatorName,"en")
print("Operators Name: ",NameOfSimP)

key = 'f8a2f1dd936b43c2bc8f27d5e4db6d6d'

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
print("Location in Map lat and lng: ",lat,",",lng)

myMap = folium.Map(location = [lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)
myMap.save('currentNewLocation.html')




