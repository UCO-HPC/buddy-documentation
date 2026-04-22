Job Composer
============

The Job Composer allows you to manage Slurm jobs without needing to use the command line,
 providing a built-in text editor for your SBATCH scripts and easy access to output files.

To create jobs through Open OnDemand, navigate to **Jobs > Jobs Composer** from the dashboard.

.. image:: ../_static/img/ondemand_nav_Job.png
   :alt: Navbar-Jobs of the ondemand

You will see the below output opened in a new tab. The list of options available to create new jobs are: From Default Template, From Template, From Specified Path, and From Selected Job.

.. image:: ../_static/img/ondemand_jobcomp_def.png
   :alt: choose an option for create a job

Create Job
----------

From Default Template
^^^^^^^^^^^^^^^^^^^^^

1. On the Job Composer page, select **New Job > From Default Template**.

   .. image:: ../_static/img/ondemand-jobs-output.png
      :alt: select from default template.

   A new job will be created like below.

   .. image:: ../_static/img/ondemand-jobs-default-create.png
      :alt: Job created

2. You can modify the options of the created job like name, Cluster, Job Script using the **Job Options** button.

   .. image:: ../_static/img/ondemand-jobs-default-modify.png
      :alt: option for modifying created job

   After you click the button, you can change the job options like below:

   .. image:: ../_static/img/ondemand_default_jobmodify1.png
      :alt: Jop options were displayed

   In the above example, the Name has been changed from default (Simple Sequential Job) to TestJob. After the name has been modified, hit the **Save** button and the modified job name will be replicated in the Job Composer page.

   Output:
   
   .. image:: ../_static/img/ondemandjobs-default-modify2.png
      :alt: TestJob is created

3. Now, modify the submit script ``main_job.sh``.


   a. On the Job Composer page, hit the **Open Editor** button under Submit Script section.

      .. image:: ../_static/img/ondemand_jobmodify3.png
         :alt: Open editor 

   b. In the text editor opening in a new tab, modify the Job Script with the below content.

      .. image:: ../_static/img/ondemand-jobs-default-modifyscript1.png
         :alt: Modify the job script content

   c. After the job submission script ``main_job.sh`` has been updated, hit the **Save** button. Go back to the previous tab to see the updated script.

      .. image:: ../_static/img/ondemand_jobsmodifying4.png
         :alt: updated transcript is shown

   The Job Details pane also shows important information related to the job.

   .. note::
      If you want to open the submit script file directly in the terminal, use the **Open Terminal** button.
      **Open Dir** will open the directory in the file manager.

4. Now, hit the **Submit** button. The status will change from *Not Submitted* to *Queued* or *Running*. You will see a success message alert at the top of your page. The status will change to *Completed* once finished.

   .. image:: ../_static/img/ondemand-jobs-default-submit.png
      :alt: Jub Submitted

5. To view the output, click the generated output file ``slurm-<job-id>.out`` under **Folder contents** in the Job Details section.

   .. image:: ../_static/img/ondemand-jobs-default-modify5.png
      :alt: To view the output

   **Output (slurm-<job-id>.out)**:

   .. image:: ../_static/img/ondemand-jobs-default-viewoutput.png
      :alt: Script Output

From Template
^^^^^^^^^^^^^^^^^^^^^

Instead of retyping the Slurm attributes and job parameters for your new job, you can create a custom template and use as a basis for your future jobs.
It also saves time. Also, it’s easier and faster to create a custom template in Open OnDemand. Follow the below steps to create a custom template and compose job from that template.

1. First, create a directory called ``custom_template`` under your home directory.

   .. code-block:: bash

      mkdir custom_template

2. Create the following files, ``input.txt`` and ``script.sh`` under the ``custom_template`` directory.

   input.txt:
      
      .. code-block:: bash

         Ubuntu,apt
         Debian,apt
         CentOS,yum
         Arch Linux,pacman
         Fedora,dnf

   script.sh:

      .. code-block:: bash

         #!/bin/bash
         #SBATCH --job-name=template_test

         while IFS= read -r line; do
            if [[ "$line" == *"apt"* ]]; then
               printf '%s\n' "$line"
             fi
         done < input.txt

   The bash script **script.sh** will read the input file line by line and if it finds a line 
   that has the string **apt**, then, it will print the line.

3. The custom template is ready and available under the path **<home></your-username></custom_template>**. Now, using Open OnDemand, you can create a template.


   a. Go to **Jobs > Jobs Composer** from the dashboard. Select the **templates** tab.

      .. image:: ../_static/img/ondemand-jobs-customtemp-create.png
         :alt: Select template from headers

   b. Select New Template from the Templates page

      .. image:: ../_static/img/ondemand-jobs-customtemp-new.png
         :alt: To create new template

   c. Now, you can enter the values for the custom template. Enter the path and name to the template and hit Save button

      .. image:: ../_static/img/ondemand-jobs-editor-customtemp.png
         :alt: To edit custom template built-in

   d. You will see the template has been successfully created and you will see a similar output like below. 
      
      .. image:: ../_static/img/ondemand-jobs-customtemp-dispalyed.png
         :alt: Show the custom-template

      Also, on the right bottom, you can see **Template location** and also **Folder Contents** with the files **input.txt, script.sh** and an additional file called **manifest.yml**.

4. Now, you can create a job from the template. Select the **Create New Job** button from the **Templates** page. 
   A new job will be created using the custom template and you will be automatically redirected to the **Jobs** page      

   .. image:: ../_static/img/ondemand-jobs-customtemp-createjob.png
      :alt: Create job from template page

5. Submit the job by clicking **Submit** button and you will the status change from **Not Submitted** to **Queued** or **Running**. 
   You will also see a success alert for the job submission at the top of your page.

   .. image:: ../_static/img/ondemand-jobs-customtemp-submit.png
      :alt: To submit the custom template

6. After the status changes to **completed** which indicates that the job has finished, select the output file **slurm-<job-id>**.
   out under the **folder contents** section on the right pane of the window.  

   .. image:: ../_static/img/ondemand-jobs-customtemp-outputjob.png
      :alt: To output the content 

   **Output(slurm-<job-id>.out):**
   
      .. image:: ../_static/img/ondemand-jobs-customtemp-viewoutput.png
         :alt: Output content

From Specified Path
^^^^^^^^^^^^^^^^^^^^^^^

   Creating jobs from **Specified Path** is one of the simplest ways of creating a job but there are things you need to take note of.


.. note::
   If you want to open the submit script file directly in the terminal, use the **Open Terminal** button.
   **Open Dir** will open the directory in the file manager.

.. warning::
   If you have a submission script called **script.sh** in your home directory and you specify path as **home/<your-username>**, it will cause all the content such as files and sub directories in the home directory to be copied under the new workspace which is a bad and space overkill. 
   It’s recommended to create a directory and place all the necessary scripts under that directory and specify it as a source path for your jobs.

1. First, create a directory called **test** under your **home** directory.

   .. code-block:: bash

      mkdir test

2. Create the following files, **script.py**, **script.sh** under **test** directory.  

   script.sh:
      
      .. code-block:: bash

         #!/bin/bash

         #SBATCH --job-name=maxFib      ## Name of the job
         #SBATCH --output=maxFib.out    ## Output file
         #SBATCH --time=0-00:10:00      ## Job Duration
         #SBATCH --ntasks=1             ## Number of tasks (analyses) to run
         #SBATCH --cpus-per-task=1      ## The number of threads the code will use
         #SBATCH --mem-per-cpu=100M     ## Real memory(MB) per CPU required by the job.

         ## Load the python interpreter
         module load python

         ## Execute the python script and pass the argument/input '90'
         srun --export=ALL python script.py 90

   script.py:

      .. code-block:: bash

         import sys
         import os

         if len(sys.argv) != 2:
            print('Usage: %s MAXIMUM' % (os.path.basename(sys.argv[0])))
            sys.exit(1)

         maximum = int(sys.argv[1])

         n1 = 1
         n2 = 1

         while n2 <= maximum:
            n1, n2 = n2, n1 + n2

         print('The greatest Fibonacci number up to %d is %d' % (maximum, n1))

.. important::
   If you have a close look at the submit script **script.sh**, it has --export=ALL flag in the srun command. 
   The flag is mandatory if you want to submit and run jobs to the **Discovery** cluster through Open OnDemand.

3. Now, navigate to **Jobs > Job Composer**. Select **New Job > From Specified Path**.

   .. image:: ../_static/img/ondemand-jobs-path-create.png
      :alt: To choose the specific path

4. Enter the source path to **test** directory and give a name for the job as **PythonJob**. 
   Also, give a name for the submission script as **script.sh** and specify the cluster name as **Discovery**. Hit **Save** button after setting all the job options.

   .. image:: ../_static/img/ondemand-jobs-path-input.png
      :alt: To show the path output

5. You will see a new job created in the **Jobs** page. Now, select the **Submit** button to launch the job.

   .. image:: ../_static/img/ondemand-jobs-path-submit.png
      :alt: To show the path output

6. Now, you will see the status changing from **Not Submitted** to **Queued/Running**. 
   After the status changes to **Completed**, you can view the output **maxFib.out** under Folder Contents on the right pane.

   .. image:: ../_static/img/ondemand-jobs-relativepath-detail.png
      :alt: To show the deatil of created job

**Output(maxFib.out):**

   .. image:: ../_static/img/ondemand-jobs-relativepath-detail.png
      :alt: To show the output


From Selected Job
^^^^^^^^^^^^^^^^^^^^^^

   1. To create a new job from the existing one, select **New Job > From Selected Job.**

      .. image:: ../_static/img/ondemand-jobs-selectedjob-create.png
        :alt: To select from Selected Job

   2. You will have a new job(copy) created in the **Jobs** page.

      .. image:: ../_static/img/ondemand-jobs-selectedjob-output.png
         :alt: To see the created job in the folder

.. note::
   You can also use the buttons **Stop, Delete** to stop a running job and delete the selected job respectively
      