# File Name: GridBuilder.py
# Purpose: Wrapper module for local coordinate transformation from OSGB to Local Grid
import arcpy

class Coordinate(object):
    def __init__(self, zoneKey, id, coordE, coordN, height):
        '''Read from constructor'''
        self.ZoneKey = zoneKey          # Zone Key parameter
        self.FID = id
        self.CoordE = coordE            # Easting Coordinate
        self.CoordN = coordN            # Easting Coordinate
        self.Height = height            # Height Coordinate

        self.PrjSF = None               # Project Scale Factor
        self.ElvSF = None               # Elevation Scale Factor
        self.CSF = None                 # Combined Scale Factor       
        self.StartCordE = None
        self.StartCordN = None    
        self.OrignCordE = None
        self.OrignCordN = None
        
        self.LclCordE = None
        self.LclCordN = None

    def calcuCSF(self):
        if self.PrjSF != None and self.ElvSF != None:
            self.CSF = self.PrjSF * self.ElvSF
        else:
            print 'The factor is null'

    def calcuESCoord(self):
        if self.CSF != None:
            self.LclCordE = (self.CoordE - self.OrignCordE)/(self.CSF)
            self.LclCordN = (self.CoordN - self.OrignCordN)/(self.CSF)
        else:
            print 'The factor is null'

    def BuildGeometry(self, point):
        newPoint = arcpy.Point()
        newPoint.X = self.LclCordE
        newPoint.Y = self.LclCordN
        pointGeometry = arcpy.PointGeometry(newPoint)
        return pointGeometry

    @property
    def setPrjSF(self):
        return self.PrjSF

    @setPrjSF.setter
    def setPrjSF(self, value):
        self.PrjSF = value

    @property
    def getZoneKey(self):
        return self.ZoneKey

    @property
    def getHeight(self):
        return self.Height


class Zones(object):  
    def __init__(self, key, startE, startN, orignE, orignN, prjSF):
        self.Key = key
        self.StartE = startE            # Loop local grid parameters
        self.StartN = startN            # Loop local grid parameters
        self.OrignE = orignE
        self.OrignN = orignN
        self.PrjSF = prjSF

    @property
    def getPrjSF(self):
        return self.PrjSF

    @property
    def getKey(self):
        return self.Key
    

class HetBand(object):
    def __init__(self, height, hegtBand, elvSF, comts):
        self.Height= height
        self.HegtBand = hegtBand
        self.ElvSF = elvSF
        self.Comts = comts
    

