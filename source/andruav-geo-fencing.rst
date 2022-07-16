.. _andruav-geo-fencing:

===================
Andruav Geo Fencing
===================

Geo Fence means that you define areas where you that is safe for your drone to fly in and other areas that is unsafe or forbidden to fly over them.

This is not GEO fence that Ardupilot support. This Geo-Fencing is controlled by Andruav itself not ardupilot. It is very flexible.

.. youtube:: Vlt3dbQ30W0


|

To access Geo-Fence click `https://cloud.ardupilot.org:8001/mapeditor.html <https://cloud.ardupilot.org:8001/mapeditor.html>`_ .

Geo-Fence Manager allows you to design geo-fences and mission plans for multiple drones at the same time.



|

In the below image you can see *two* mission plans together with geo-fences regions. There is a green Geo-Fence region but inside it a no fly zone in red. ANother no-fly zone exists outside the green area. 

.. image:: ./images/_new_map4.png
        :align: center
        :alt: Mission Planner

you can export each mission plan as a file to be uploaded from :ref:`webclient-whatis`. Geo-Fences on the other side are saves for all the group in the system database.
Geo-Fences will be active each time Andruav Mobile starts until it is deleted by `Geo-Fence editor <https://cloud.ardupilot.org:8001/mapeditor.html>`_ .


Rules of Geo-Fence
==================
#. If there is only red *no-fly* zones. then you can fly any where except these areas.
#. If there is one or more *green-fly* zone you need to fly into one of these areas.
#. A red area can be inside a green area. You always need to be in the green but not in the red.

|

**The following are good fence example:**


.. image:: ./images/good_fence1.png
   :height: 400px
   :alt: Good fence example 1


.. image:: ./images/good_fence2.png
   :height: 400px
   :alt: Good fence example 2


|

**The following are bad fence example:**


.. image:: ./images/bad_fence2.png
   :height: 400px
   :alt: Bad fence example 2


.. image:: ./images/bad_fence3.png
   :height: 400px
   :alt: Bad fence example 2



Also this is a bad situation as green areas are defined and drone is out of it.


.. image:: ./images/bad_fence1.png
   :height: 400px
   :alt: Bad fence example 1


