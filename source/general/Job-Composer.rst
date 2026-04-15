Job Composer
============

To create jobs through Open OnDemand, navigate to Jobs > Jobs Composer from the dashboard.

// insert image here //

You will see the below output opened in a new tab. The list of options available to create new jobs are: From Default Template, From Template, From Specified Path, and From Selected Job.

// insert image here //

Create Job
----------

From Default Template
^^^^^^^^^^^^^^^^^^^^^

1. On the Job Composer page, select **New Job > From Default Template**.

   // insert image here //

   A new job will be created like below.

   // insert image here //

2. You can modify the options of the created job like name, Cluster, Job Script using the **Job Options** button.

   // insert image here //

   After you click the button, you can change the job options like below:

   // insert image here //

   In the above example, the Name has been changed from default (Simple Sequential Job) to TestJob. After the name has been modified, hit the **Save** button and the modified job name will be replicated in the Job Composer page.

   Output:
   // insert image here //

3. Now, modify the submit script ``main_job.sh``.

   a. On the Job Composer page, hit the **Open Editor** button under Submit Script section.

      // insert image here //

   b. In the text editor opening in a new tab, modify the Job Script with the below content.

      // insert image here //

   c. After the job submission script ``main_job.sh`` has been updated, hit the **Save** button. Go back to the previous tab to see the updated script.

      // insert image here //

   The Job Details pane also shows important information related to the job.

   // insert image here //

   .. note::
      If you want to open the submit script file directly in the terminal, use the **Open Terminal** button. **Open Dir** will open the directory in the file manager.

4. Now, hit the **Submit** button. The status will change from *Not Submitted* to *Queued* or *Running*. You will see a success message alert at the top of your page. The status will change to *Completed* once finished.

   // insert image here //

5. To view the output, click the generated output file ``slurm-<job-id>.out`` under **Folder contents** in the Job Details section.

   // insert image here //

   Output (slurm-<job-id>.out):
   // insert image here //
