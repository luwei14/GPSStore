import lxml.etree as etree

class GPX:
    def __init__(self, creator,version=1.1):
        self.version = version  # You must include the version number in your GPX document.
        self.creator = creator  # You must include the name or URL of the software that created your GPX document.  This allows others to inform the creator of a GPX instance document that fails to validate.
        self.metadata = None    # Metadata about the file.
        self.waypts = []        # A list of waypoints.
        self.routes = []        # A list of routes.
        self.tracks = []        # A list of tracks.
        self.extensions = None  # You can add extend GPX by adding your own elements from another schema here.
    
    def version(self):
        pass

    def read(self, fpath):
        pass

    def write(self, fpath):
        pass

    def xml(self):
        pass

    def add_waypts(self, waypts):
        pass
    
    def add_routes(self, routes):
        pass

    def add_tracks(self, tracks):
        pass

class GPXMetaData:
    '''
		Information about the GPX file, author, and copyright restrictions goes in the metadata section.  Providing rich,
		meaningful information about your GPX files allows others to search for and use your GPS data.
    '''
    def __init__(self):
        self.name = None        # The name of the GPX file.
        self.desc = None        # A description of the contents of the GPX file.
        self.author = None      # The person or organization who created the GPX file.
        self.copyright = None   # Copyright and license information governing use of the file.
        self.link = None        # URLs associated with the location described in the file.
        self.time = None        # The creation date of the file.
        self.keywords = None    # Keywords associated with the file.  Search engines or databases can use this information to classify the data.
        self.bounds = None      # Minimum and maximum coordinates which describe the extent of the coordinates in the file.
        self.extensions = None  # You can add extend GPX by adding your own elements from another schema here.

class GPXWayPoint:
    '''
        wpt represents a waypoint, point of interest, or named feature on a map.        
    '''
    def __init__(self, lat, lon):
        # Required
        self.lat = lat          # The latitude of the point.  This is always in decimal degrees, and always in WGS84 datum.
        self.lon = lon          # The longitude of the point.  This is always in decimal degrees, and always in WGS84 datum.
        # Position Info
        self.ele = None         # Elevation (in meters) of the point.
        self.time = None        # Creation/modification timestamp for element. Date and time in are in Univeral Coordinated Time (UTC), not local time! Conforms to ISO 8601 specification for date/time representation. Fractional seconds are allowed for millisecond timing in tracklogs.
        self.magvar = None      # Magnetic variation (in degrees) at the point
        self.geoidheight = None # Height (in meters) of geoid (mean sea level) above WGS84 earth ellipsoid.  As defined in NMEA GGA message.
        # Description info
        self.name = None        # The GPS name of the waypoint. This field will be transferred to and from the GPS. GPX does not place restrictions on the length of this field or the characters contained in it. It is up to the receiving application to validate the field before sending it to the GPS.
        self.cmt = None         # GPS waypoint comment. Sent to GPS as comment. 
        self.desc = None        # A text description of the element. Holds additional information about the element intended for the user, not the GPS.
        self.src = None         # Source of data. Included to give user some idea of reliability and accuracy of data.  "Garmin eTrex", "USGS quad Boston North", e.g.
        self.link = None        # Link to additional information about the waypoint.
        self.sym = None         # Text of GPS symbol name. For interchange with other programs, use the exact spelling of the symbol as displayed on the GPS.  If the GPS abbreviates words, spell them out.
        self.type = None        # Type (classification) of the waypoint.
        # Accuracy info
        self.fix = None         # Type of GPX fix.
        self.sat = None         # Number of satellites used to calculate the GPX fix.
        self.hdop = None        # Horizontal dilution of precision.
        self.vdop = None        # Vertical dilution of precision.
        self.pdop = None        # Position dilution of precision.
        self.ageofdgpsdata = None # Number of seconds since last DGPS update.
        self.dgpsid = None      # ID of DGPS station used in differential correction.
        self.extensions = None  # You can add extend GPX by adding your own elements from another schema here.

class GPXRoute:
    '''
        rte represents route - an ordered list of waypoints representing a series of turn points leading to a destination.
    '''
    def __init__(self):
        self.rtepts = []        # A list of route points.
        self.name = None        # GPS name of route.
        self.cmt = None         # GPS comment for route.
        self.desc = None        # Text description of route for user.  Not sent to GPS.
        self.src = None         # Source of data. Included to give user some idea of reliability and accuracy of data.
        self.link = None        # Links to external information about the route.
        self.number = None      # GPS route number.
        self.type = None        # Type (classification) of route.
        self.extensions = None  # You can add extend GPX by adding your own elements from another schema here.


class GPXTrack:
    '''
        trk represents a track - an ordered list of points describing a path.
    '''
    def __init__(self):
        self.trksegs = []        # A Track Segment holds a list of Track Points which are logically connected in order. To represent a single GPS track where GPS reception was lost, or the GPS receiver was turned off, start a new Track Segment for each continuous span of track data.
        self.name = None        # GPS name of track.
        self.cmt = None         # GPS comment for track.
        self.desc = None        # User description of track.
        self.src = None         # Source of data. Included to give user some idea of reliability and accuracy of data.
        self.link = None        # Links to external information about the track.
        self.number = None      # GPS track number.
        self.type = None        # Type (classification) of track.
        self.extensions = None  # You can add extend GPX by adding your own elements from another schema here.

class GPXTrackSegment:
    '''
        A Track Segment holds a list of Track Points which are logically connected in order. To represent a single GPS track where GPS reception was lost, or the GPS receiver was turned off, start a new Track Segment for each continuous span of track data.
    '''
    def __init__(self):
        self.trkpts = []         # A Track Point holds the coordinates, elevation, timestamp, and metadata for a single point in a track.
        self.extensions = None  # You can add extend GPX by adding your own elements from another schema here.

class GPXParser:
    def __init__(self):
        pass

    def parse(self, fpath):
        fp = open(fpath)
        root = etree.fromstring(fp.read())
        fp.close()
        version = root.attrib["version"]
        creator = root.attrib["creator"]
        gpx = GPX(version = version, creator = creator)
        gpx.metadata = GPXMetaData()
        mtnode = root.find("metadata")
        for mtchild in mtnode:
            tagname = mtchild.tag 
            value = mtchild.text
            setattr(gpx.metadata, tagname, value)

        wpts = root.findall("wpt")
        for wpt in wpts:
            lon = float(wpt.attrib("lon"))
            lat = float(wpt.attrib("lat"))
            p = GPXWayPoint(lat, lon)
            for wptchild in wpt:
                tagname = wptchild.tag
                if tagname in ["ele","geoidheight","hdop","vdop","pdop","ageofdgpsdata","sat"]:
                    value = float(wptchild.text)
                else:
                    value = wptchild.text
                setattr(p, tagname,value)
            gpx.waypts.append(p)

        routes = root.findall("rte")
        for rte in routes:
            route = GPXRoute()
            for rtechild in rte:
                tagname = rtechild.tag
                if tagname == "rtept":
                    continue 
                value = rtechild.text
                if tagname == "number":
                    value = int(value)
                setattr(route, tagname, value)
            rtepts = rte.findall("rtept")
            for rtept in rtepts:
                lon = float(rtept.attrib["lon"])
                lat = float(rtept.attrib["lat"])
                p = GPXWayPoint(lat, lon)
                for rteptchild in rtept:
                    tagname = rteptchild.tag
                    if tagname in ["ele","geoidheight","hdop","vdop","pdop","ageofdgpsdata","sat"]:
                        value = float(rteptchild.text)
                    else:
                        value = rteptchild.text
                    setattr(p, tagname, value)
                route.rtepts.append(p)
            gpx.routes.append(route)

        tracks = root.findall("trk")
        for trk in tracks:
            track = GPXTrack()
            for trkchild in trk:
                tagname = trkchild.tag
                if tagname == "trkseg":
                    continue 
                value = trkchild.text
                if tagname == "number":
                    value = int(value)
                setattr(track, tagname, value)
            
            trksegs = trk.findall("trkseg")
            for trkseg in trksegs:
                seg = GPXTrackSegment()
                trkpts = trkseg.findall("trkpt")
                for trkpt in trkpts:
                    lon = float(trkpt.attrib["lon"])
                    lat = float(trkpt.attrib["lat"])
                    p = GPXWayPoint(lat, lon)
                    for trkptchild in trkpt:
                        tagname = trkptchild.tag
                        if tagname in ["ele","geoidheight","hdop","vdop","pdop","ageofdgpsdata","sat"]:
                            value = float(trkptchild.text)
                        else:
                            value = trkptchild.text
                        setattr(p, tagname, value)
                    seg.trkpts.append(p)
                track.trksegs.append(seg)
            gpx.routes.append(track)
        return gpx

        
if __name__ == "__main__":
    parse = GPXParser()
    gpx = parse.parse("/Users/luwei/Data/EDooon/data/31159018.gpx")