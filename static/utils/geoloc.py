from geopy.geocoders import Nominatim
import geocoder


def geolo(lat,lon):
    # calling the nominatim tool
    geoLoc = Nominatim(user_agent="GetLoc")
    ac=str(lat)+","+str(lon)
    print(ac)
    # passing the coordinates
    locname = geoLoc.reverse(ac)
  
    # printing the address/location name
    a=locname.address
    b=a.split(",")
    c=''
    for i in b:
        if ' District' in i:
            c=i
    d=c.rstrip('District')
    d=d.lstrip(' ')
    return str(d)
