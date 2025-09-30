Data Transfer
=============
Data transfer to and from buddy can be done in several ways depending on your needs and the size of the data.

Using SFTP or SCP
-----------------
Small files can be transfered to and from Buddy using a file transfer protol such as SFTP or SCP.

Using Github
------------
For source code it might be preferrable to use git to keep data on Buddy synced with a project. This is acomplished by commiting changes on your local machine, pushing them up to a repository, and pulling the changes down onto Buddy. 

Using Globus (Coming Soon)
--------------------------
For files that are larger than 20Gb, Globus is the prefered method for moving data between the cluster and another source. This can be accomplished by doing the following:

1. Make an Account and Obtain a Globus ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   1. Visit `globusid.org <https://www.globusid.org/>`_
   2. Click ``create a Globus ID``
   3. Fill out account details and for organization be sure to enter "University of Central Oklahoma"

2. Log in with Globus ID
~~~~~~~~~~~~~~~~~~~~~~~~
   1. Visit `globus.org <https://www.globus.org/>`_ and click ``Log In`` in the upper right
   2. Click ``Globus ID to sign in``

.. image:: /_static/img/globus_login.png
  :width: 45%
  :align: center
  :alt: Buddy Globus login
..

   3. Sign in using your globus username and password. (You may not need sign in if you just created your account and a login cookie still exists in your browser)
   4. If this is your first time logging in:

      a. Enter a verification code from your globus verification email
      b. Click ``Continue``
      c. Click ``Continue`` again

   5. Click ``Allow``

3. Connect to Buddy
~~~~~~~~~~~~~~~~~~~
   1. Search ``Buddy`` in the collection search bar

.. image:: /_static/img/collection_search_buddy.png
 :width: 30%
 :align: center
 :alt: Buddy Globus collection search
.. 

   2. Select ``Home storage`` for files smaller than 100Gb otherwise select ``DTN storage``
   3. Click ``Continue``
   4. Choose to Link an identity from ``Buddy OIDC SERVER...``
   5. Sign in using your Buddy username and password
   6. Click ``Allow``

You should now be able to access your buddy home folder or DTN storage. The steps to access both are the same.
