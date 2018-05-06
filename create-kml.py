#!/bin/python

class Coord:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon



def start_folder(kml, name):
    kml.write('<Folder><name>{:s}</name><open>1</open>'.format(name))

def end_folder(kml):
    kml.write('</Folder>')

def pushpin(kml, name, coord):
    kml.write("""
			<Placemark>
                                <name>{:s}</name>
<!--   <LookAt>
					<longitude>38.34803907965529</longitude>
					<latitude>33.2540199398231</latitude>
					<altitude>0</altitude>
					<heading>11.08435171895972</heading>
					<tilt>1.703726260245887</tilt>
					<range>4693076.838697146</range>
					<gx:altitudeMode>relativeToSeaFloor</gx:altitudeMode>
				</LookAt>-->
				<styleUrl>#m_ylw-pushpin</styleUrl>
				<Point>
					<gx:drawOrder>1</gx:drawOrder>
                                        <coordinates>{:f},{:f}</coordinates>
				</Point>
			</Placemark>""".format(name, coord.lon, coord.lat)
    )





class Person:
    def __init__(self, kml, lat, lon, name, father):
        self.coord=Coord(lat, lon)
        self.name=name
        pushpin(kml, name, self.coord)
        if father:
           line(kml, father, self)


def line(kml, person_1, person_2):
    kml.write("""
			<Placemark>
                                <name>{:s} - {:s}</name>
				<styleUrl>#m_ylw-pushpin0</styleUrl>
				<LineString>
					<tessellate>1</tessellate>
					<coordinates>
                                                {:f},{:f},0 {:f},{:f},0 
					</coordinates>
				</LineString>
			</Placemark>""".format(person_1.name, person_2.name, person_1.coord.lon, person_1.coord.lat, person_2.coord.lon, person_2.coord.lat))

kml = open('Voelkertafel.kml', 'w')

kml.write("""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
	<name>Voelkertafel.kml</name>
	<StyleMap id="m_ylw-pushpin"> <Pair> <key>normal</key> <styleUrl>#s_ylw-pushpin0</styleUrl> </Pair> <Pair> <key>highlight</key> <styleUrl>#s_ylw-pushpin_hl</styleUrl> </Pair> </StyleMap>
	<Style id="s_ylw-pushpin_hl"> <IconStyle> <scale>1.3</scale> <Icon> <href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href> </Icon> <hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/> </IconStyle> </Style>
	<StyleMap id="m_ylw-pushpin0"> <Pair> <key>normal</key> <styleUrl>#s_ylw-pushpin</styleUrl> </Pair> <Pair> <key>highlight</key> <styleUrl>#s_ylw-pushpin_hl0</styleUrl> </Pair> </StyleMap>
	<Style id="s_ylw-pushpin"> <IconStyle> <scale>1.1</scale> <Icon> <href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href> </Icon> <hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/> </IconStyle> <LineStyle> <color>ff00ffff</color> <width>2</width> </LineStyle> </Style>
	<Style id="s_ylw-pushpin_hl0"> <IconStyle> <scale>1.3</scale> <Icon> <href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href> </Icon> <hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/> </IconStyle> <LineStyle> <color>ff00ffff</color> <width>2</width> </LineStyle> </Style>
	<Style id="s_ylw-pushpin0"> <IconStyle> <scale>1.1</scale> <Icon> <href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href> </Icon> <hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/> </IconStyle> </Style>
""")

kml.write("""<Folder><name>Voelkertafel</name><open>1</open>
		<LookAt>
			<longitude>39.07882192413162</longitude>
			<latitude>33.96621037200322</latitude>
			<altitude>0</altitude>
			<heading>11.48094450866536</heading>
			<tilt>1.890562138906871</tilt>
			<range>5907525.300609684</range>
			<gx:altitudeMode>relativeToSeaFloor</gx:altitudeMode>
		</LookAt>""")


start_folder(kml, 'Japhet')

japhet = Person(kml, 39    , 31    , 'Japhet'  , None)

gomer  = Person(kml, 47.781, 34.042, 'Gomer'   , japhet)
magog  = Person(kml, 46    , 55    , 'Magog'   , japhet)
madai  = Person(kml, 35    , 52    , 'Madai'   , japhet)
jawan  = Person(kml, 38    , 22    , 'Jawan'   , japhet)
tubal  = Person(kml, 40    , 39    , 'Tubal'   , japhet)
mesech = Person(kml, 41    , 42    , 'Mesech'  , japhet)
tiras  = Person(kml, 44    , 28    , 'Tiras'   , japhet)

aschkenas = Person(kml, 46, 40, 'Aschkenas', gomer)
riphat    = Person(kml, 41, 33, 'Riphat'   , gomer)
togarma   = Person(kml, 38, 40, 'Togarma'  , gomer)

# elischa   = Person(kml, 41    , 15  , 'Elischa'  , jawan)
elischa   = Person(kml, 34.884, 32.456, 'Elischa'  , jawan) # According to http://tribesofaboriginalnations.com/wp-content/uploads/sites/12/2015/08/table-of-nations1.jpg

# tarsis    = Person(kml, 37.5  ,  4   , 'Tarsis'   , jawan)
tarsis    = Person(kml, 37.5  , -2   , 'Tarsis'   , jawan)
# kittim    = Person(kml, 35    , 33   , 'Kittäer'  , jawan)
kittim    = Person(kml, 35.418, 34.075, 'Kittäer'  , jawan) # According to http://tribesofaboriginalnations.com/wp-content/uploads/sites/12/2015/08/table-of-nations1.jpg

dodanim   = Person(kml, 36.19 , 27.96, 'Dodaniter', jawan)

# pushpin(kml, 'Japhet', japhet)
# pushpin(kml, 'Gomer' , gomer )
# line(kml, japhet, gomer)
#line(kml, japhet, magog)
# line(kml, japhet, )

kml.write("""
""")

end_folder(kml)

start_folder(kml, 'Ham')

ham      = Person(kml, 30    , 32    , 'Ham'    , None)
kusch    = Person(kml, 26    , 33    , 'Kusch'  , ham )
mizraim  = Person(kml, 28    , 30    , 'Mizraim', ham )
put      = Person(kml, 31    , 26    , 'Put'    , ham )
kanaan   = Person(kml, 32    , 35    , 'Kanaan' , ham )

end_folder(kml)

start_folder(kml, 'Sem')

sem        = Person(kml, 34    , 36   , 'Sem'       , None)
elam       = Person(kml, 30    , 49   , 'Elam'      , sem )
assur      = Person(kml, 36    , 43   , 'Assur'     , sem )
# arpakschad = Person(kml, 34    , 36   , 'Arpakschad', sem )
lud        = Person(kml, 40    , 27   , 'Lud'       , sem )
aram       = Person(kml, 34    , 38   , 'Aram'      , sem )

end_folder(kml)

kml.write("""
</Folder>
</Document>
</kml>
""")

kml.close()
