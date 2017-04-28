# :steam_locomotive: cta_time :steam_locomotive:
### [Workflow](https://workflow.is/) Layer for CTA Train Tracker API 

![purple line](http://www.chicago-l.org/operations/lines/images/line_maps/PurpleLine.jpg)

 
------------- 
 
### Instructions
1.  Apply for CTA Developer API access [here](http://www.transitchicago.com/developers/traintrackerapply.aspx)
2.  Once approved, store API access key in env.py as "CTA_API_KEY"
3.  Add/remove CTA stops in "stations" dictionary ([complete list of CTA stop and map IDs](https://data.cityofchicago.org/Transportation/CTA-System-Information-List-of-L-Stops/8pix-ypme))
4.  Stand up server to host code
5.  ???
6.  profit


-------------

### Dependencies

This module makes use of the following Python modules that you must have installed.

* beautifulsoup4
* datetime
* Flask
* requests
