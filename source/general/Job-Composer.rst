Job Composer
======================

To create jobs through Open OnDemand, navigate to Jobs > Jobs Composer from the dashboard
// insert imgage here //

You will see the below output opened in a new tab.
 The list of options available to create new jobs are: 
  From Default Template, From Template, From Specified Path, and From Selected Job.

// insert image here //

Create Job
-------------------------------------
From Default Template
1. On the Job Composer page, select New Job > From Default Template.
  // insert image here //
  A new job will be created like below.
  // insert image here //
2. You can modify the options of the created job like name, Cluster, Job Script using the Job Options button  
  // insert image here //
  After you click the button, you can change the job options like below
  //insert image here //
  In the above example, the Name has been changed from default (Simple Sequential Job) to TestJob. 
  AFter the name has been modified, hit the Save button and the modified job name will be replicated in the Job Composer page like below.
  Output:
  // insert image here //
3. Now, modify the submit script main_job.sh.
      a. On the Job Composer page, hit the Open Editor button under Submit Script section.
      // insert image here //
      b. In the text editor opening in a new tab, modify the Job Script with the below content.
      // insert image here //
      c. After the job submission script main_job.sh has been updated with the above code, hit the Save button.
       Now, go back to the previous tab and you will see the submission script updated.
      // insert image here //
      The above Job Details pane also shows important information related to the job.
      //insert image here // 
      Note : If you want to open the submit script main_job.sh file directly in the terminal, 
      use the >_Open Terminal button. Open Dir button will open the directory of the submit script in file manager.
4. Now, hit the submit button to submit your Test Job. Thus, the status will be changed from Not Submitted to Queued or
 Running and also you will get a success message alert at the top of your page saying that Job was successfully submitted.
 You will see the status Completed after the job execution gets finished.
// insert image here //
5. To view the output after the job finishes, click the generated output file slurm-<job-id>.out 
 under Folder contents in Job Details section.
 //insert image here//
 Output(slurm-<job-id>.out):
 // inseret image here //

    

