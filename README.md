# gdg-2cc

## Task:

Create an API using Flask or any framework you are comfortable with (Flask is easy to learn) and scrape the GSOC website to fetch details of all the organizations in Google summer of codes and in the api send their name, link to their website, description (which comes on clicking learn more), The technologies they use and their contact email.

## Abstract:

Using Flask and web libraries, the data has been stored and returned in JSON format so that it could be easily consumed by applications (web/mobile).

## Introduction:

I’ve used Flask (a web micro framework) to write the API which handles the requests on GET parameter and the URL endpoints that GSOC website uses to fetch the data.

## Result

```{
 "result": [
   {
     "contact": "johannes.schauer@uni-wuerzburg.de",
     "description": "The 3D Toolkit is a collection of programs that allow working with 3D point cloud data. The tools include a powerful and efficient 3D point cloud viewer called \"show\" which is able to open point clouds containing millions of points even on older graphics cards while still providing high frame rates. It provides bindings for ROS, the Robotic Operating System and for Python, the programming language. Most of the functionality of 3DTK is provided in the form of \"tools\", hence the name which are executed on the command line. These tools are able to carry out operations like simultaneous localization and mapping (SLAM), plane detection, transformations, surface normal computation, feature detection and extraction, collision detection and dynamic object removal. We support Linux, Windows and MacOS. 3DTK contains the implementation of several complex algorithms like multiple SLAM and ICP implementations as well as several data structures like k-d trees, octrees, sphere quadtrees and voxel grids. The software is home of the implementation of algorithms from several high impact research papers. While the Point Cloud Library (PCL) might be dead, 3DTK is alive and actively maintained by an international team of skilled researchers from all over the world, ranging from Europe to China. Know-how from 3DTK influenced several businesses from car manufacturers to mineral excavation or archaeological projects.",
     "link": "http://threedtk.de",
     "organization": "3DTK",
     "technologies": [
       "c/c++",
       " cmake",
       "opencv",
       "ros",
       "boost"
     ]
   },
```

## Conclusion

I’ve learned web scraping, developing APIs, and backend tools that could serve various platforms. I’ve also learned about  JSON, a central and convenient format of data communication.

## References:

https://docs.python-requests.org
www.pythonforbeginners.com/requests/using-requests-in-python
https://flask.pocoo.org


