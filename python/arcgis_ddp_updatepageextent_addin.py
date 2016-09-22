import arcpy
import pythonaddins

class ExtentToViewport(object):
    """Implementation for AddIns_addin.ExtentToShapeTool (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        #This is some basic information about the current map document
        mxd = arcpy.mapping.MapDocument("CURRENT")
        df = mxd.activeDataFrame
        ddp = mxd.dataDrivenPages

        #And let's check to make sure the data driven pages layer is in the same projection as the data fram
        if df.spatialReference.name <> arcpy.Describe(ddp.indexLayer).spatialReference.name:
            warningButton = pythonaddins.MessageBox("Nope. Sorry. Your layer's spatial reference doesn't match the data frame. Fix it, or I will help you not.", "Warning Message", 0)
        else:

            #Now we need to find the Object ID for the current data-driven page and select it
            fidFldName = arcpy.ListFields(ddp.indexLayer,"*","OID")[0].name

            if fidFldName == "OBJECTID":
                qryStr = "OBJECTID = " + str(ddp.pageRow.OBJECTID)
            elif fidFldName == "OID":
                qryStr = "OID = " + str(ddp.pageRow.OID)
            elif fidFldName == "FID":
                qryStr = "FID = " + str(ddp.pageRow.FID)
            else:
                errMess = pythonaddins.MessageBox("Hmm... Having trouble querying your viewport layer. Sorry, have to quit.", "Oops.", 0)

            selLyr = arcpy.SelectLayerByAttribute_management(ddp.indexLayer.name, "NEW_SELECTION", qryStr)

            #Once we've selected the right feature, we can change the extent to the current data frame extent
            if arcpy.Describe(selLyr).FIDSet <> '':
                curExtent = df.extent
                pnt1 = arcpy.Point(curExtent .XMin, curExtent .YMin)
                pnt2 = arcpy.Point(curExtent .XMin, curExtent .YMax)
                pnt3 = arcpy.Point(curExtent .XMax, curExtent .YMax)
                pnt4 = arcpy.Point(curExtent .XMax, curExtent .YMin)
                array = arcpy.Array([pnt1, pnt2, pnt3, pnt4])
                polygon = arcpy.Polygon(array)

                rows = arcpy.da.UpdateCursor(selLyr, "SHAPE@")
                for row in rows:
                    row[0] = polygon
                    rows.updateRow(row)

                del row
                del rows
            else:
                errMess2 = pythonaddins.MessageBox("Selection failed. Sorry.", "Oops.", 0)

            del selLyr

            arcpy.RefreshActiveView()
        pass