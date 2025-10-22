R/RStudio
=========

Using TensorFlow
^^^^^^^^^^^^^^

The TensorFlow library is pre-installed in "RStudio 2025.09.0 (R 4.5.1)" and will be used for this example. To use GPUs, you will need to specify these additional modules: ``CUDA/11.8.0 cuDNN/8.7.0.84-CUDA-11.8.0`` and select the GPU queue. If you are using a different version of R/RStudio, you can install the TensorFlow library by entering the command ``remotes::install_github("rstudio/tensorflow")`` after launching the session.

To set up TensorFlow, we'll first need to load the library and then run the install command. Enter ``library(tensorflow)`` then run ``install_tensorflow(version = "2.10")``. The install step may take a while. 

Once the install is complete, you will need to switch to the ``r-tensorflow`` virtual environment in R Studio. To do this, go to Tools > Global Options > Python > Select > Virtual Environments and then double-click the ``~/.virtualenvs/r-tensorflow/bin/python`` option. Click Apply to confirm the change. Click Yes on the dialog that appears asking you to restart R Studio. You do not need to close the session or tab, but you can refresh the page.

If you are unfamiliar with using TensorFlow for R, a beginner's tutorial can be found here: `<https://tensorflow.rstudio.com/tutorials/quickstart/beginner>`_.

To learn more about using R/RStudio on Buddy, consider signing up for a workshop session hosted by the `Software Carpentries at UCO <https://library.uco.edu/carpentries>`_.

You can also reference the R Documentation here: `<https://cran.r-project.org/manuals.html>`_.
