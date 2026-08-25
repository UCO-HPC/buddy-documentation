Account and Software Requests
=============================

These are the requirements for obtaining an account on Buddy:

- If you are a current UCO faculty member, you just need to provide your name and UCO email address when emailing hpc@uco.edu.
- If you are a current UCO student, you will need to have a professor send an email to hpc@uco.edu on your behalf to get an account created for you.
- If you are a non-UCO faculty member within the state of Oklahoma collaborating with a UCO faculty member, the UCO faculty member needs to send an email on your behalf to hpc@uco.edu have your account created.
- If you are not a UCO faculty member or student but you are attending a UCO-hosted workshop, please provide the name of your institution, your full name, and email address when emailing hpc@uco.edu.

General Account Request
-----------------------
A general account is an account made for professors or researchers and their
collaborators, and is given normal permissions on Buddy. To make a general
account request please email hpc@uco.edu and provide us with the following
information:
 
- Requester's name
- Requester's UCO username (if you are from another university, please provide
  the username given by your institution along with the name of the institution)
- Requester's department
- Required software
- Do you need a project space?
 
  - Are there any special permissions required for this directory? For example:
    "I don't want collaborators to make files", "I want collaborators to be able
    to read and make files", etc.
 
- Are you a professor or a student?
 
  - If professor: do you have any students you need to add? For each, provide:
 
    - Full name
    - Email address
 
- If you are collaborating with UCO faculty, please provide the names and email
  addresses of your collaborators

Classroom Account Request
-------------------------
A classroom account is one given to students who will be using Buddy as part of
a class. The instructor is given a general account, while students receive
classroom accounts, which expire after the class ends and which have more
limited functionality than general accounts.
 
To make a classroom account request please email hpc@uco.edu and provide us with
the following information.
 
Course information
~~~~~~~~~~~~~~~~~
 
- **Course name and number** (for example, CMSC 4343)
- **CRN** — the five-digit Course Reference Number for the section
- **Semester and year** (for example, Fall 2026)
 
.. note::
 
   The CRN is used to build the class group name, so please double-check it
   against your course listing. A CRN identifies one specific section in one
   specific semester, which is what lets us keep this term's class separate from
   the same course taught in a previous term.
 
**Combined and cross-listed sections.** If your class is a combined section —
two CRNs meeting together, such as an undergraduate and graduate section of the
same course — please provide **both CRNs**, along with **both course numbers**
if they differ. For example:
 
- CMSC 4343, CRN 12075 and CRN 12125 (same course number, two sections)
- CMSC 4343 (CRN 12075) combined with CMSC 5343 (CRN 12078)
 
Both sections will share one class group and one shared folder. If you would
rather keep them separate, let us know and we will create them as two classes.
 
If you teach **more than one course** that needs accounts, please tell us which
students belong to which course — either send one roster per course, or include
a column in the spreadsheet identifying the course or CRN for each student.

Student roster
~~~~~~~~~~~~~
 
A spreadsheet (``.xlsx``) or CSV containing, for each student:
 
- Email address
- First name
- Last name
 
The column order does not matter and you do not need to reformat anything.
 
Two things that help:
 
- **Please leave yourself off the student roster.** We will add you as the
  instructor separately, with instructor-level access to the class folder. If
  you already have a Buddy account, we will use your existing account — you do
  not need a new one, and nothing about your existing account or files changes.
  If you do not have one yet, we will create it as part of setting up the class.
- If any participants have **non-UCO email addresses**, let us know their
  institution so we can format their usernames correctly.
 
Shared class folder
~~~~~~~~~~~~~~~~~~
 
Most classes want a shared folder on the cluster. We have three standard
layouts — please tell us which one fits your course, or describe what you need
and we will advise.
 
**Option A — No shared folder**
 
Students receive their own accounts and home directories only. Choose this if
students will work entirely in their own space.
 
**Option B — Distribution only**
 
A single folder where you post datasets, starter code, and reference material.
 
- You can add, edit, and delete files
- Students can read and copy files, but cannot modify or add anything
 
**Option C — Full class layout**
 
A folder tree covering distribution, individual student work, and your own
private space::
 
    CMSC4343-share/
    ├── materials/     you post files here; students can read them
    ├── students/      one folder per student
    │   ├── jsmith3/     only that student (and you) can open it
    │   └── mbarrett10/
    ├── instructor/    private to you
    └── shared/        optional: everyone can read and write
 
- Each student gets their own folder that only they and you can open. Students
  cannot see one another's work.
- You can read and write in every student folder, so you can collect or return
  work.
- The optional ``shared/`` folder is a space where the whole class can read and
  write each other's files, which is useful for group projects.
 
Let us know whether you would like the optional ``shared/`` folder included.
 
The class folder appears in your home directory and in each student's home
directory. Tell us what you would like it named — for example
``CMSC4343-share``.
 
Software
~~~~~~~
 
If your class needs licensed or restricted software (Gaussian, MATLAB, ANSYS,
and so on), tell us which packages and we will add the students to the
appropriate access groups at the same time.

Email template
~~~~~~~~~~~~~
 
To make this easier, copy the template below into an email to hpc@uco.edu, fill
in the blanks, and attach your roster. Delete any lines that do not apply.
 
.. code-block:: text
 
    To: hpc@uco.edu
    Subject: Buddy classroom account request — [COURSE NUMBER], [SEMESTER]
 
    Course name and number:
    CRN:
    Semester and year:
 
    Combined/cross-listed section?  (yes/no)
      If yes, second CRN:
      If yes, second course number (if different):
 
    Roster: attached as a spreadsheet with each student's email address,
    first name, and last name.
 
    Do I already have a Buddy account?  (yes/no)
 
    Any students with non-UCO email addresses?  (yes/no)
      If yes, their institution:
 
    Software needed (Gaussian, MATLAB, ANSYS, etc.):
 
    Shared class folder:  (A / B / C — see options above)
      If C, include the optional shared/ folder for group work?  (yes/no)
      Name for the folder as it should appear in home directories:
 
    Anything else we should know:
 
Here is the same template filled in, as an example:
 
.. code-block:: text
 
    To: hpc@uco.edu
    Subject: Buddy classroom account request — CMSC 4343, Fall 2027
 
    Course name and number: CMSC 4343
    CRN: 12075
    Semester and year: Fall 2027
 
    Combined/cross-listed section?  yes
      If yes, second CRN: 12078
      If yes, second course number (if different): CMSC 5343
 
    Roster: attached as a spreadsheet with each student's email address,
    first name, and last name.
 
    Do I already have a Buddy account?  yes
 
    Any students with non-UCO email addresses?  no
 
    Software needed: MATLAB
 
    Shared class folder:  C
      If C, include the optional shared/ folder for group work?  yes
      Name for the folder as it should appear in home directories:
      CMSC4343-share
 
    Anything else we should know: Two students are auditing and are not on
    the official roster; I have included them at the bottom of the file.

What happens next
~~~~~~~~~~~~~~~~

Each student receives an email containing their username, a one-time password,
and instructions for logging in at buddy.uco.edu and changing their password.

A few things worth planning around:

- **Students who add the course later** can be added at any time. Please send
  us the student's name and email address, along with the course number, CRN,
  and semester so we know which class to add them to. If you teach more than
  one class on Buddy, or your class is a combined section, this is what tells
  us which group and shared folder they belong in.
- **If a student drops the course, please let us know** so we can remove their
  access to the class folder. Cluster accounts are not linked to enrollment, so
  a student keeps access to the class materials until we are told to remove it.
- **Class folders and groups remain in place after the semester ends.** Let us
  know if you would like anything archived or removed.

.. note::

   Buddy's shared class folder is intended for data and code that is too large
   for D2L. It is not a replacement for your LMS — assignment submission,
   deadlines, and grading should stay in D2L.
   
Software Request
----------------
To make a software request please email hpc@uco.edu with the name of the software and version information or other requirements if they exist.

.. note::
   While we try to provide requested software this might not always be possible or may take a long time to work through installation and integration issues. We will keep you updated as mush as possible throughout the process and will try to work with you to fulfill your needs. That being said, most software can be installed quickly and easily.
