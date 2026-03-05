API
===

To use the API, you will first need to find your API key, accessible from the UI. Click on your user avatar and navigate to Settings, and then the Account page in settings. Here you will be able to see the API Keys. Expand this section and copy either the JWT token or create an API key.

.. image:: /_static/img/buddygpt_api.PNG
   :width: 100%
   :align: center
   :alt: BuddyGPT Settings page with API key information

API Endpoint
------------

Use the following endpoint to connect to the API:

For an OpenAI API-compatible response, use:

.. code-block:: text

   https://ai.hpc.uco.edu/api/chat/completions


Accessing Stored LLMs on UCO HPC
---------------------------------

Transformers by Hugging Face
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the Transformers framework, we provide the following models:

**GPT-OSS-20b**
   - An open-source model from OpenAI
   - This model has been quantized using the MXFP4 format
   - Requires about 14 GB of GPU memory

**Command-R**
   - An open-source model from Cohere
   - This model has not been quantized and its tensors are in BF16 precision
   - Requires more than 20 GB of GPU memory to run non-quantized version

**GPT-OSS-120b**
   - An open-source model from OpenAI
   - This model has been quantized using the MXFP4 format
   - Requires about 80 GB of GPU memory

**Qwen3-Coder-Next**
   - An open-source model from Alibaba
   - This model has not been quantized and its tensors are in BF16 precision
   - Requires more than 20 GB of GPU memory to run non-quantized version

.. note::
   These models are contained in the following path:

   .. code-block:: text

      /opt/ai_models

Downloading Transformers Compatible Models
------------------------------------------

.. note::
   Before proceeding with a model install, consult `Accessing Stored LLMs on UCO HPC`_ to see if UCO HPC already provides the model you intend to use!

In order to install models from Hugging Face, you will need to create an account using https://huggingface.co/join. Once you have an account, you will then need to generate a token for our system using the documentation provided under the `User access tokens <https://huggingface.co/docs/hub/en/security-tokens>`_ page. If you only intend to install publicly available models and data, then usually read permissions are sufficient for the token.

Token Type Recommendation
~~~~~~~~~~~~~~~~~~~~~~~~~

When creating your Hugging Face access token (Settings > Access Tokens), choose the token type based on your use case:

- **Read (Recommended):** Best for most users in this guide. Allows downloading models and datasets.
- **Write:** Only needed if you plan to upload files or push changes to repositories on Hugging Face.
- **Fine-grained:** Useful if you want to limit access to specific repositories while keeping only the minimum required permissions.

For the steps in this section (``hf auth login`` and model download), a **Read** token is recommended.

.. image:: /_static/img/buddygpt_api_hf_token.PNG
   :width: 100%
   :align: center
   :alt: Create token on Hugging Face from settings page

.. image:: /_static/img/buddygpt_api_hf_token2.PNG
   :width: 100%
   :align: center
   :alt: Access Token Output


After you have your account set up, you can search models using the `Hugging Face Models <https://huggingface.co/models>`_ page. Here you can refine your search based on the task you want to complete, model size, and dependent libraries. Once you have identified a model that you would like to run, review the model card, paying attention to the libraries needed and examples provided. If necessary, accept the terms of use for the model. For example, Meta's Llama 3.1 requires you to accept a community license agreement. However, at the time of writing this documentation, OpenAI's gpt-oss-20b does not require a license agreement.

.. note::
   Depending on the model, it can take 30 minutes or more to get access to the model once you have accepted the terms of use.

At this point, all necessary libraries should be installed in either your custom environment or UCO HPC's provided environment and we can begin downloading the LLMs we would like to run. If you are using our Transformers module, ``HF_HOME`` and ``HF_HUB_CACHE`` will point to your project's directory, ensuring that your home directory does not fill up. If you are not using our module, be sure these variables are appropriately set before proceeding. There are several ways to install a model, however, we often suggest that you use the ``huggingface-cli``. For more in-depth information about ``huggingface-cli`` (such as how to view models and delete them) see `Command Line Interface (CLI) <https://huggingface.co/docs/huggingface_hub/en/guides/cli>`_. The ``hf cache scan`` and ``hf cache delete`` sections are particularly useful for managing models.

Once the ``huggingface-cli`` is available, you can set up your token associated with our system using the following:

.. code-block:: bash

   hf auth login

When prompted for the token, provide the one you generated at the beginning of this section. When asked if you would like to "Add token as git credential?" you may type "n", if you do not intend to use the token as a git credential. For new users, "n" is usually preferred for simplicity.

.. important::
   To protect your tokens, it is suggested that you remove system-wide read privileges:

   .. code-block:: bash

      chmod o-r /opt/ai_models/.cache/stored_tokens
      chmod o-r /opt/ai_models/.cache/token

Now that we have our tokens set up and we have accepted the terms of use, we can install our model from the command line. Here, we will install a very simple Gemma model (``google/gemma-3-270m-it``) into our directory ``/opt/ai_models/gemma-3-270m-it``:

.. code-block:: bash

   hf download --local-dir /opt/ai_models/gemma-3-270m-it google/gemma-3-270m-it

.. tip::
   On Hugging Face, there are often different types of LLMs. For example, some have "instruct" in their name or specify that they are instruct models. Instruct models are, as the name implies, instruction models. These models are most likely what you want as they are ideal for specifying tasks for the LLM to perform and are the models used in common chat interfaces. In contrast, the base models make no assumption about structure and are attempting to only complete the text provided.

After this installation completes, you will then have access to your installed model! See the next section for instructions on running this LLM from Python.

Downloading and Uploading Models to UCO HPC
-------------------------------------------

You can bring models from Hugging Face onto the UCO HPC cluster using either direct downloads over SSH or by dragging and dropping via the Open OnDemand web interface.
For heavily quantized GGUF models meant for ``llama-server``, it is often practical to download them straight to the cluster via SSH.

1. **Connect to the HPC server:**
   
   .. code-block:: bash

      ssh username@hpc.uco.edu

   .. image:: /_static/img/buddygpt_api_ssh.PNG
      :width: 100%
      :align: center
      :alt: HPC SSH connection example

2. **Setup your environment:**
   Create a Python virtual environment and install the ``huggingface_hub`` library using ``pip``.

   .. code-block:: bash

      python -m venv ai_hub
      source ai_hub/bin/activate
      pip install huggingface_hub

3. **Authentication:**
   Retrieve an API Key from Hugging Face (under Settings > Access Tokens) and authenticate. 
   You also need to set ``HF_HOME`` to point to the cache directory.
   
   .. code-block:: bash

      hf auth login --token <API Key>
      export HF_HOME=/opt/ai_models/.cache
   
   .. image:: /_static/img/buddygpt_api_hf_login.PNG
      :width: 100%
      :align: center
      :alt: HPC SSH connection example

4. **Find Model Weights (GGUF):**
   You will need GGUF model formats to run on ``llama``. On Hugging Face, look under Quantizations (``unsloth`` models are usually pretty good). It's recommended to find weights with the ``Q4_K_M`` quantization. Note the repository name and exact filename(s).

5. **Download and Link:**
   Use the CLI to pull the model and generate a symbolic link to the destination directory. Replace the parameters with your model info.
   
   .. code-block:: bash

      hf download <repo name> --include="<file name pattern>"
      # Link to the first (or only) file
      ln -s $(hf download <repo name> <filename>) /opt/ai_models/<short name>

   .. note::
      To list downloaded models at any time, run: ``hf cache ls``


Models and Building llama-server
--------------------------------

If you plan to run models using ``llama-server``, jobs should be scheduled to run on a **GPU node**. You can view example scripts at `/opt/creic-server-scripts/ai-scripts`.

If ``llama.cpp`` is not already built with CUDA or if you need to build it yourself, you will need to load dependencies and compile from source.

**Prerequisites:** Needs ``CUDA-12.8`` and ``CMake``.

.. code-block:: bash
   
   module load CUDA/12.8 CMake/4.0.3-GCCcore-14.3.0 GCCcore/14.3.0

**Compilation Steps:**

.. code-block:: bash

   git clone https://github.com/ggml-org/llama.cpp.git
   mkdir llama.cpp/build
   cd llama.cpp/build
   cmake .. -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES=52
   cmake --build . --config Release -j 30

Once built, you can execute the compiled binaries with your downloaded GGUF models!


cURL Example
~~~~~~~~~~~~

You can also use cURL to interact with the API:

.. code-block:: bash

   curl -X POST https://ai.hpc.uco.edu/api/chat/completions \
     -H "Authorization: Bearer your-api-key-here" \
     -H "Content-Type: application/json" \
     -d '{
       "model": "llama-3.1-70b",
       "messages": [{"role": "user", "content": "Hello!"}],
       "stream": false
     }'

.. note::
   Replace ``your-api-key-here`` with your actual API key obtained from the BuddyGPT UI settings.
