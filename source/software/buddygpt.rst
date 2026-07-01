.. _buddy-gpt:

BuddyGPT
========

BuddyGPT is an LLM service that makes open source LLM models like LLaMA accessible to UCO researchers. It is hosted entirely with on-prem resources at UCO, not only providing democratized access but adding another layer of control compared to commercial services. Chats, documents, and models are not shared between users nor used for training.

There are two modalities for interacting with BuddyGPT, UI, and API, and additional functionality for both modalities is under active development. This system is integrated with a PostgreSQL vector database in the backend to enable retrieval-augmented generation (RAG) functionality.

.. warning::
   Note this service is a pilot and provides only limited safety measures. Models may hallucinate or generate offensive content. BuddyGPT should not be used for any illegal, harmful, or violent purposes.

.. danger::
   **DeepSeek is prohibited on all state-owned devices.** On March 3, 2025, Governor Kevin Stitt directed the Office of Management and Enterprise Services (OMES) to review DeepSeek. Following that review, the State of Oklahoma has banned the use of DeepSeek on all state-owned devices (laptops, desktops, and mobile phones/tablets). Key reasons include:

   - **Security concerns:** DeepSeek collects extensive user data (chat history, uploaded files, IP addresses) and stores it in China, violating the state CIO's data storage standard.
   - **Compliance issues:** Use of DeepSeek may violate regulations such as FERPA, HIPAA, IRS Pub 1075, and CJI, and conflicts with Executive Order 2024-11.
   - **Adversarial manipulation:** DeepSeek-R1 has shown high susceptibility to adversarial attacks that can bypass safety measures.
   - **Lack of safeguards:** DeepSeek lacks a layered security architecture and has known vulnerabilities such as weak encryption, increasing the risk of data leakage.

   Do **not** select or use any DeepSeek model within BuddyGPT. If you have questions, contact the OMES Information Services division.

.. danger::
   Do not input, by any method, any data into these systems that your research institution would consider sensitive or proprietary. Do not input, by any method, any data into these systems that is regulated by State or Federal Law. This includes, but is not limited to, HIPAA data, Export Controlled data, personal identification numbers (e.g. SSNs) or biometric data.

Access
------

Access is currently being given on a per request basis. Navigate to https://ai.hpc.uco.edu/ and log in using your UCO credentials. This will create a pending account.

Next, reach out to hpc@uco.edu with the subject line "BuddyGPT Access Request". In the description, provide a brief description of how you intend to use the service and if you would like access to the UI, API, or both. An admin will assess and approve your request and get back to you.



.. image:: /_static/img/buddygpt_ui_login.PNG
   :width: 80%
   :align: center
   :alt: BuddyGPT login page (authentication)

.. toctree::
   :maxdepth: 1
   :caption: BuddyGPT Guides

   buddygpt_ui
   buddygpt_api
