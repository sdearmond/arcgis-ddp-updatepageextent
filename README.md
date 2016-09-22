# arcgis-ddp-updatepageextent


This is a python tool for ESRI ArcMap to update the current data driven page extent to the current data frame extent.

Installing the addin:

To use this tool, you will need to have ESRI ArcMap version 10.0 or later installed. Double-click on the "ddp_updatepgextent.esri.addin" to install as a toolbar. (If you'd rather just check out the python code, it is provided in: python/arcgis_ddp_updatepageextent_addin.py)


Adding the tool:

Once the addin is installed, open ArcMap, right-click anywhere on your toolbars, and choose customize. On the commands tab, scroll down to DDP Python Tools and click on it. In the commands window, click on the "Data Frame Extent to Viewport Extent" tool and drag anywhere on your toolbars.


Using the tool:

Open any mxd with data driven pages enabled. While focused on the data driven page you wish to edit, zoom and/or pan to alter the extent of the data frame as you desire. Then click on the "Data Frame Extent to Viewport Extent" tool. Your data driven page extent will automatically be updated to the current data frame extent.


Note:

If data driven pages is not enabled for your current mxd, no changes will occur. Also, as the tool will tell you, the coordinate system for your data frame and your data driven page index layer must match or the tool will not run.